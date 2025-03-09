import logging

from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from server.mcp_definition import mcp
from transport.http.server import make_mcp_http_server_router
from transport.ws.server import make_mcp_ws_server_router

http_router = make_mcp_http_server_router(mcp._mcp_server)
ws_router = make_mcp_ws_server_router(mcp._mcp_server)

app = FastAPI()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    exc_str = f"{exc}".replace("\n", " ").replace("   ", " ")
    logging.error(f"{request}: {exc_str}")
    content = {
        "status_code": 10422,
        "message": exc_str,
        "data": None,
    }
    return JSONResponse(
        content=content,
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
    )


app.include_router(http_router)
app.include_router(ws_router)
