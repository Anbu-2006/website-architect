# Multi-Agent Orchestration, Spatial Fencing & State Collision Prevention

> **Website Architect Reference Standard — Version 2.5.0**  
> *Authoritative Subagent Topology, Finite State Machine Architecture, and Spatial File-System Fencing.*

---

## 1. The Monolithic Context Failure Mode

When an agentic system relies on a single monolithic conversational context to build a full commercial website, it inevitably encounters **context saturation, loss of architectural intent, and regressions toward generic AI templates**:
- Scraped DOM trees, image search results, and brand guidelines quickly consume 60,000+ tokens.
- The model experiences "attention dilution" across hundreds of lines of code.
- As token limits approach, the model takes shortcuts: falling back to 3-card symmetrical grids, ungrounded purple/cyan blur blobs, dummy `#` hash links, and stub components.
- The model is fundamentally incapable of rigorous self-critique when auditing code it just authored in the same context turn.

To guarantee agency-grade commercial execution, `website-architect` decomposes production into **5 specialized autonomous subagents** governed by deterministic lifecycle states, scoped tool privileges, spatial file-system fencing, and signed schema contracts.

---

## 2. The 5-Subagent Finite State Machine Topology

```
┌────────────────────────────────────────────────────────────────────────┐
│                   PARENT ORCHESTRATOR (State Graph & Lock Manager)     │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
    ┌───────────────────────────────┴───────────────────────────────┐
    ▼                                                               ▼
┌──────────────────────────────────────┐        ┌──────────────────────────────────────┐
│  AGENT 1: DEEP INTERNET SCOUT        │        │  AGENT 2: CREATIVE ART DIRECTOR      │
│  - Privilege: Read-Only Primitives   │        │  - Privilege: Read-Only Primitives   │
│  - Crawls Awwwards, Godly, Maps      │        │  - Formulates Visual Thesis          │
│  - Extracts WAAPI, SVGs, AVIF assets │        │  - Typography math & OKLCH palette   │
│  - Emits: assets_manifest.json (v2)  │        │  - Emits: creative_thesis.json       │
└──────────────────┬───────────────────┘        └──────────────────┬───────────────────┘
                   │                                               │
                   └───────────────────────┬───────────────────────┘
                                           │ [Atomic Handoff Gate]
                                           ▼
                       ┌──────────────────────────────────────┐
                       │  AGENT 3: 3D & KINETIC SPECIALIST    │
                       │  - Spatial Fence: src/components/    │
                       │    canvas/ & src/styles/             │
                       │  - R3F Canvas + Draco < 3MB          │
                       │  - Lenis + GSAP ticker engine        │
                       │  - Emits: scene_graph.json           │
                       └──────────────────┬───────────────────┘
                                          │ [Atomic Handoff Gate]
                                          ▼
                       ┌──────────────────────────────────────┐
                       │  AGENT 4: MASTER PRODUCTION BUILDER  │
                       │  - Spatial Fence: src/app/ &         │
                       │    src/components/sections/          │
                       │  - Asymmetric Bento Grid 2.0 (8/4)   │
                       │  - Zero-JS CSS Grid 0fr->1fr         │
                       │  - Live Telemetry Clocks & JSON-LD   │
                       │  - Multi-Page Subpages (>= 4 sects)  │
                       └──────────────────┬───────────────────┘
                                          │ [Atomic Handoff Gate]
                                          ▼
                       ┌──────────────────────────────────────┐
                       │  AGENT 5: FORENSIC QUALITY AUDITOR   │
                       │  - Static AST Gate: 22+ checks       │
                       │  - Playwright Headless Runtime Gate  │
                       │  - Zero Console Errors, CLS < 0.05,  │
                       │    LCP < 1.2s, APCA Lc >= 75         │
                       └──────────────────────────────────────┘
```

---

## 3. Deterministic Pipeline Transition States

| State ID | Trigger Condition | Active Subagent | Permitted Toolset Scope | Exit Verification Requirement |
| :--- | :--- | :--- | :--- | :--- |
| **01: Intake & Discovery** | Project initialization directive received. | **Agent 1: Deep Internet Scout** | `WebSearch`, `FetchDOM`, `ReadLocalFile`, `ExtractTokens` | Validated `assets_manifest.json` and `reference_layout_tree.json`. |
| **02: Aesthetic Formulation** | Successful verification of State 01 artifacts. | **Agent 2: Creative Art Director** | `ReadArtifact`, `EvaluateContrast`, `ParseArchetypeTokens` | Validated `creative_thesis.json` with OKLCH palette & fluid clamping. |
| **03: Kinetic Formulation** | Successful verification of State 02 thesis. | **Agent 3: 3D & Kinetic Specialist** | `ReadThesis`, `SimulateSpring`, `ProfileMeshBudget` | Validated `scene_graph.json` and leak-free `InteractiveSceneCanvas.tsx`. |
| **04: Component Synthesis** | Atomic signing of States 01–03 contracts. | **Agent 4: Master Production Builder** | `WriteScopedFile`, `EditComponent`, `RunLocalCompile` | Clean compile (`tsc --noEmit`) without AST violations; $\ge 4$ subpage sections. |
| **05: Forensic Verification** | Completion of all Builder file write locks. | **Agent 5: Forensic Quality Auditor** | `ReadCodebase`, `ExecuteHeadlessBrowser`, `InspectCDP` | Zero AST violations (22+ rules), $\text{CLS} < 0.05$, $\text{LCP} < 1.2\text{s}$, APCA $L_c \ge 75$. |

---

## 4. State Collision Prevention & Spatial File-System Fencing

To prevent concurrent file mutation collisions and architectural divergence:
1. **Spatial Fencing by Subtree**:
   - `src/components/canvas/`: Mutated exclusively by **Agent 3 (3D & Kinetic Specialist)**.
   - `src/app/` & `src/components/sections/`: Mutated exclusively by **Agent 4 (Master Production Builder)**.
   - `src/styles/` & `globals.css`: Seeded by Art Director / Design System tokens.
   - Discovery agents (Agent 1 & Agent 2) operate with strictly **read-only privileges**.
2. **Lockfile Semaphores (`.lock.agent_id`)**:
   Before modifying any shared configuration (e.g. `package.json` or `tailwind.config.ts`), the orchestrator issues a temporary semaphore lock. Transactions are queued and executed serially.
3. **Cryptographically Signed Schema Contracts**:
   Downstream agents cannot initiate synthesis until upstream JSON schemas (`assets_manifest.schema.json`, `creative_thesis.schema.json`, `scene_graph.schema.json`) pass strict structural validation.
