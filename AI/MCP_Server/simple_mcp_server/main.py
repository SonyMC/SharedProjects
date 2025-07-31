"""
FastMCP quickstart example.

cd to the `examples/snippets/clients` directory and run:
    uv run server fastmcp_quickstart stdio
"""
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Demo")


# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> str:
    """Add two numbers"""
    result = a + b
    # Call the dynamic greeting function
    greeting = get_greeting("Tiger")
    # Print the result and greeting
    return f"Result: {result}, {greeting}"


# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Dynamic Greeting"""
    return f"*** Keep Roaring...{name}! ***"

# Ensure the server is available when the module is imported
if __name__ == "__main__":
    mcp.run()