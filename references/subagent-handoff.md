# Subagent Handoff Protocol & Stage Receipts

Rule: The master conductor (`website-architect`) owns all writes to shared canonical project state.
Subagents are read-heavy workers, run in an isolated fresh context, write ONE structured file to `.arch/handoffs/`, and return a 5-line summary. They never communicate with each other.

## Where to Fork (and Where Not To)

| Stage | Fork? | Why |
|---|---|---|
| Stage 1 / 4: Benchmark Scouting | Yes, 3 parallel (one per candidate) | Breadth-first, independent, context-heavy |
| Stage 3: Asset Sourcing | Yes, isolated worker | Independent operations, noisy tool logs |
| Stage 5.5: Copy & Content | Yes, isolated copywriter | Focused on conversion psychology, independent of code |
| Stage 9: Construction | No (Conductor owns writing) | Tightly coupled edits sharing tokens and components |
| Quality Gate Reviews | Yes, fresh-context reviewer | The builder agent should never grade its own work |

## Handoff Prompt Template

```markdown
ROLE: <benchmark-scout | asset-sourcer | conversion-copywriter | independent-reviewer>
OBJECTIVE: <one measurable sentence>
INPUTS (read-only): .arch/creative_thesis.json, .arch/archetype.json, .arch/content.json
OUTPUT: Write exactly to `.arch/handoffs/<role>-<id>.json` matching `schemas/<name>.schema.json`
TOOLS ALLOWED: <explicit allowlist>. Everything else is forbidden.
BOUNDARIES: Do NOT edit anything under app/, components/, lib/. Do NOT call paid-credit tools.
STOP WHEN: <completion criterion, e.g. 3 candidate references scored, or asset manifest compiled>
RETURN: Maximum 5 lines: path written, top finding, confidence score, open questions, tool errors.
```

## Stage Receipt Protocol (Cryptographic Proof for Gate 2)

Each specialist skill must emit `.arch/receipts/stage-<n>-<skill>.json`:

```json
{
  "stage": 8,
  "skill": "design-system",
  "started": "2026-09-29T10:00:00Z",
  "inputs": {
    "DESIGN.md": "sha256:..."
  },
  "outputs": {
    "src/app/globals.css": "sha256:..."
  },
  "consumed_by": [
    "src/components/sections/Hero.tsx",
    "src/components/sections/Navbar.tsx"
  ]
}
```

`verify_orchestration.py` checks three deterministic invariants:
1. The receipt exists in `.arch/receipts/`.
2. Every output hash still matches the actual file on disk.
3. At least one `consumed_by` file really references the output (e.g. For tokens: greps for `var(--...)` token names).
This proves the skill's output genuinely shaped the application, rather than being an empty invocation in a log.
