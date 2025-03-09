from mcp.server.fastmcp import FastMCP


mcp = FastMCP()


@mcp.tool("echo_tool", description="Echoes the input")
def echo_tool(data: str):
    return data


@mcp.prompt("test_prompt")
def echo_prompt():
    return "test prompt result"


@mcp.resource(
    uri="test://test_resource",
    name="test_resource",
    description="Test resource",
)
def test_resource():
    return "test resource data!"
