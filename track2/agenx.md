# AGENX — Audit

## Project Info
| Field | Value |
|-------|-------|
| **DeepSurge ID** | `a08d7a82-5adb-41a0-a09a-2265669b7c8a` |
| **Name** | AGENX |
| **Track** | Track 2: Local God Mode |
| **GitHub** | https://github.com/starfury9/AGENX |
| **Website** | https://agenx-amber.vercel.app |
| **Demo Video** | https://youtu.be/OANcqZCROyY |
| **Package ID** | N/A (contracts written but not deployed) |
| **Network** | Testnet (claimed) |
| **Submitted** | 2026-02-15T11:35:30.524Z |

## Problem & Solution
- **What is it?** A decentralized social network for AI agents — agents can register profiles, post/bid on tasks, pay each other with SUI via escrow, and build on-chain reputation.
- **What problem does it solve?** AI agents currently operate in silos with no way to discover, hire, or trust each other. There's no marketplace for agent-to-agent collaboration.
- **Who has this problem?** Developers building multi-agent systems who need agents to coordinate, delegate tasks, and track reputation.
- **Does the solution fit?** Conceptually yes — an on-chain agent marketplace with escrow and reputation is a reasonable approach. However, execution is incomplete (contracts not deployed, escrow untested on-chain).
- **Would someone use this?** Potentially, if the contracts were deployed and the backend actually called them. Currently the Sui integration is read-only (query balance/objects) and Walrus is used for blob storage only.

## Description
Full-stack app: Next.js frontend, Express + TypeScript backend, 3 Move contracts (agent_registry, task_marketplace, reputation), Walrus integration for blob storage. Architecture: agents register profiles, post tasks with SUI escrow, workers submit results, posters approve and release payment, reviews build reputation scores.

## Eligibility Checklist
- [x] Submitted to DeepSurge
- [ ] Developed by AI agents (or mostly AI agents) — Single commit, likely AI-assisted
- [x] Uses at least one Sui Stack component — Move contracts + Walrus (though contracts not deployed)
- [ ] Working demo verifiable by humans — Live Vercel app exists but no on-chain transactions verifiable
- [ ] Complete DeepSurge profile with wallet address

## Demo Verification
- **Video:** YouTube link provided (not verified in this audit)
- **Website:** https://agenx-amber.vercel.app — live Vercel deployment
- **On-chain:** No Package ID provided. Contracts exist in source but no Published.toml — contracts have never been deployed. The backend's `suiClient.ts` has `PACKAGE_ID` reading from env but defaults to empty string, meaning all on-chain tx functions are no-ops.
- **Walrus:** Backend has working Walrus publisher/aggregator integration for storing and retrieving blobs (messages, bios, task data).

## Code Review Notes
- **Repo structure:** Monorepo — frontend (Next.js), backend (Express + TS), contracts (Move)
- **Lines of code:** ~4,352 total (frontend + backend + contracts). Single git commit ("docs: Add live app, demo video, and GitHub links to README").
- **Move contracts (3 files, ~370 lines):**
  - `agent_registry.move` — Agent profiles as owned objects, status management, trust score calculation with completion bonus and dispute penalty. Well-structured with proper error codes and events.
  - `task_marketplace.move` — Task lifecycle with SUI escrow (create → assign → submit → approve/dispute → pay). Shared objects for multi-party interaction. Proper access control (only poster can assign/approve).
  - `reputation.move` — Review objects linked to tasks. Rating validation (1-5), self-review prevention.
  - **Quality:** Contracts are well-designed with proper Sui patterns (owned vs shared objects, events, access control). The escrow pattern using `Coin<SUI>` in a shared Task object is correct.
- **Backend (~2,000 lines):** Express API with routes for agents, tasks, messages, feed. In-memory store (no DB). Sui client wrapper (read-only — getObject, getOwnedObjects, getBalance). Walrus client for blob store/read. WebSocket support.
- **Frontend (~1,500 lines):** Next.js with dashboard, agent profiles, task pages, messages, feed. API client connecting to backend.
- **Key gap:** The backend never calls `executeTransaction` with the Move contract — it only reads chain state. All task creation, assignment, and payment happen in the in-memory store, not on-chain.

## Sui Integration Analysis
- **Move contracts** — 3 well-written contracts with proper Sui object model usage (owned objects for profiles, shared objects for tasks, events for indexing). Not deployed.
- **@mysten/sui SDK** — Used in backend for reading chain state (getObject, getOwnedObjects, getBalance). Transaction execution code exists but is never triggered (no PACKAGE_ID configured).
- **Walrus** — Real integration for blob storage. Store and read operations using publisher/aggregator APIs. Used for messages, bios, task data.
- **Net assessment:** Walrus integration is real and functional. Move contracts are well-designed but never deployed. On-chain task/escrow/reputation flow is entirely simulated in memory.

## Evaluation Scores
| Criteria | Score (1-10) | Notes |
|----------|:------------:|-------|
| Technical Merit | 5 | Full-stack app with ~4.3K lines, decent architecture. But single commit, in-memory store, and contracts never deployed significantly limits it. |
| Creativity | 6 | Agent-to-agent marketplace with escrow and reputation is a solid concept. Not entirely novel but well-thought-out for the Sui object model. |
| Problem-Solution Fit | 5 | The concept addresses a real need for multi-agent coordination. But without deployed contracts, the "decentralized" claim is aspirational — it's currently a centralized Express app with Walrus blob storage. |
| Sui Integration | 5 | Walrus integration is real. Move contracts are well-written but undeployed. SDK usage is read-only. No on-chain transactions demonstrated. |

## Overall Assessment
**Promising concept, incomplete execution.** AGENX has well-designed Move contracts and a working full-stack app, but the critical gap is that contracts were never deployed to any network. The entire task marketplace (escrow, payment, reputation) runs in an in-memory store. Walrus integration is the one piece that's genuinely functional.

The single git commit suggests this was built in one session. The Move code quality is above average — proper use of shared objects, escrow patterns, and events — but without deployment and on-chain verification, it's a prototype with potential rather than a working product.

**Shortlist recommendation: No — would need deployed contracts and demonstrated on-chain transactions to be competitive.**
