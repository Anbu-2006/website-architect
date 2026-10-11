#!/usr/bin/env python3
"""
MotionSites AI Prompt & Recipe Integration Tool.
Provides real-time search, prompt extraction, and design recipes from MotionSites AI.
Supports both public/free prompts (183+ items) and authenticated access (500+ items).
"""

import sys
import os
import json
import urllib.request
import urllib.parse
from typing import Dict, Any, List, Optional

SUPABASE_URL = "https://xgdzyqfalbibzelpdpvr.supabase.co"
ANON_KEY = (
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9."
    "eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InhnZHp5cWZhbGJpYnplbHBkcHZyIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzE4MzUwMDYsImV4cCI6MjA4NzQxMTAwNn0."
    "u8lH5Y14xx2WxrNEBp8ngkJlijIYHJASq_gOzTaINZY"
)
TOKEN_PATH = os.path.expanduser(
    r"~/.mcp-auth/mcp-remote-v1/6f6b422ac0fd9bcc153d671202420419_tokens.json"
)


def get_auth_token() -> Optional[str]:
    """Check if the user has authenticated via mcp-remote OAuth."""
    if os.path.exists(TOKEN_PATH):
        try:
            with open(TOKEN_PATH, "r", encoding="utf-8") as f:
                data = json.load(f)
                return data.get("access_token")
        except Exception:
            return None
    return None


def search_prompts(
    query: str = "",
    section_type: Optional[str] = None,
    free_only: bool = False,
    limit: int = 15,
) -> List[Dict[str, Any]]:
    """Search MotionSites public prompt catalog."""
    url = f"{SUPABASE_URL}/rest/v1/prompts_public?select=id,title,category,type,is_free,search_keywords"
    
    params = []
    if free_only:
        params.append("is_free=eq.true")
    if section_type and section_type != "all":
        params.append(f"type=eq.{section_type}")
    if query:
        # Supabase ilike on title or search_keywords
        encoded_q = urllib.parse.quote(f"*{query}*")
        params.append(f"or=(title.ilike.{encoded_q},search_keywords.ilike.{encoded_q})")
        
    params.append(f"limit={limit}")
    if params:
        url += "&" + "&".join(params)

    headers = {
        "apikey": ANON_KEY,
        "Authorization": f"Bearer {ANON_KEY}",
        "Content-Type": "application/json",
    }
    
    req = urllib.request.Request(url, headers=headers, method="GET")
    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            return json.loads(response.read().decode("utf-8"))
    except Exception as e:
        print(f"Error searching prompts: {e}", file=sys.stderr)
        return []


def get_prompt_details(prompt_id: str) -> Dict[str, Any]:
    """Retrieve full prompt text, sections, and metadata for a specific prompt ID."""
    url = f"{SUPABASE_URL}/functions/v1/get-prompt"
    payload = json.dumps({"prompt_id": prompt_id}).encode("utf-8")

    token = get_auth_token()
    auth_header = f"Bearer {token}" if token else f"Bearer {ANON_KEY}"

    headers = {
        "apikey": ANON_KEY,
        "Authorization": auth_header,
        "Content-Type": "application/json",
    }

    req = urllib.request.Request(url, data=payload, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=12) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8")
        return {"error": f"HTTP {e.code}: {body}"}
    except Exception as e:
        return {"error": str(e)}


def list_categories() -> List[str]:
    """Fetch distinct categories from MotionSites."""
    url = f"{SUPABASE_URL}/rest/v1/prompts_public?select=category&limit=1000"
    headers = {
        "apikey": ANON_KEY,
        "Authorization": f"Bearer {ANON_KEY}",
    }
    req = urllib.request.Request(url, headers=headers, method="GET")
    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            rows = json.loads(response.read().decode("utf-8"))
            cats = sorted(list(set(r.get("category") for r in rows if r.get("category"))))
            return cats
    except Exception as e:
        print(f"Error fetching categories: {e}", file=sys.stderr)
        return []


def print_help():
    print("""MotionSites AI Prompt & Recipe Tool

Usage:
  python motionsites_prompts.py search "<keyword>" [--type <hero|footer|pricing|features|landing>] [--free-only] [--limit 15]
  python motionsites_prompts.py get "<prompt_id>"
  python motionsites_prompts.py categories
  python motionsites_prompts.py recipes
  python motionsites_prompts.py status
""")


def print_status():
    token = get_auth_token()
    print("=== MotionSites AI MCP Status ===")
    print(f"Endpoint: {SUPABASE_URL}/functions/v1/mcp")
    print(f"Public REST: {SUPABASE_URL}/rest/v1/prompts_public")
    if token:
        print("OAuth Token: Active (Stored in ~/.mcp-auth/mcp-remote-v1/)")
        print("Tier: Authenticated (Access to 500+ prompts & custom recipes)")
    else:
        print("OAuth Token: Unauthenticated (Public / Free mode active)")
        print("Access: 183 free prompts available with zero auth required.")
        print("To authenticate: npx -y mcp-remote https://xgdzyqfalbibzelpdpvr.supabase.co/functions/v1/mcp")


