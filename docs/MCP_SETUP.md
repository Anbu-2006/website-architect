# 🔌 MCP Server Setup & Integration Matrix

Website Architect connects directly with 5 specialized Model Context Protocol (MCP) servers to source verified components, download SVGs, and inspect live browser outputs.

---

## Recommended MCP Servers

| MCP Server | Key Tools | Purpose in Architecture |
| :--- | :--- | :--- |
| **`magicuidesign-mcp`** | `listRegistryItems`, `getRegistryItem` | Curated animated React components (Bento Grids, Shimmer Buttons, Marquees) |
| **`21st-magic`** | `search`, `get_component`, `search_logo` | Real-world brand SVGs, Tailwind hero sections, and design inspirations |
| **`shadcn-ui`** | `get_component`, `list_components` | Accessible UI primitives (Radix UI + Tailwind CSS) |
| **`lucide-icons`** | `search_icons`, `get_icon_usage_examples` | Vector SVG iconography (eliminating emoji icons) |
| **`chrome-devtools-mcp`** | `navigate_page`, `take_screenshot`, `list_console_messages` | In-browser automated validation and console error capture |

---

## Configuration (`mcp_config.json`)

To enable these servers in Antigravity IDE, Claude Code, or Cursor, configure your MCP configuration:

```json
{
  "mcpServers": {
    "magicuidesign-mcp": {
      "command": "npx",
      "args": ["-y", "magicuidesign-mcp@latest"]
    },
    "21st-magic": {
      "command": "npx",
      "args": ["-y", "@21st-dev/magic-mcp@latest"]
    },
    "lucide-icons": {
      "command": "npx",
      "args": ["-y", "lucide-icons-mcp@latest"]
    },
    "chrome-devtools-mcp": {
      "command": "npx",
      "args": ["-y", "chrome-devtools-mcp@latest"]
    }
  }
}
```

---
*Authored by Anbuselvan T. ([@Anbu-2006](https://github.com/Anbu-2006)).*
