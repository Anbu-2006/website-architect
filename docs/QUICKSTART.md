# 🚀 Quickstart Guide — Website Architect

This guide gets you up and running with **Website Architect & Master Builder**, whether you are executing scripts directly via terminal or integrating the engine with an autonomous AI coding agent (Antigravity, Claude Code, Cursor).

---

## 1. Environment Setup

### Prerequisites
- Python 3.11+
- Node.js 18+ (for modern frontend scaffolding: Next.js, Vite)
- PowerShell / Bash

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/Anbu-2006/website-architect.git
cd website-architect

# 2. Create and activate a virtual environment
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On Linux/macOS:
source .venv/bin/activate

# 3. Install Python dependencies
pip install -r requirements.txt

# 4. Install Playwright browser binaries (for token extraction)
playwright install chromium
```

---

## 2. Running the Pipeline Step-by-Step

### Step 1: Classify Business & Retrieve Design Archetypes
Analyze a client's business prompt or reference website URL to determine the optimal visual archetype (e.g. Minimalist Editorial, Luxury Dark Tech, Brutalist Swiss, Warm Consumer):

```bash
python scripts/classify_business.py --query "Luxury decentralized finance protocol with high-frequency trading analytics"
```

### Step 2: Extract Live Design Tokens from Benchmarks
Pull authentic typography, color palettes, spacing rhythms, and button styles from live benchmark websites:

```bash
python scripts/extract_tokens.py --url "https://linear.app" --output tokens.json
```

### Step 3: Generate 3 Divergent Section Options
Create interactive 16:9 SVG wireframe previews for a specific page section (e.g., Hero, Bento Grid, Pricing):

```bash
python scripts/section_option_previewer.py --section "hero" --archetype "dark-tech"
```

### Step 4: Run Anti-Slop Forensic Verification
Audit your generated HTML/CSS or React components against 22+ anti-slop rules (bans unexamined purple blobs, uniform 3-card kits, fake stats, and broken anchor tags):

```bash
python scripts/anti_slop_gate.py --target "src/components"
```

### Step 5: Verify Full Architecture Receipts
Verify that all claimed components, icons, and design tokens exist on disk with valid AST contracts:

```bash
python scripts/verify_orchestration.py --project-root "."
```

---

*Maintained by Anbuselvan T. ([@Anbu-2006](https://github.com/Anbu-2006)).*
