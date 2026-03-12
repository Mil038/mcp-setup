# MCP Masterclass Demo

This repository contains a **minimal example of a Model Context Protocol (MCP) server** that can be connected to **Claude Desktop**.

The goal of this project is to demonstrate how:

* An **MCP server exposes tools**
* An **AI client (Claude Desktop) connects to the server**
* Claude can **call tools automatically**

This demo includes a simple tool that lets Claude Desktop take a screenshot of your desktop and save it locally and show it in the chat.

---

# Architecture

```
Claude Desktop (MCP Client)
        │
        │ MCP
        ▼
FastMCP Server (Python)
        │
        ▼
Simple Tool → Take screenshot
```

---

# Repository Structure

```
mcp-setup
│
├── README.md
├── requirements.txt
│
├── app
│   ├── main.py
│   └── tools.py
│
└── claude_desktop_config_example.json
```

---

# Prerequisites

Before starting, make sure you have:

* **Python 3.10+**
* **Claude Desktop installed**

# Step 1 — Clone the Repository & install dependencies
First, clone the repository and go to the correct directory:
```
git clone https://github.com/Mil038/mcp-setup
cd mcp-setup
```
Then install the requirements using the following command:
```
pip install -r requirements.txt
```

# Step 3 — Configure Claude Desktop

Claude Desktop can be downloaded from [here](https://claude.ai/download)

Claude Desktop loads MCP servers from the configuration file. To populate this configuration file, go to `Settings > Developer > Edit Config`. This should open the folder where `claude_desktop_config.json` is located.

Open the configuration file and add the following:

```
{
  "mcpServers": {
    "mcp-setup": {
      "command": "python",
      "args": ["ABSOLUTE_PATH/mcp-setup/app/main.py"]
    }
  }
}
```

Here, `ABSOLUTE_PATH/` is the absolute path to the root of the projects directory. You can use `pwd` in the terminal to retrieve the absolute path.

Important:
* The path **must be an absolute path**
* Claude Desktop will automatically start the MCP server

# Step 4 — Restart Claude Desktop

After saving the configuration:

1. Close Claude Desktop
2. Start Claude Desktop again

Claude will now detect the MCP server automatically.

# Step 5 — Test the MCP Tool

Ask Claude:

```
Take a screenshot of the screen
```

Claude will detect that the MCP server provides a tool and may call:

```
Calling tool: screenshot()
```

Then the tool runs and returns:

```
Screenshot saved to screenshots/screenshot_20260312_194210.png
```

This means Claude successfully called the MCP tool, it should also show it in chat.

# Tool Implementation

The MCP server exposes a single tool:

```
screenshot()
```

This tool takes a screenshot of your desktop and saves it.
