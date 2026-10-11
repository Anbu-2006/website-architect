# 🏛️ Universal Website Architect & Master Builder (`/website-architect`)

> **Autonomous Cognitive General Contractor, Multi-Skill Orchestrator & Production Web Building Engine**  
> Designed for Google Antigravity, Claude Code, and Cursor. Converts any business pitch, client brief, or commercial URL into a production-ready, validated web application without generic AI slop, broken anchor links, or unguided monolithic code dumps.

<p align="left">
  <a href="https://github.com/Anbu-2006/website-architect">
    <img src="https://img.shields.io/badge/GitHub-Anbu--2006%2Fwebsite--architect-181717?style=flat&logo=github" alt="GitHub Repo" />
  </a>
  <a href="LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License" />
  </a>
  <img src="https://img.shields.io/badge/Python-3.11%2B-3776AB?style=flat&logo=python" alt="Python" />
  <img src="https://img.shields.io/badge/MCP-5%20Web%20Servers-009688?style=flat" alt="MCP" />
  <img src="https://img.shields.io/badge/Anti--Slop-22%2B%20Forensic%20Checks-10b981?style=flat" alt="Anti-Slop Gate" />
</p>

---

## ⚡ Quick Install (1-Line Terminal Commands)

Install **Website Architect** into your environment with a single terminal command:

### 🪟 Windows (PowerShell)
```powershell
irm https://raw.githubusercontent.com/Anbu-2006/website-architect/main/install.ps1 | iex
```

### 🍎 Linux & macOS (Bash / Zsh)
```bash
curl -fsSL https://raw.githubusercontent.com/Anbu-2006/website-architect/main/install.sh | bash
```

### 🤖 Direct AI Agent Skill Setup (Antigravity & Claude Code)
```bash
# Global Agent Skills (~/.gemini/config/skills/):
git clone https://github.com/Anbu-2006/website-architect.git ~/.gemini/config/skills/website-architect

# Or Active Project Workspace (.agents/skills/):
git clone https://github.com/Anbu-2006/website-architect.git .agents/skills/website-architect
```

### 🐍 Python CLI Package Setup
```bash
git clone https://github.com/Anbu-2006/website-architect.git
cd website-architect
pip install -e .
playwright install chromium
```

---

## Table of Contents

