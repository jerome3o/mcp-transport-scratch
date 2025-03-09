from mcp.server import Server
from mcp.server.websocket import websocket_server_transport
from fastapi.routing import APIRouter, WebSocket


def make_mcp_ws_server_router(mcp: Server):
    router = APIRouter()

    @router.websocket("/mcp/ws")
    async def websocket_endpoint(websocket: WebSocket):
        # Auth?
        async with websocket_server_transport(websocket) as (read_stream, write_stream):
            await mcp.run(
                read_stream=read_stream,
                write_stream=write_stream,
                initialization_options=mcp.create_initialization_options(),
            )

    return router
