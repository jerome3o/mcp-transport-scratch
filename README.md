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


## Example output

```log
Starting in-memory client test
Client session started
Client initialized
Tool result: meta=None nextCursor=None tools=[Tool(name='echo_tool', description='Echoes the input', inputSchema={'properties': {'data': {'title': 'Data', 'type': 'string'}}, 'required': ['data'], 'title': 'echo_toolArguments', 'type': 'object'})]
Prompts result: meta=None nextCursor=None prompts=[Prompt(name='test_prompt', description='', arguments=[])]
Resources result: meta=None nextCursor=None resources=[Resource(uri=AnyUrl('test://test_resource'), name='test_resource', description='Test resource', mimeType='text/plain', size=None, annotations=None)]
Call tool result: meta=None content=[TextContent(type='text', text='Hello, world!', annotations=None)] isError=False
Call prompt result: meta=None description=None messages=[PromptMessage(role='user', content=TextContent(type='text', text='test prompt result', annotations=None))]
Read resource result: meta=None contents=[TextResourceContents(uri=AnyUrl('test://test_resource'), mimeType='text/plain', text='test resource data!')]
Memory test completed

Starting websocket client test
Connected to websocket
Client session started
Client initialized
Tool result: meta=None nextCursor=None tools=[Tool(name='echo_tool', description='Echoes the input', inputSchema={'properties': {'data': {'title': 'Data', 'type': 'string'}}, 'required': ['data'], 'title': 'echo_toolArguments', 'type': 'object'})]
Prompts result: meta=None nextCursor=None prompts=[Prompt(name='test_prompt', description='', arguments=[])]
Resources result: meta=None nextCursor=None resources=[Resource(uri=AnyUrl('test://test_resource'), name='test_resource', description='Test resource', mimeType='text/plain', size=None, annotations=None)]
Call tool result: meta=None content=[TextContent(type='text', text='Hello, world!', annotations=None)] isError=False
Call prompt result: meta=None description=None messages=[PromptMessage(role='user', content=TextContent(type='text', text='test prompt result', annotations=None))]
Read resource result: meta=None contents=[TextResourceContents(uri=AnyUrl('test://test_resource'), mimeType='text/plain', text='test resource data!')]
Websocket test completed

Starting HTTP client test
Connected to HTTP
Client session started
Client initialized
HTTP Request: POST http://127.0.0.1:8000/mcp/http "HTTP/1.1 200 OK"
Tool result: meta=None nextCursor=None tools=[Tool(name='echo_tool', description='Echoes the input', inputSchema={'properties': {'data': {'title': 'Data', 'type': 'string'}}, 'required': ['data'], 'title': 'echo_toolArguments', 'type': 'object'})] meta=None
HTTP Request: POST http://127.0.0.1:8000/mcp/http "HTTP/1.1 200 OK"
Prompts result: meta=None nextCursor=None prompts=[Prompt(name='test_prompt', description='', arguments=[])] meta=None
HTTP Request: POST http://127.0.0.1:8000/mcp/http "HTTP/1.1 200 OK"
Resources result: meta=None nextCursor=None resources=[Resource(uri=AnyUrl('test://test_resource'), name='test_resource', description='Test resource', mimeType='text/plain', size=None, annotations=None)] meta=None
HTTP Request: POST http://127.0.0.1:8000/mcp/http "HTTP/1.1 200 OK"
Call tool result: meta=None content=[TextContent(type='text', text='Hello, world!', annotations=None)] isError=False meta=None
HTTP Request: POST http://127.0.0.1:8000/mcp/http "HTTP/1.1 200 OK"
Call prompt result: meta=None description=None messages=[PromptMessage(role='user', content=TextContent(type='text', text='test prompt result', annotations=None))] meta=None
HTTP Request: POST http://127.0.0.1:8000/mcp/http "HTTP/1.1 200 OK"
Read resource result: meta=None contents=[TextResourceContents(uri=AnyUrl('test://test_resource'), mimeType='text/plain', text='test resource data!')] meta=None
HTTP test completed
```