from fastapi.routing import APIRouter
from mcp import types
from mcp.server import Server
from mcp.shared.memory import (
    create_connected_server_and_client_session as create_session,
)


AllowedClientRequest = (
    types.PingRequest
    # | types.InitializeRequest
    | types.CompleteRequest
    # | types.SetLevelRequest
    | types.GetPromptRequest
    | types.ListPromptsRequest
    | types.ListResourcesRequest
    | types.ListResourceTemplatesRequest
    | types.ReadResourceRequest
    # | types.SubscribeRequest
    # | types.UnsubscribeRequest
    | types.CallToolRequest
    | types.ListToolsRequest
)


class AllowedJSONRPCRequest(types.JSONRPCRequest):
    params: AllowedClientRequest


def make_mcp_http_server_router(mcp_server: Server):
    router = APIRouter()

    @router.post("/mcp/http")
    async def handle_mcp_http(message: AllowedJSONRPCRequest) -> types.ServerResult:

        async with create_session(mcp_server) as session:
            session.initialize()
            result = await session.send_request(message.params, types.ServerResult)

        return result

    return router
