#!/usr/bin/env python3
import os
from fastmcp import FastMCP

mcp = FastMCP("Sample MCP Server")

@mcp.tool(description="Greet a user by name with a welcome message from the MCP server")
def greet(name: str) -> str:
    return f"Hello, {name}! Welcome to our sample MCP server running on Hostinger!"

@mcp.tool(description="Get information about the MCP server including name, version, environment, and Python version")
def get_server_info() -> dict:
    return {
        "server_name": "Sample MCP Server",
        "version": "1.0.0",
        "environment": os.environ.get("ENVIRONMENT", "development"),
        "python_version": os.sys.version.split()[0]
    }

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    host = "0.0.0.0"
    
    print(f"Starting FastMCP server on {host}:{port}")
    
    # Add CORS and headers configuration for Poke compatibility
    mcp.run(
        transport="http",
        host=host,
        port=port,
        stateless_http=True,
        cors=True,  # Enable CORS
        cors_allow_origins=["*"],  # Allow all origins (you can restrict this later)
        cors_allow_methods=["GET", "POST", "OPTIONS"],
        cors_allow_headers=["*"]
    )
