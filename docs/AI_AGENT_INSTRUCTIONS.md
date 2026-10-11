# 🤖 AI Agent Operational Playbook

This document specifies the exact execution lifecycle for autonomous AI coding agents (Antigravity IDE, Claude Code, Cursor, Codex) utilizing `/website-architect`.

---

## 🧭 The 9-Stage Execution Lifecycle

When a user requests a website or landing page build, DO NOT immediately output JSX or HTML files. Follow these 9 sequential stages:

```
[Stage 1: Intake & Discovery]
       │
       ▼
[Stage 2: Aesthetic Reasoning & Archetype Selection]
       │
       ▼
[Stage 3: Design Intelligence & Mathematical Tokens]
       │
       ▼
[Stage 4: Token Ingestion & Tailwind @theme Setup]
       │
       ▼
[Stage 5: Scaffolding & Component Matrix]
       │
       ▼
[Stage 6: Multi-Page Routing & Information Architecture]
       │
       ▼
[Stage 7: Resilient 3-Tier Asset Sourcing]
       │
       ▼
[Stage 8: Section-by-Section Option Protocol]
       │
       ▼
[Stage 9: Quality Verification & Anti-Slop Audit]
```

---

## 📋 Stage Breakdown & Rule Enforcement

### Stage 1: Intake & Discovery
- Identify the target industry, key user personas, conversion goals, and brand voice.
- Check if user supplied reference URLs, brand assets, or logos.

### Stage 2: Aesthetic Reasoning
- Formulate an intentional visual thesis.
- Present 3 divergent directions to the user (e.g. Minimalist Editorial, Tactile/Expressive, Kinetic/Spatial).
- **CRITICAL ANTI-SLOP RULE**: Ban generic AI defaults:
  - ❌ NO dark navy `#0B0F19` backgrounds with purple gradient blur blobs (`#7C3AED`).
  - ❌ NO uniform 3-card feature grids with identical height and emoji icons.
  - ❌ NO generic marketing jargon ("Revolutionize", "Supercharge your workflow", "Unlock power").

### Stage 3 & 4: Design Tokens & Layout Architecture
- Define tokens using a strict 3-layer architecture:
  - Primitive Tokens (raw hex, rem scales)
  - Semantic Tokens (`--bg-surface`, `--text-primary`, `--border-subtle`)
  - Component Tokens (`--card-padding`, `--btn-radius`)
- Enforce 8dp/4dp spatial scale. Zero magic numbers in component styling.

### Stage 7: Surgical Asset Sourcing
- Use the 3-Tier Sourcing protocol:
  - Tier 1: User-supplied assets in workspace.
  - Tier 2: Free stock CDNs (Unsplash, Pexels) with verified dimensions.
  - Tier 3: Native generative image tools (`generate_image`) with explicit aspect ratios.
- **Rule**: Never leave broken placeholders (`placeholder.com` or `src="#"`).

### Stage 8: Section-by-Section Human Option Protocol
- Never build the entire website in a single monolithic response.
- Build section by section (Header/Hero, Social Proof, Bento Feature Grid, Interactive Demo, Pricing, Footer).
- Propose layout variations before committing to final code.

### Stage 9: Verification Gates
- Execute `anti_slop_gate.py` to assert zero layout violations.
- Verify dev server in browser (`npm run dev`) with zero console errors.

---
*Authored by Anbuselvan T. ([@Anbu-2006](https://github.com/Anbu-2006)).*
