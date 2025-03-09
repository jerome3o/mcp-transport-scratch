from transport.ws.client import client_websocket_transport
from transport.http.client import client_http_transport

import anyio
from mcp.client.session import ClientSession

import logging

_logger = logging.getLogger(__name__)


async def test_websocket():
    _logger.info("Starting websocket test")
    async with client_websocket_transport("ws://localhost:8000/mcp/ws") as (
        read_stream,
        write_stream,
    ):
        _logger.info("Connected to websocket")
        async with ClientSession(read_stream, write_stream) as client:
            _logger.info("Client session started")
            await client.initialize()
            _logger.info("Client initialized")
            tool_result = await client.list_tools()
            _logger.info(f"Tool result: {tool_result}")
            print(tool_result)
    _logger.info("Websocket test completed")


async def test_http():
    _logger.info("Starting HTTP test")
    async with client_http_transport("http://localhost:8000/mcp/http") as (
        read_stream,
        write_stream,
    ):
        _logger.info("Connected to HTTP")
        async with ClientSession(read_stream, write_stream) as client:
            _logger.info("Client session started")
            await client.initialize()
            _logger.info("Client initialized")
            tool_result = await client.list_tools()
            _logger.info(f"Tool result: {tool_result}")
            print(tool_result)
    _logger.info("HTTP test completed")


async def main():
    # await test_websocket()
    await test_http()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    anyio.run(main)
