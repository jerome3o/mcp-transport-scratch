from mcp.server.websocket import websocket_server_transport
from fastapi import FastAPI, WebSocket

from server.mcp_server import mcp

app = FastAPI()


@app.websocket("/mcp/ws")
async def websocket_endpoint(websocket: WebSocket):
    # Auth?
    async with websocket_server_transport(websocket) as (read_stream, write_stream):
        await mcp._mcp_server.run(
            read_stream=read_stream,
            write_stream=write_stream,
            initialization_options=mcp._mcp_server.create_initialization_options(),
        )
