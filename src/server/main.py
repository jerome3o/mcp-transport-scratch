from fastapi import FastAPI

from server.mcp_definition import mcp
from transport.ws.server import make_mcp_ws_server_router
from transport.http.server import make_mcp_http_server_router

http_router = make_mcp_http_server_router(mcp)
ws_router = make_mcp_ws_server_router(mcp)

app = FastAPI()

app.include_router(http_router)
app.include_router(ws_router)
