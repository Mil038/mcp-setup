# MCP Masterclass Demo

This repository contains a **minimal example of a Model Context Protocol (MCP) server** that can be connected to **Claude Desktop**.

The goal of this project is to demonstrate how:

* An **MCP server exposes tools**
* An **AI client (Claude Desktop) connects to the server**
* Claude can **call tools automatically**

This demo includes a simple tool that returns a **random quote**.

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
Simple Tool → Random Quote
```

---

# Repository Structure

```
mcp-masterclass-demo
│
├── README.md
├── requirements.txt
│
├── app
│   ├── main.py
│   └── tools.py
│
├── data
│   └── quotes.json
│
└── claude_desktop_config_example.json
```

---

# Prerequisites

Before starting, make sure you have:

* **Python 3.10+**
* **Claude Desktop installed**

Claude Desktop can be downloaded from:

https://claude.ai/download

---

# Step 1 — Clone the Repository

```
git clone https://github.com/YOUR_USERNAME/mcp-masterclass-demo
cd mcp-masterclass-demo
```

---

# Step 2 — Install Dependencies

Install the required Python packages:

```
pip install -r requirements.txt
```

Dependencies:

```
fastmcp
```

---

# Step 3 — Configure Claude Desktop

Claude Desktop loads MCP servers from the configuration file:

## Mac location

```
~/Library/Application Support/Claude/claude_desktop_config.json
```

## Windows location

```
%APPDATA%\Claude\claude_desktop_config.json
```

---

# Step 4 — Add the MCP Server

Open the configuration file and add the following:

```
{
  "mcpServers": {
    "masterclass-demo": {
      "command": "python",
      "args": [
        "/ABSOLUTE/PATH/TO/mcp-masterclass-demo/app/main.py"
      ]
    }
  }
}
```

Example (Mac):

```
{
  "mcpServers": {
    "masterclass-demo": {
      "command": "python",
      "args": [
        "/Users/username/mcp-masterclass-demo/app/main.py"
      ]
    }
  }
}
```

Important:

* The path **must be an absolute path**
* Claude Desktop will automatically start the MCP server

---

# Step 5 — Restart Claude Desktop

After saving the configuration:

1. Close Claude Desktop
2. Start Claude Desktop again

Claude will now detect the MCP server automatically.

---

# Step 6 — Test the MCP Tool

Ask Claude:

```
Give me a random quote
```

Claude will detect that the MCP server provides a tool and may call:

```
random_quote()
```

Example output:

```
"AI is the new electricity."
```

This means Claude successfully called the MCP tool.

---

# Tool Implementation

The MCP server exposes a single tool:

```
random_quote()
```

This tool returns a random quote from a small dataset.

Example dataset:

```
data/quotes.json
```

---

# Running the MCP Server Manually (Optional)

You can also start the MCP server manually for debugging:

```
python app/main.py
```

---

# Learning Goals

With this example you learn:

* How to **create an MCP server**
* How to **expose**