0. [Quick Install (1-Line Terminal Commands)](#-quick-install-1-line-terminal-commands)
1. [Architectural Overview & Core Philosophy](#1-architectural-overview--core-philosophy)
2. [Interconnected UI/UX Design Skills (The Specialist Fleet)](#2-interconnected-uiux-design-skills-the-specialist-fleet)
3. [Interconnected MCP Tools Matrix (The 3 Core Web MCPs)](#3-interconnected-mcp-tools-matrix-the-3-core-web-mcps)
4. [Turnkey MCP Setup & `mcp_config.json`](#4-turnkey-mcp-setup--mcp_configjson)
5. [End-to-End Orchestration (How the Skills & MCPs Work Together)](#5-end-to-end-orchestration-how-the-skills--mcps-work-together)
6. [The Section-by-Section Option Protocol & Zero-Credit Previews](#6-the-section-by-section-option-protocol--zero-credit-previews)
7. [Resilient 3-Tier Sourcing & Machine-Verifiable Receipts](#7-resilient-3-tier-sourcing--machine-verifiable-receipts)
8. [Automated Quality Verification Gates](#8-automated-quality-verification-gates)
9. [Pre-Flight Health Checks & Verification Commands](#9-pre-flight-health-checks--verification-commands)
10. [Directory Structure](#10-directory-structure)

---

## 1. Architectural Overview & Core Philosophy

### The Problem: AI Mode Collapse & "Pretend Orchestration"
Standard AI web generation suffers from two critical flaws:
1. **Distributional Mode Collapse ("AI Slop")**: LLMs trained on millions of generic templates default to a predictable statistical median: dark navy backgrounds (`#0B0F19`), purple/indigo blur blobs, uniform 3-card grids, Inter typography, and hollow marketing prose.
2. **Context Dilution & Pretend Orchestration**: Dumping 10+ general skills into prompt context creates "Lost-in-the-Middle" degradation, where models claim they called tools or downloaded assets, but no files exist on disk.

### The Solution: Master Cognitive General Contractor
`/website-architect` acts as the **Master General Contractor**. Instead of treating all tools equally, it orchestrates a strictly scoped pipeline:
- **Dedicated UI/UX Design Skills**: Provides mathematical design tokens, aesthetic theses (minimalist, brutalist, high-end agency, high-motion GSAP), and anti-slop quality gates.
- **Dedicated Web MCP Servers**: Directly queries component registries (`magicuidesign-mcp`, `21st-magic`) and verifies dev server output in an isolated browser (`chrome-devtools-mcp`).
- **Section-by-Section Option Protocol**: Dissects the page into individual sections, generating 3 divergent options with 16:9 SVG wireframe previews for human selection via `ask_question`.
- **Machine-Verifiable Receipts**: Claims of component installation or brand logo downloads are strictly verified by AST and filesystem checks.

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                   DEDICATED UI/UX & WEB MCP ORCHESTRATION PIPELINE                     │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                        │
│   STAGE 1 & 2: INTAKE & AESTHETIC REASONING                                            │
│   ├── Business Classification & Benchmarks ➔ classify_business.py                      │
│   ├── Anti-Slop Brief Read & Dials         ➔ taste-skill (Brief Read + Dials: 8/6/4)   │
│   └── Human Decision Modals                ➔ ask_question (Native Interactive UI)      │
│                                                                                        │
│   STAGE 3 & 4: DESIGN INTELLIGENCE & TOKEN INGESTION                                   │
│   ├── Live Benchmark Extraction (60fps)    ➔ extract_tokens.py (Playwright Chromium)   │
│   ├── Mathematical Color & Typography      ➔ ui-ux-pro-max (scripts/search.py)         │
│   └── 3-Layer Token Generation             ➔ design-system (Primitive ➔ Semantic)     │
│                                                                                        │
│   STAGE 6 & 7: MULTI-PAGE ROUTING & RESILIENT ASSET SOURCING                           │
│   ├── Multi-Page App Router Crawl          ➔ crawl_sitemap.py                          │
│   ├── Anti-Anchor Illusion AST Gate        ➔ check_no_anchor_illusion.py               │
│   ├── Editorial Photography Sourcing       ➔ harvest_assets.py (--source pinterest)   │
│   └── 3-Tier Sourcing Engine               ➔ resilient_sourcing.py (MCP ➔ CDN ➔ Cache) │
│                                                                                        │
│   STAGE 9: SECTION-BY-SECTION HUMAN-IN-THE-LOOP OPTION LIFECYCLE                       │
│   ├── 3 Divergent Wireframes & HTML Previews ➔ section_option_previewer.py             │
│   ├── Interactive Option Selection Modal   ➔ ask_question (Option A, B, C, Hybrid)    │
│   ├── Aesthetic Archetype Rules            ➔ soft-skill / minimalist-skill / brutalist  │
│   ├── Animated Bento & Shimmer CTAs        ➔ magicuidesign-mcp (getRegistryItem)      │
│   ├── Drop-in Curated React Blocks         ➔ 21st-magic MCP (search & get_component)  │
│   └── Accessible Primitives (Radix UI)     ➔ ui-styling (shadcn/ui + Lucide)           │
│                                                                                        │
│   STAGE 9 FINAL: QUALITY VERIFICATION GATES                                            │
│   ├── Anti-Slop AST & Token Gate           ➔ anti_slop_gate.py                        │
│   ├── Machine Receipt Verifier             ➔ verify_orchestration.py                  │
│   ├── 61-Point Craft Polish                ➔ impeccable (audit, polish, craft-floor)  │
│   └── In-Browser Dev Server Test           ➔ chrome-devtools-mcp (navigate & console)  │
│                                                                                        │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Interconnected UI/UX Design Skills (The Specialist Fleet)

`website-architect` connects specifically with the curated UI/UX design skills brought in to give the AI elite design taste, mathematical token precision, and aesthetic variety:

| Skill Identifier | Physical Path | Primary Role & Archetype Focus | How to Invoke (Command / Tool Contract) |
| :--- | :--- | :--- | :--- |
| **`ui-ux-pro-max`** | `C:\Users\anbua\.gemini\config\skills\ui-ux-pro-max` | **Mathematical Design Intelligence**: 192 product palettes, 74 font pairings, 119 UX guidelines, 22 stack profiles. Guarantees WCAG AA contrast ($\ge 4.5:1$). | `python "C:/Users/anbua/.gemini/config/skills/ui-ux-pro-max/scripts/search.py" "<archetype> <stack>" --design-system` |
| **`taste-skill`** (`design-taste-frontend`) | `C:\Users\anbua\.gemini\config\skills\taste-skill\SKILL.md` | **Anti-Slop Brief Read**: Reads room before coding. Sets 3 dials (`DESIGN_VARIANCE`, `MOTION_INTENSITY`, `VISUAL_DENSITY`) and selects curated design system. | `view_file(AbsolutePath="C:/Users/anbua/.gemini/config/skills/taste-skill/SKILL.md")` |
| **`soft-skill`** (`high-end-visual-design`) | `C:\Users\anbua\.gemini\config\skills\soft-skill\SKILL.md` | **$150k Agency Design**: Luxury, hospitality, and agency craft. Enforces Doppelrand (double-bezel nested borders), button-in-button CTAs, custom spring physics `cubic-bezier(0.32, 0.72, 0, 1)`. | `view_file(AbsolutePath="C:/Users/anbua/.gemini/config/skills/soft-skill/SKILL.md")` |
| **`minimalist-skill`** (`minimalist-ui`) | `C:\Users\anbua\.gemini\config\skills\minimalist-skill\SKILL.md` | **Clean Editorial Minimalism**: Dev tools, B2B SaaS, documentation. Warm bone `#F7F6F3`, desaturated pastels, 1px borders, faux-OS window chrome, `<kbd>` keystrokes. | `view_file(AbsolutePath="C:/Users/anbua/.gemini/config/skills/minimalist-skill/SKILL.md")` |
| **`brutalist-skill`** (`industrial-brutalist-ui`) | `C:\Users\anbua\.gemini\config\skills\brutalist-skill\SKILL.md` | **Industrial Brutalist UI**: Manufacturing, aerospace, robotics. Rigid 0px radius, monolithic uppercase clamp headers, `#F4F4F0` / `#050505` / Aviation Red `#E61919`, ASCII telemetry. | `view_file(AbsolutePath="C:/Users/anbua/.gemini/config/skills/brutalist-skill/SKILL.md")` |
| **`gpt-tasteskill`** (`gpt-taste`) | `C:\Users\anbua\.gemini\config\skills\gpt-tasteskill\SKILL.md` | **Advanced GSAP Motion & Editorial Layout**: 2-line hero iron rule, gapless bento grids (`grid-flow-dense`), GSAP scroll pinning, and text scrubbing (opacity 0.1 $\to$ 1.0). | `view_file(AbsolutePath="C:/Users/anbua/.gemini/config/skills/gpt-tasteskill/SKILL.md")` |
| **`design-system`** | `C:\Users\anbua\.gemini\config\skills\design-system` | **Design Token Architecture**: 3-layer token generation (`Primitive` $\to$ `Semantic` $\to$ `Component`), CSS variable generation and token validation. | `node "C:/Users/anbua/.gemini/config/skills/design-system/scripts/generate-tokens.cjs" --config tokens.json -o tokens.css` |
| **`ui-styling`** | `C:\Users\anbua\.gemini\config\skills\ui-styling\SKILL.md` | **Accessible shadcn/ui & Radix UI**: Component styling, accessible dialogs, drawers, dropdowns, forms, and Tailwind CSS utility classes. | `view_file(AbsolutePath="C:/Users/anbua/.gemini/config/skills/ui-styling/SKILL.md")` |
| **`impeccable`** | `C:\Users\anbua\.gemini\config\skills\impeccable\SKILL.md` | **Craft Polish & Quality Floor**: 61-point craft floor, heuristic scoring (`critique`), technical audit (`audit`), compositor-only GPU animations (`transform`, `opacity`). | `view_file(AbsolutePath="C:/Users/anbua/.gemini/config/skills/impeccable/SKILL.md")` |

---

## 3. Interconnected MCP Tools Matrix (The 7 Free Web Architecture MCPs)

`/website-architect` connects specifically to **seven dedicated, 100% FREE Web & UI/UX Model Context Protocol (MCP) servers** downloaded from npm. Every tool in this fleet is free of charge, requires zero paid subscriptions, and is purpose-built to give the AI elite component sourcing, icon intelligence, browser automation, and architectural planning.

### Overview Matrix

| MCP Server | Download / Registry Source | Pricing / Quota | Primary Capabilities & Tools | Role in Website Architect |
| :--- | :--- | :--- | :--- | :--- |
| **`magicuidesign-mcp`** | npm: `@magicuidesign/mcp@latest`<br>GitHub: [magicuidesign/magicui](https://github.com/magicuidesign/magicui) | **100% FREE**<br>Unmetered | `listRegistryItems`<br>`getRegistryItem`<br>`searchRegistryItems` | Programmatically fetches complete, production-ready React component code for animated Bento Grids, Shimmer Buttons, Marquees, Animated Beams, and Border Beams. |
| **`shadcn-ui`** | npm: `@jpisnice/shadcn-ui-mcp-server@latest`<br>GitHub: [Jpisnice/shadcn-ui-mcp-server](https://github.com/Jpisnice/shadcn-ui-mcp-server) | **100% FREE**<br>Unmetered | `list_components`<br>`get_component`<br>`list_blocks`<br>`get_block` | Authoritative access to all 45+ official shadcn/ui components (dialogs, accordion, forms, sheets, navigation menus, tables) and official blocks without AI hallucination. |
| **`21st-magic`** | npm: `@21st-dev/magic@latest`<br>Platform: [21st.dev](https://21st.dev) | **Free Metadata / Tiered Code**<br>Daily component quota; fallback to open CDN | `search`<br>`get_component`<br>`search_logo`<br>`get_theme` | Community React component discovery, SVGL brand vector logos, and Tailwind themes. Relegated to metadata when quota is reached. |
| **`lucide-icons`** | npm: `lucide-icons-mcp@latest`<br>GitHub: [SeeYangZhi/lucide-icons-mcp](https://github.com/SeeYangZhi/lucide-icons-mcp) | **100% FREE**<br>Unmetered | `search_icons`<br>`get_icon`<br>`list_categories` | Direct searchable registry of 1,500+ Lucide vector icons with tags, categories, and ready-to-use React JSX/SVG code. |
| **`chrome-devtools-mcp`** | npm: `chrome-devtools-mcp@latest`<br>GitHub: [ChromeDevTools/devtools-frontend](https://github.com/ChromeDevTools) | **100% FREE**<br>Local headless Chrome | `list_pages`<br>`navigate_page`<br>`list_console_messages`<br>`take_screenshot`<br>`evaluate_script` | Low-level Chrome DevTools Protocol automation: console errors, layout shift ($CLS < 0.05$), network requests, and visual viewport screenshots. |
| **`playwright-mcp`** | npm: `@playwright/mcp@latest`<br>Docs: [playwright.dev](https://playwright.dev) | **100% FREE**<br>Local open-source | `browser_navigate`<br>`browser_click`<br>`browser_fill`<br>`accessibility_snapshot` | High-level user interaction simulation, accessibility tree validation, end-to-end user flows, and multi-tab automation. |
| **`sequential-thinking`** | npm: `@modelcontextprotocol/server-sequential-thinking@latest`<br>GitHub: [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | **100% FREE**<br>Official Anthropic Reference | `sequentialthinking` | Dynamic multi-step reasoning, hypothesis testing, and architectural planning for complex web blueprints. |

---

### Detailed Setup & Tool Contracts for Each MCP

#### 1. `magicuidesign-mcp` (Animated UI Components)
- **Source**: `@magicuidesign/mcp` on [npm](https://www.npmjs.com/package/@magicuidesign/mcp) | [GitHub](https://github.com/magicuidesign/magicui).
- **Cost**: 100% Free & unmetered. No API key needed.
- **Installation Command**:
  ```bash
  npx -y @magicuidesign/mcp@latest
  ```
- **Configuration in `mcp_config.json`**:
  ```json
  "magicuidesign-mcp": {
    "command": "npx",
    "args": ["-y", "@magicuidesign/mcp@latest"],
    "env": {}
  }
  ```
- **Tool Calling Examples**:
  ```python
  # Search Magic UI registry
  call_mcp_tool(ServerName="magicuidesign-mcp", ToolName="searchRegistryItems", Arguments={"query": "bento-grid", "limit": 5})

  # Retrieve complete component source code
  call_mcp_tool(ServerName="magicuidesign-mcp", ToolName="getRegistryItem", Arguments={"name": "bento-grid", "includeSource": True})
  ```

---

#### 2. `shadcn-ui` (Authoritative Components & Blocks)
- **Source**: `@jpisnice/shadcn-ui-mcp-server` on [npm](https://www.npmjs.com/package/@jpisnice/shadcn-ui-mcp-server) | [GitHub](https://github.com/Jpisnice/shadcn-ui-mcp-server).
- **Cost**: 100% Free & unmetered.
- **Installation Command**:
  ```bash
  npx -y @jpisnice/shadcn-ui-mcp-server@latest
  ```
- **Configuration in `mcp_config.json`**:
  ```json
  "shadcn-ui": {
    "command": "npx",
    "args": ["-y", "@jpisnice/shadcn-ui-mcp-server@latest"],
    "env": {}
  }
  ```
- **Tool Calling Examples**:
  ```python
  # List all available components
  call_mcp_tool(ServerName="shadcn-ui", ToolName="list_components", Arguments={})

  # Fetch button or dialog source code
  call_mcp_tool(ServerName="shadcn-ui", ToolName="get_component", Arguments={"componentName": "dialog"})
  # Fetch pre-built layout block
  call_mcp_tool(ServerName="shadcn-ui", ToolName="get_block", Arguments={"blockName": "dashboard-01", "includeComponents": True})
  ```

---

#### 3. `21st-magic` (Community React Blocks & Brand Logos)
- **Source**: `@21st-dev/magic` on [npm](https://www.npmjs.com/package/@21st-dev/magic) | [Platform](https://21st.dev).
- **Cost**: Free metadata search; component retrieval has daily quotas.
- **API Key**: Free API key from [21st.dev/account/api-keys](https://21st.dev).
- **Installation Command**:
  ```bash
  npx -y @21st-dev/magic@latest API_KEY=YOUR_21ST_API_KEY
  ```
- **Configuration in `mcp_config.json`**:
  ```json
  "21st-magic": {
    "command": "npx",
    "args": ["-y", "@21st-dev/magic@latest", "API_KEY=YOUR_21ST_API_KEY"],
    "env": {
      "TWENTY_FIRST_API_KEY": "YOUR_21ST_API_KEY",
      "API_KEY_21ST": "YOUR_21ST_API_KEY"
    }
  }
  ```
- **Zero-Failure Fallback**: If 21st.dev reaches daily limits or returns empty, `scripts/resilient_sourcing.py` automatically falls back to Simple-Icons CDN (`https://cdn.simpleicons.org/<brand>`) and open SVGL at $0.00.

---

#### 4. `lucide-icons` (Direct Vector Icon Intelligence)
- **Source**: `lucide-icons-mcp` on [npm](https://www.npmjs.com/package/lucide-icons-mcp) | [GitHub](https://github.com/SeeYangZhi/lucide-icons-mcp).
- **Cost**: 100% Free & unmetered.
- **Installation Command**:
  ```bash
  npx -y lucide-icons-mcp@latest --stdio
  ```
- **Configuration in `mcp_config.json`**:
  ```json
  "lucide-icons": {
    "command": "npx",
    "args": ["-y", "lucide-icons-mcp@latest", "--stdio"],
    "env": {}
  }
  ```
- **Tool Calling Examples**:
  ```python
  # Search icons by keyword (e.g. arrow, check, user)
  call_mcp_tool(ServerName="lucide-icons", ToolName="search_icons", Arguments={"query": "arrow-right"})
  # Get React usage examples
  call_mcp_tool(ServerName="lucide-icons", ToolName="get_icon_usage_examples", Arguments={"name": "arrow-right"})
  ```

---

#### 5. `chrome-devtools-mcp` (Low-Level CDP & Browser Diagnostics)
- **Source**: `chrome-devtools-mcp` on [npm](https://www.npmjs.com/package/chrome-devtools-mcp) | [GitHub](https://github.com/ChromeDevTools/devtools-frontend).
- **Cost**: 100% Free local headless Chrome automation.
- **Prerequisite**: Google Chrome or Chromium installed on host OS.
- **Installation Command**:
  ```bash
  npx -y chrome-devtools-mcp@latest --channel=stable --headless=false
  ```
- **Configuration in `mcp_config.json`**:
  ```json
  "chrome-devtools-mcp": {
    "command": "npx",
    "args": [
      "-y",
      "chrome-devtools-mcp@latest",
      "--channel=stable",
      "--headless=false",
      "--memoryDebugging=true",
      "--allowUnrestrictedPaths=true"
    ],
    "env": {}
  }
  ```
- **Tool Calling Examples**:
  ```python
  # Navigate to dev server
  call_mcp_tool(ServerName="chrome-devtools-mcp", ToolName="navigate_page", Arguments={"pageId": 1, "url": "http://localhost:3000"})

  # Check for runtime console errors
  call_mcp_tool(ServerName="chrome-devtools-mcp", ToolName="list_console_messages", Arguments={"pageId": 1})

  # Capture screenshot
  call_mcp_tool(ServerName="chrome-devtools-mcp", ToolName="take_screenshot", Arguments={"pageId": 1, "format": "png"})
  ```

---

#### 6. `playwright-mcp` (High-Level User Flow & Accessibility Testing)
- **Source**: `@playwright/mcp` on [npm](https://www.npmjs.com/package/@playwright/mcp) | [Docs](https://playwright.dev).
- **Cost**: 100% Free local open-source.
- **Installation Command**:
  ```bash
  npx -y @playwright/mcp@latest
  ```
- **Configuration in `mcp_config.json`**:
  ```json
  "playwright-mcp": {
    "command": "npx",
    "args": ["-y", "@playwright/mcp@latest"],
    "env": {}
  }
  ```
- **Tool Calling Examples**:
  ```python
  # Navigate and capture accessibility snapshot
  call_mcp_tool(ServerName="playwright-mcp", ToolName="browser_navigate", Arguments={"url": "http://localhost:3000"})
  call_mcp_tool(ServerName="playwright-mcp", ToolName="accessibility_snapshot", Arguments={})
  ```

---

#### 7. `sequential-thinking` (Architectural Reasoning & Planning)
- **Source**: `@modelcontextprotocol/server-sequential-thinking` on [npm](https://www.npmjs.com/package/@modelcontextprotocol/server-sequential-thinking) | [GitHub](https://github.com/modelcontextprotocol/servers).
- **Cost**: 100% Free reference server from Anthropic.
- **Installation Command**:
  ```bash
  npx -y @modelcontextprotocol/server-sequential-thinking@latest
  ```
- **Configuration in `mcp_config.json`**:
  ```json
  "sequential-thinking": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-sequential-thinking@latest"],
    "env": {}
  }
  ```
- **Tool Calling Examples**:
  ```python
  # Plan multi-step architectural decision
  call_mcp_tool(
      ServerName="sequential-thinking",
      ToolName="sequentialthinking",
      Arguments={
          "thought": "Evaluating section divergence for Hero: Option A (full-bleed video) vs Option B (60/40 split with arched mask)",
          "thoughtNumber": 1,
          "totalThoughts": 3,
          "nextThoughtNeeded": True
      }
  )
  ```

---

## 4. Turnkey MCP Setup & Complete `mcp_config.json`

To enable the complete 7-server web architect toolchain in any environment, ensure your `mcp_config.json` (located at `~/.gemini/config/mcp_config.json` or your workspace settings) includes these servers:

```json
{
  "mcpServers": {
    "magicuidesign-mcp": {
      "command": "npx",
      "args": ["-y", "@magicuidesign/mcp@latest"],
      "env": {}
    },
    "shadcn-ui": {
      "command": "npx",
      "args": ["-y", "@jpisnice/shadcn-ui-mcp-server@latest"],
      "env": {}
    },
    "21st-magic": {
      "command": "npx",
      "args": [
        "-y",
        "@21st-dev/magic@latest",
        "API_KEY=YOUR_21ST_API_KEY"
      ],
      "env": {
        "TWENTY_FIRST_API_KEY": "YOUR_21ST_API_KEY",
        "API_KEY_21ST": "YOUR_21ST_API_KEY"
      }
    },
    "lucide-icons": {
      "command": "npx",
      "args": ["-y", "lucide-icons-mcp@latest"],
      "env": {}
    },
    "chrome-devtools-mcp": {
      "command": "npx",
      "args": [
        "-y",
        "chrome-devtools-mcp@latest",
        "--channel=stable",
        "--headless=false",
        "--memoryDebugging=true",
        "--allowUnrestrictedPaths=true"
      ],
      "env": {}
    },
    "playwright-mcp": {
      "command": "npx",
      "args": ["-y", "@playwright/mcp@latest"],
      "env": {}
    },
    "sequential-thinking": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-sequential-thinking@latest"],
      "env": {}
    }
  }
}
```

### System Prerequisites
- **Node.js**: v18+ or v20+ with `npm` and `npx`.
- **Python**: v3.10+ with `playwright` and `beautifulsoup4`:
  ```bash
  pip install playwright beautifulsoup4
  python -m playwright install chromium
  ```

---

## 5. End-to-End Orchestration (How the Skills & MCPs Work Together)

When an AI agent executes `/website-architect`, it collaborates across the skills and MCP tools in this exact sequence:

```
[User Prompt / Brief / Maps URL]
                │
                ▼
      classify_business.py
  (Identifies Archetype & ADS Score)
                │
                ▼
           taste-skill
  (Design Read 0.B & Dial Settings)
                │
                ▼
       sequential-thinking
  (Multi-Step Architectural Hypothesis)
                │
                ▼
         ui-ux-pro-max
  (Mathematical Color & Font Tokens)
                │
                ▼
       extract_tokens.py
  (Headless 60fps Playwright Extraction)
                │
                ▼
        design-system
  (3-Layer Primitive ➔ Semantic Tokens)
                │
                ▼
       harvest_assets.py
  (Zero-Credit Photos from Maps/Pinterest)
                │
                ▼
         PRD & Blueprint
  (Halts for User Confirmation via ask_question)
                │
                ▼
┌────────────────────────────────────────────────────────┐
│ SECTION-BY-SECTION HUMAN-IN-THE-LOOP OPTION LIFECYCLE  │
│                                                        │
│  1. section_option_previewer.py                        │
│     ➔ Produces 3 divergent options with 16:9 SVGs      │
│  2. ask_question                                       │
│     ➔ User selects Option A, B, C, or Custom Hybrid    │
│  3. Component & Icon Sourcing:                         │
│     ➔ shadcn-ui MCP / magicuidesign-mcp / 21st-magic   │
│     ➔ lucide-icons MCP for vector symbols              │
│     ➔ resilient_sourcing.py for verified brand SVGs    │
│  4. Author Section Code                                │
│     ➔ Applies soft-skill / minimalist / brutalist      │
│  5. anti_slop_gate.py                                  │
│     ➔ Audits section AST before moving to next section │
└────────────────────────────────────────────────────────┘
                │
                ▼
┌────────────────────────────────────────────────────────┐
│ FINAL QUALITY VERIFICATION GATES                       │
│                                                        │
│  1. verify_orchestration.py                            │
│     ➔ Confirms claimed MCP files physically exist      │
│  2. check_no_anchor_illusion.py                        │
│     ➔ Blocks fake # anchor hashes                      │
│  3. anti_slop_gate.py                                  │
│     ➔ Verifies whole project has zero AI slop          │
│  4. In-Browser Verification:                           │
│     ➔ chrome-devtools-mcp (console errors & CLS)       │
│     ➔ playwright-mcp (accessibility tree & user flow)  │
└────────────────────────────────────────────────────────┘
```

---

## 6. The Section-by-Section Option Protocol & Zero-Credit Previews

Monolithic single-prompt website generation is the #1 cause of user dissatisfaction and AI failure. `website-architect` enforces the **Section-by-Section Option Protocol**:

### The 7-Axis Divergence Contract
For every section (Hero, Features, Social Proof, Conversion, Footer), `section_option_previewer.py` generates exactly 3 structurally divergent options differing across **at least 3 of these 7 axes**:
1. **Composition Structure**: (e.g. Asymmetric 60/40 split vs. Centered monolithic vs. Interlocking Bento).
2. **Visual Density**: (Generous 96px whitespace vs. High-density data grid).
3. **Primary Media Treatment**: (Full-bleed ambient video loop vs. Curved arched photo mask vs. Interactive UI telemetry).
4. **Reading Direction**: (Z-pattern editorial scan vs. Left-pinned index list vs. Staggered card stream).
5. **Primary Interaction Mechanism**: (GSAP scroll scrub reveal vs. Hover elevation card vs. Tabbed state switcher).
6. **Typography Role**: (Oversized clamp display serif vs. Clean technical monospace vs. Sans-serif utility).
7. **Rhythm & Edge Treatment**: (Border-radius 24px Doppelrand vs. 0px rigid brutalist vs. 1px hairline flat minimal).

### Zero-Credit Programmatic SVG Wireframes
Generated by `scripts/section_option_previewer.py`, these wireframes use 16:9 aspect ratios, token colors, and structural layout zones. **They cost zero external image generation credits**, providing instant visual grounding in the chat modal.

---

## 7. Resilient 3-Tier Sourcing & Machine-Verifiable Receipts

To eliminate "pretend orchestration" (where an AI claims it downloaded a logo or imported a component, but the file doesn't exist), `website-architect` uses `scripts/resilient_sourcing.py`:

```
Tier 1: MCP Tool Query
  ├── Magic UI (@magicuidesign/mcp) ➔ getRegistryItem
  ├── Shadcn UI (@jpisnice/shadcn-ui-mcp-server) ➔ get_component
  ├── Lucide Icons (lucide-icons-mcp) ➔ get_icon
  └── 21st.dev (@21st-dev/magic)    ➔ search_logo / get_component
          │ (If timeout, rate-limited, or empty)
          ▼
Tier 2: Direct CDN & Public API ($0.00)
  ├── Simple-Icons CDN ➔ https://cdn.simpleicons.org/<brand>
  └── SVGL Open API    ➔ https://api.svgl.app/
          │ (If network offline or missing brand)
          ▼
Tier 3: Bundled Cache & Programmatic Generator
  └── Local SVG generator creates crisp, branded vector badges on disk
```

### Verification
Run `python skills/website-architect/scripts/verify_orchestration.py <project_dir>`:
- Verifies physical presence of claimed Magic UI / Shadcn components in `src/components/ui/`.
- Verifies physical presence of brand SVGs in `public/logos/`.
- Verifies `package.json` contains declared dependencies (`lucide-react`, `motion`, `clsx`, `tailwind-merge`).

---

## 8. Automated Quality Verification Gates

Before presenting any final code to the user, the agent runs automated gates:

### 1. `anti_slop_gate.py` (AST Checker)
Scans all TSX/JSX files for AI anti-patterns:
- **Repetitive 3-card kits**: Flags pages where $>40\%$ of sections use uniform 3-card grids.
- **Structural emojis**: Flags emojis used as icons (e.g. `<span>🚀</span>`); enforces SVG icons (Lucide).
- **Raw hex colors**: Flags inline hex codes; enforces semantic CSS variables and Tailwind tokens.
- **Generic marketing prose**: Flags ungrounded filler words ("seamlessly", "cutting-edge", "game-changer").

### 2. `check_no_anchor_illusion.py` (MPA Route Validator)
Ensures navigation links use real Next.js `<Link href="/subpage">` routes instead of fake anchor hashes (`href="#services"`).

### 3. `chrome-devtools-mcp` & `playwright-mcp` (In-Browser Live Audits)
- Navigates to `http://localhost:3000`.
- Verifies zero unhandled React runtime errors in console.
- Verifies zero layout shifts ($CLS < 0.05$).
- Captures accessibility tree snapshots and responsive screenshots for visual verification.

---

## 9. Pre-Flight Health Checks & Verification Commands

Test all scripts and integrations directly from the terminal:

```bash
# 1. Test Business Classifier & Live Benchmarks
python scripts/classify_business.py --pitch "Artisanal Japanese matcha cafe in Kyoto with table reservations and online tea club"

# 2. Test 3-Tier Resilient Sourcing (Brand SVGs & Magic UI components)
python scripts/resilient_sourcing.py --target "./demo" --brand "stripe" --brand "github" --brand "google"

# 3. Test Zero-Credit Section Option Previewer (Generates 3 divergent SVG options)
python scripts/section_option_previewer.py --section hero --output "./demo/hero_options.html"

# 4. Test Anti-Slop AST Gate on Project Codebase
python scripts/anti_slop_gate.py ./src

# 5. Test Orchestration & Component Receipt Verifier
python scripts/verify_orchestration.py .

# 6. Test Multi-Page App Router Anchor Validator
python scripts/check_no_anchor_illusion.py ./src/app
```

---

## 10. Directory Structure

```text
website-architect/
├── SKILL.md                                        # Master 9-stage cognitive engine orchestrator
├── README.md                                       # Comprehensive setup, skill & MCP orchestration guide
├── pyproject.toml                                  # Python build system & package metadata
├── requirements.txt                                # Python runtime dependencies
├── metadata.json                                   # Skill registration manifest
├── LICENSE                                         # MIT License
├── docs/
│   ├── QUICKSTART.md                               # Step-by-step developer tutorial
│   ├── AI_AGENT_INSTRUCTIONS.md                    # 9-stage operational playbook for AI agents
│   └── MCP_SETUP.md                                # MCP server connection matrix & configs
├── scripts/
│   ├── classify_business.py                        # Autonomous archetype, ADS score & live benchmark inference
│   ├── section_option_previewer.py                 # Zero-credit 16:9 SVG wireframe & divergent option generator
│   ├── anti_slop_gate.py                           # AST checker blocking AI slop, emojis, and unvaried card kits
│   ├── verify_orchestration.py                     # Machine receipt verifier eliminating pretend orchestration
│   ├── resilient_sourcing.py                       # 3-tier fallback engine (MCP -> Direct CDN -> Offline cache)
│   ├── extract_tokens.py                           # 60fps GPU-accelerated Playwright token & motion extractor
│   ├── crawl_sitemap.py                            # Multi-page recursive route & navigation crawler
│   ├── check_no_anchor_illusion.py                 # AST & regex validator blocking fake anchor hashes
│   ├── video_to_wireframe.py                       # Video recording decomposition & wireframe extractor
│   ├── layout_fidelity_score.py                    # Visual & DOM fidelity verification gate
│   └── harvest_assets.py                           # Multi-archetype Pinterest & Google Maps media harvester
├── references/
│   ├── multi-skill-and-mcp-orchestration-matrix.md # Full-stack orchestration of UI skills & MCP tools
│   ├── section-by-section-option-protocol.md       # Divergence contract, preview ladder & state machine
│   ├── tech-stack-and-gui-guide.md                 # Universal omnipotent Next.js 15 stack standard & runtime guide
│   ├── benchmark-references-and-anti-slop-guide.md # 15 Greppable Negative Guardrails & benchmark catalog
│   ├── intelligent-design-reasoning-engine.md      # 6-dimension aesthetic thesis formulation
│   ├── page-and-feature-distribution-matrix.md     # Authoritative page-by-page breakdown & section anatomy
│   ├── universal-archetypes-reference.md           # Universal commercial archetypes & sub-types
│   ├── intake-protocol-and-decision-trees.md       # Autonomous discovery & friction-free decision flow
│   ├── enterprise-prd-template.md                  # Authoritative PRD specification blueprint
│   ├── web-interface-guidelines.md                 # Vercel Web Interface Guidelines & a11y standards
│   └── category-assets-reference.md                # Category-specific visual asset & media standards
└── evals/
    └── evals.json                                  # Comprehensive benchmark evaluation suite
```

---

## 👤 Maintainer & Lead Architect

- **Anbuselvan T.** ([@Anbu-2006](https://github.com/Anbu-2006)) — Lead Full-Stack Architect & AI Systems Engineer
- **GitHub Repository**: [https://github.com/Anbu-2006/website-architect](https://github.com/Anbu-2006/website-architect)
- **Portfolio**: [anbudev.me](https://anbudev.me)

---

## 📄 License

Released under the [MIT License](LICENSE). Copyright &copy; 2026 Anbuselvan T. All Rights Reserved.
