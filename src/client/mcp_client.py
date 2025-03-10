from transport.ws.client import client_websocket_transport
from transport.http.client import client_http_transport
from mcp.shared.memory import create_connected_server_and_client_session
from server.mcp_definition import mcp

import anyio
from mcp.client.session import ClientSession

import logging

_logger = logging.getLogger(__name__)


async def validate_client(client: ClientSession):
    _logger.info("Client session started")

    await client.initialize()
    _logger.info("Client initialized")

    list_tool_result = await client.list_tools()
    _logger.info(f"Tool result: {list_tool_result}")

    list_prompts_result = await client.list_prompts()
    _logger.info(f"Prompts result: {list_prompts_result}")

    list_resources_result = await client.list_resources()
    _logger.info(f"Resources result: {list_resources_result}")

    call_tool_result = await client.call_tool("echo_tool", {"data": "Hello, world!"})
    _logger.info(f"Call tool result: {call_tool_result}")

    call_prompt_result = await client.get_prompt("test_prompt")
    _logger.info(f"Call prompt result: {call_prompt_result}")

    read_resource_result = await client.read_resource("test://test_resource")
    _logger.info(f"Read resource result: {read_resource_result}")


async def test_memory():
    _logger.info("Starting in-memory client test")
    async with create_connected_server_and_client_session(mcp._mcp_server) as client:
        await validate_client(client)

    _logger.info("Memory test completed")
    _logger.info("")


async def test_websocket():
    _logger.info("Starting websocket client test")
    async with client_websocket_transport("ws://127.0.0.1:8000/mcp/ws") as (
        read_stream,
        write_stream,
    ):
        _logger.info("Connected to websocket")
        async with ClientSession(read_stream, write_stream) as client:
            await validate_client(client)

    _logger.info("Websocket test completed")
    _logger.info("")


async def test_http():
    _logger.info("Starting HTTP client test")
    async with client_http_transport("http://127.0.0.1:8000/mcp/http") as (
        read_stream,
        write_stream,
    ):
        _logger.info("Connected to HTTP")
        async with ClientSession(read_stream, write_stream) as client:
            await validate_client(client)

    _logger.info("HTTP test completed")
    _logger.info("")


async def main():
    await test_memory()
    await test_websocket()
    await test_http()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    anyio.run(main)
