from mcp.server.fastmcp import FastMCP


mcp = FastMCP()


@mcp.tool("echo", description="Echoes the input")
def echo(data: str):
    return data
