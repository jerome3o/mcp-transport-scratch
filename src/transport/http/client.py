import anyio
from anyio import create_memory_object_stream
from anyio.streams.memory import MemoryObjectReceiveStream, MemoryObjectSendStream
from typing import Any, AsyncGenerator
from mcp.types import JSONRPCMessage, InitializeResult, LATEST_PROTOCOL_VERSION
from mcp import types
from httpx import AsyncClient
from contextlib import asynccontextmanager


_canned_initization_result = InitializeResult(
    protocolVersion=LATEST_PROTOCOL_VERSION,
    capabilities=types.ServerCapabilities.model_validate(
        {
            "prompts": {},
            "resources": {},
            "tools": {},
        }
    ),
    serverInfo=types.Implementation(
        name="HTTP-only-server",
        version="0.0.1",
    ),
)


@asynccontextmanager
async def client_http_transport(
    url: str,
    httpx_client: AsyncClient | None = None,
) -> AsyncGenerator[
    Any,
    tuple[
        MemoryObjectReceiveStream[JSONRPCMessage],
        MemoryObjectSendStream[JSONRPCMessage],
    ],
]:
    httpx_client = httpx_client or AsyncClient()

    read_stream_writer, read_stream = create_memory_object_stream[JSONRPCMessage](0)
    write_stream, write_stream_reader = create_memory_object_stream[JSONRPCMessage](0)

    async def listen_for_messages_from_client():
        try:
            while True:
                await anyio.sleep(0)
                async for message in write_stream_reader:
                    if message.root.method == "initialize":
                        await read_stream_writer.send(
                            types.JSONRPCResponse(
                                id=message.root.id,
                                result=_canned_initization_result.model_dump(),
                                jsonrpc="2.0",
                            )
                        )
                        await anyio.sleep(0)
                        continue

                    response = await httpx_client.post(url, json=message.model_dump())
                    response.raise_for_status()
                    response_json = response.json()
                    await read_stream_writer.send(
                        JSONRPCMessage.model_validate_json(response_json)
                    )
        except anyio.get_cancelled_exc_class():
            pass

    async with anyio.create_task_group() as tg:
        tg.start_soon(listen_for_messages_from_client)
        yield (read_stream, write_stream)
