from fastmcp import FastMCP
from tools import take_screenshot

mcp = FastMCP("masterclass-demo")


@mcp.tool()
def screenshot():
    """Take a screenshot of the user's screen."""
    return take_screenshot()


if __name__ == "__main__":
    mcp.run()
