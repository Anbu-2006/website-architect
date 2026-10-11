import os
import re
from pathlib import Path

def run():
    p = Path(r"c:\Users\anbua\.gemini\.agents\skills\website-architect\references\design-systems")
    p_cfg = Path(r"C:\Users\anbua\.gemini\config\skills\website-architect\references\design-systems")
    
    brands = [d.name for d in p.iterdir() if d.is_dir()]
    
    index_lines = [
        "# Curated Production Design Systems Index (74 Brands)",
        "> Standardized DESIGN.md specifications from VoltAgent/awesome-design-md for autonomous web architecture.",
        "",
        "## Quick Navigation by Category",
        "- **Developer Tools & Infra:** Linear, Vercel, Supabase, Raycast, Cursor, Prisma, Clickhouse, Hashicorp, Expo",
        "- **Fintech & Crypto:** Stripe, Coinbase, Kraken, Binance, Revolut, Mastercard",
        "- **Luxury, Automotive & Hardware:** Apple, Porsche, Ferrari, Bugatti, Lamborghini, BMW, BMW-M, HP, IBM, Dell-1996",
        "- **AI & Frontier Tech:** OpenAI, Claude, Mistral, Cohere, ElevenLabs, Palantir",
        "- **Productivity, Design & SaaS:** Notion, Figma, Framer, Airtable, Airbnb, Cal, Intercom, Shopify, Slack, Loom",
        "",
        "## Complete Brand Registry",
        "| Brand | Directory | Spec Link | Aesthetic Focus |",
        "|---|---|---|---|"
    ]

    for b in sorted(brands):
        b_dir = p / b
        spec = "DESIGN.md" if (b_dir / "DESIGN.md").exists() else "README.md"
        desc = "Authentic production brand tokens, palette, and layout rules"
        spec_path = b_dir / spec
        if spec_path.exists():
            try:
                with open(spec_path, "r", encoding="utf-8") as f:
                    content = f.read(1500)
                    m = re.search(r'description:\s*["\']([^"\']+)["\']', content)
                    if m:
                        desc = m.group(1)[:90] + "..."
            except Exception:
                pass
        
        link = f"[{spec}](file:///c:/Users/anbua/.gemini/.agents/skills/website-architect/references/design-systems/{b}/{spec})"
        index_lines.append(f"| **{b.capitalize()}** | `references/design-systems/{b}/` | {link} | {desc} |")

    content = "\n".join(index_lines)

    for target in [p, p_cfg]:
        with open(target / "INDEX.md", "w", encoding="utf-8") as f:
            f.write(content)
            
    print(f"Generated INDEX.md with {len(brands)} brands!")

if __name__ == "__main__":
    run()