def print_curated_recipes():
    print("""
=============================================================================
MOTIONSITES CURATED DESIGN RECIPES & PROMPT EXAMPLES
=============================================================================

[1] LIQUID GLASS MORPHISM HERO (Bloom AI / Velorah Aesthetic)
-----------------------------------------------------------------------------
Prompt Structure:
- Fullscreen autoplaying, looping, muted video background with object-cover at z-0.
- Strict grayscale typography hierarchy: Poppins font-weight 500 for headings,
  Source Serif 4 italic accents for <em> tags.
- Dual-tier liquid glass surfaces:
  * Tier 1 (Cards): bg-black/40 backdrop-blur-xl border border-white/10 shadow-[0_8px_32px_0_rgba(0,0,0,0.37)]
  * Tier 2 (Pills/CTAs): bg-white/10 hover:bg-white/20 backdrop-blur-md border border-white/20
- Ambient radial highlight overlay: radial-gradient(circle at 50% 0%, rgba(255,255,255,0.08), transparent 70%)

[2] FUTURISTIC NEURAL DARK MODE (Neon Logic / SynapseX Aesthetic)
-----------------------------------------------------------------------------
Prompt Structure:
- Pure dark surface #050505 with subtle scanline / CRT micro-texture.
- Primary font: 'Space Mono' monospace.
- Glowing pill badges with subtle border animation:
  * border: 1px solid rgba(255, 255, 255, 0.12)
  * inner shadow: inset 0 0 12px rgba(255, 255, 255, 0.05)
- Interactive card tilt using motion/react with spring physics (damping: 20, stiffness: 300).

[3] LIQUID GLASS LUXURY FOOTER (Lumina / Vize Aesthetic)
-----------------------------------------------------------------------------
Prompt Structure:
- Asymmetric footer layout with oversized editorial typography.
- Glassmorphic container floating 24px above bottom boundary.
- Social links rendered as frosted glass circular pills with magnetic hover.
- Copyright and status indicator: green pulsing dot (bg-emerald-400 animate-pulse).
- No hard horizontal lines; separation achieved via contrasting subtle glass layers.

[4] INTERACTIVE BENTO GRID WITH LIVE ASSETS (NexaCore / Glow Features)
-----------------------------------------------------------------------------
Prompt Structure:
- 12-column grid with asymmetric spans (col-span-8, col-span-4, col-span-4, col-span-4, col-span-4).
- Hover glow tracker: CSS radial gradient positioned at mouse coordinates via pointermove.
- Micro-interactions: numbers counter on scroll into view via IntersectionObserver.
- Clean vector SVGs only (Lucide React) — zero emojis as structural elements.
=============================================================================
""")


def main():
    if len(sys.argv) < 2:
        print_help()
        sys.exit(0)

    cmd = sys.argv[1].lower()

    if cmd == "status":
        print_status()

    elif cmd == "categories":
        cats = list_categories()
        print(f"Categories ({len(cats)}):")
        for c in cats:
            print(f" - {c}")

    elif cmd == "recipes":
        print_curated_recipes()

    elif cmd == "search":
        query = sys.argv[2] if len(sys.argv) > 2 and not sys.argv[2].startswith("--") else ""
        section_type = None
        free_only = False
        limit = 15

        i = 2
        while i < len(sys.argv):
            arg = sys.argv[i]
            if arg == "--type" and i + 1 < len(sys.argv):
                section_type = sys.argv[i + 1]
                i += 2
            elif arg == "--free-only":
                free_only = True
                i += 1
            elif arg == "--limit" and i + 1 < len(sys.argv):
                limit = int(sys.argv[i + 1])
                i += 2
            else:
                if not query and not arg.startswith("--"):
                    query = arg
                i += 1

        results = search_prompts(query, section_type=section_type, free_only=free_only, limit=limit)
        print(f"Found {len(results)} prompts matching '{query}':")
        for r in results:
            free_tag = "[FREE]" if r.get("is_free") else "[PAID]"
            print(f" {free_tag} {r.get('id')} - {r.get('title')} ({r.get('category')} / {r.get('type')})")
            kw = r.get("search_keywords", "")
            if kw:
                snippet = (kw[:120] + "...") if len(kw) > 120 else kw
                print(f"        {snippet.strip()}")

    elif cmd == "get":
        if len(sys.argv) < 3:
            print("Error: Specify prompt_id. Example: python motionsites_prompts.py get bloom-ai-hero")
            sys.exit(1)
        prompt_id = sys.argv[2]
        res = get_prompt_details(prompt_id)
        if "error" in res:
            print(f"Error: {res['error']}")
        else:
            print(f"=== {prompt_id.upper()} DESIGN PROMPT ===")
            print(res.get("prompt_text") or "(No prompt text returned)")
            if res.get("sections"):
                print("\n--- Sections Breakdown ---")
                for s in res.get("sections", []):
                    print(f"\n### {s.get('name')}")
                    print(s.get("text"))

    else:
        print_help()


if __name__ == "__main__":
    main()
