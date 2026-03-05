# TaskHawk — Audit

## Project Info
| Field | Value |
|-------|-------|
| **DeepSurge ID** | `e3aafb3d-1e7c-45f1-ae9e-7aefa8517dec` |
| **Name** | TaskHawk |
| **Track** | Track 2: Local God Mode |
| **Team** | Mememan (same author as Shield Claw) |
| **GitHub** | https://github.com/mememan-anon/TaskHawk |
| **Website** | https://task-hawk.vercel.app |
| **Demo Video** | https://youtu.be/vfFPYa2QumU (6.5 min) |
| **Package ID** | None |
| **Network** | Testnet (Walrus only) |

## Problem & Solution
- **What is it?** An AI-powered flight search agent — speak in natural language, get real flight prices from Google Flights, and every search is anchored on Walrus for verifiable provenance.
- **What problem does it solve?** Flight search is tedious and results are ephemeral. TaskHawk lets an AI agent parse natural language queries, search multiple sources, and store results on Walrus as a verifiable record.
- **Who has this problem?** Travelers who want natural language flight search. The provenance angle is interesting for agents doing research tasks.
- **Does the solution fit?** The flight search works well. But the Walrus provenance is bolted on — storing flight results on-chain doesn't solve a real pain point for travelers.
- **Would someone use this?** The flight search UI is actually usable. The Walrus part adds minimal practical value.

## Eligibility Checklist
- [x] Submitted to DeepSurge
- [x] Uses at least one Sui Stack component (Walrus)
- [x] Working demo (6.5 min video + live website)
- [ ] Complete DeepSurge profile with wallet address

## Demo Verification
- **Video:** 6.5 min walkthrough. Shows:
  1. VS Code with README and code structure
  2. Live flight search "SFO to JFK under $500" using Google Flights API — real airline prices (Alaska $220, Frontier $225, American $270) ✅
  3. Mock data mode for demo without API key
  4. Walrus aggregator tabs open — blob storage of search results ✅
  5. OpenClaw browser tool integration explained
- **Website:** https://task-hawk.vercel.app — live, clean UI with search bar, data source selector (Live API / Mock), preset routes
- **On-chain:** No Move contract. Walrus blobs stored via testnet publisher/aggregator.

## Code Review Notes
- **Total:** ~5,100 lines JavaScript
- **No Move contracts** — Walrus-only Sui integration
- **Walrus client:** Well-written (280 lines) with retry logic, store/retrieve, task/trace helpers, connectivity test
- **LLM planner:** GPT-based goal parsing and execution planning
- **Flight executor:** SerpApi for real Google Flights pricing + Puppeteer fallback
- **Web UI:** Express server + vanilla HTML/CSS/JS frontend
- **OpenClaw integration:** Browser tool bridge for LLM-driven web automation
- **Well-structured codebase** with clear separation of concerns

## Sui Integration Analysis
- **Walrus** — Store and retrieve flight search results + execution traces. Proper client implementation with retry logic.
- **No Move contracts, no Sui SDK, no on-chain transactions** — purely Walrus storage

## Evaluation Scores
| Criteria | Score (1-10) | Notes |
|----------|:------------:|-------|
| Technical Merit | 6 | Solid 5K-line project with real API integration, LLM planning, browser automation. Well-engineered. But no blockchain logic. |
| Creativity | 5 | Flight search agent is a straightforward application. Walrus provenance is a thin layer. OpenClaw browser tool integration is nice but not novel. |
| Problem-Solution Fit | 4 | The flight search works, but "verifiable provenance for flight results" isn't a real pain point. The Sui integration feels like an afterthought. |
| Sui Integration | 3 | Walrus-only, no Move contracts, no on-chain transactions. Walrus is used as a simple blob store — could be replaced with any storage backend. |

## Overall Assessment
**Below shortlist threshold.** TaskHawk is a competently built flight search agent with a working demo and real API integration. The engineering quality is decent. But the Sui integration is superficial — Walrus is used as a blob store and could be trivially replaced. No Move contracts, no SDK usage, no on-chain logic. The "provenance" angle doesn't address a real user need.

**Shortlist recommendation: No — insufficient Sui integration depth.**
