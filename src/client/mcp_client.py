from client.ws_client import websocket_client

import anyio
from mcp.client.session import ClientSession


async def main():
    async with websocket_client("ws://localhost:8000/mcp/ws") as (
        read_stream,
        write_stream,
    ):
        async with ClientSession(read_stream, write_stream) as client:
            await client.initialize()
            tool_result = await client.list_tools()
            print(tool_result)


if __name__ == "__main__":
    import logging

    logging.basicConfig(level=logging.INFO)
    anyio.run(main)
