from mcp.server import Server
from mcp.server.websocket import websocket_server
from fastapi.routing import APIRouter, WebSocket


def make_mcp_ws_server_router(mcp: Server):
    router = APIRouter()

    @router.websocket("/mcp/ws")
    async def websocket_endpoint(websocket: WebSocket):
        # Auth?
        # TODO: improve the interface for this to just support websocket
        async with websocket_server(
            websocket.scope,
            websocket._receive,
            websocket._send,
        ) as (
            read_stream,
            write_stream,
        ):
            await mcp.run(
                read_stream=read_stream,
                write_stream=write_stream,
                initialization_options=mcp.create_initialization_options(),
            )

    return router
