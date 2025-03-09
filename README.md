# MCP Transport Scratch

This is a repo containing my tinkering with websocket and HTTP based MCP transport.

It contains a simple [MCP server](src/server/mcp_definition.py), that I wire up to [websockets and http](src/server/main.py). Custom transport implementations are in [transport.http](src/transport/http) and [transport.ws](src/transport/ws).

I also have a [test suite](src/client/mcp_client.py) that makes some requests on the MCP server on each transport. To run the suite you need to run some stuff


#### Setup

```bash
uv sync
source ./.venv/bin/activate
export PYTHONPATH=src/
```

#### Server

```bash
uvicorn server.main:app
```

#### Client

```bash
python src/client/mcp_client.py
```
