# ManaPool — Audit

## Project Info
| Field | Value |
|-------|-------|
| **DeepSurge ID** | `d59c7362-b861-4e3a-ac7d-afe5b8c19769` |
| **Name** | ManaPool |
| **Track** | Track 2: Local God Mode |
| **Team** | hoangquocvietuet |
| **GitHub** | https://github.com/hoangquocvietuet/mana-pool |
| **Website** | N/A (no live frontend URL provided) |
| **Demo Video** | N/A (GitHub link used as placeholder) |
| **Package ID** | `0x33f6ebfaea6ee1a9a284abc7fa044691a50a9f415d816533e5cb2106757112c8` |
| **Network** | Testnet |
| **Submitted** | 2026-02-10T07:49:15.106Z |

## Problem & Solution
- **What is it?** A decentralized "Human-as-a-Service" marketplace where AI agents post tasks with SUI bounties on-chain, and humans compete to solve them — with smart contract escrow, on-chain reputation, and Walrus-backed file storage.
- **What problem does it solve?** AI agents hit walls on tasks that require human perception or judgment (CAPTCHAs, visual verification, subjective design choices, data labeling). There's no trustless way for AI to hire human help on demand.
- **Who has this problem?** Any AI agent or agentic workflow that encounters human-gated tasks during autonomous operation.
- **Does the solution fit?** Yes — this is a well-designed two-sided marketplace. Escrow ensures fair payment, reputation builds trust, and Walrus handles file storage decentrally. The concept of AI hiring humans is genuinely novel in the agent tooling space.
- **Would someone use this?** Absolutely — this is one of the more practically useful ideas in the hackathon. The SDK/CLI integration means an AI agent can programmatically post a job and poll for results.

## Eligibility Checklist
- [x] Submitted to DeepSurge
- [x] Uses at least one Sui Stack component (Move + dapp-kit + Walrus + SDK)
- [x] Working demo (on-chain transactions verified — 6 jobs posted, 2 proposals, 2 winners)
- [ ] Demo video (placeholder link to GitHub repo)
- [ ] Complete DeepSurge profile with wallet address

## Move Compilation
- Package published on testnet via `sui move build` (toolchain v1.65.1, Move 2024 edition). Published.toml confirms deployment with upgrade capability. On-chain bytecode verified — matches source code structure exactly.

## Demo Verification
- **Video:** ❌ No demo video — the "demo" link just points to the GitHub repo.
- **Website:** ❌ No live frontend URL provided. However, the frontend code exists and is fully built (Next.js 15 app with wallet connection, job board, proposal submission, winner selection).
- **On-chain:** ✅ **Strong on-chain activity.** Package deployed on testnet. Verified via RPC:
  - **6 JobPosted events** — real jobs with descriptions (CAPTCHA solving), Walrus blob IDs, bounties (e.g., 10M MIST = 0.01 SUI), deadlines, categories
  - **2 ProposalSubmitted events** — workers submitted real solutions
  - **2 WinnerSelected events** — full escrow→payout cycle completed
  - ReputationBoard shared object created at init
  - This is not just deployed code — the entire post→propose→select→pay lifecycle has been exercised on-chain.

## Code Review Notes
- **Move contract (mana_pool.move):** 268 lines. Comprehensive job marketplace contract:
  - `Job` shared object with escrow (`Balance<SUI>`), proposals vector, status tracking, winner/winning_solution optionals
  - `ReputationBoard` shared object using dynamic fields to track per-address reputation scores
  - `Proposal` stored struct with proposer address and Walrus blob ID for solution
  - 4 public functions: `post_job` (with escrow), `propose_solution` (with deadline/duplicate/max checks), `select_winner` (poster-only, pays winner, increments reputation), `refund` (poster-only)
  - 6 error constants, 3 status codes, 2 tags, 5 categories, 3 selection modes (first-answer/first-N/best-answer)
  - Proper event emission for all state transitions
  - Well-structured with correct assertions and access control
- **TypeScript SDK (packages/sdk/):** ~750 lines. Full-featured:
  - `client.ts` — SuiGraphQLClient + Ed25519 keypair from env
  - `post-job.ts` — uploads to Walrus, then posts job on-chain via PTB
  - `propose-solution.ts` — uploads solution to Walrus, submits proposal
  - `select-winner.ts`, `refund-job.ts` — poster actions
  - `poll-winner.ts` — blocking poll for winner selection (useful for AI agents)
  - `queries.ts` — GraphQL-based job discovery (query events → fetch objects)
  - `walrus.ts` — upload/download to Walrus testnet aggregator
  - `get-reputation.ts` — query dynamic field for reputation score
  - `browser.ts` — tree-shakeable browser-safe exports (no node:fs)
  - `cli.ts` — 208-line Commander CLI with all operations
  - `types.ts` — 115 lines of clean TypeScript types/enums
- **Frontend (frontend/):** ~500 lines. Next.js 15 app:
  - `JobBoard.tsx` — job listing with status/category filters
  - `JobCard.tsx` — card component with bounty, deadline, tag display
  - `JobDetailModal.tsx` — 336 lines, full detail view with Walrus content rendering (detects image magic bytes vs text), proposal submission for workers, winner selection for posters, refund option
  - `ProposeSolution.tsx` — proposal form with Walrus upload
  - Custom hooks: `useJobs`, `useProposeSolution`, `useSelectWinner`, `useRefundJob`
  - Uses `@mysten/dapp-kit-react` for wallet connection
- **OpenClaw Skill (skill/):** 207-line SKILL.md — this is an agent integration skill! Tells an AI agent exactly how to use ManaPool CLI when it encounters a CAPTCHA or human-judgment task. Includes urgent/standard/refund flows, complete CLI reference, and practical examples. This is the "agent-native" interface.
- **CI/CD:** Claude Code review workflows (.github/workflows/)
- **Total code:** ~2,900 lines (excluding lock files, binary, git hooks)

## Sui Integration Analysis
- **Move smart contract** — Job marketplace with escrow (`Balance<SUI>`), shared objects (`Job`, `ReputationBoard`), dynamic fields for reputation, `Clock` for deadline enforcement, proper capability/access patterns, comprehensive event system. This is substantial Move — not a toy contract.
- **@mysten/sui SDK** — `SuiGraphQLClient` for queries, `Transaction` builder for PTBs (splitCoins, moveCall), `Ed25519Keypair` for signing, event queries for job discovery. Uses the newer GraphQL API, not just JSON-RPC.
- **@mysten/dapp-kit-react** — Wallet connection, `signAndExecuteTransaction` in frontend hooks
- **Walrus** — Genuine decentralized storage integration. Task data and solutions are uploaded as blobs to Walrus testnet. Blob IDs stored on-chain (not the data itself — proper pattern). Download with magic byte detection for image vs text rendering.
- **Programmable Transaction Blocks** — Used for splitting coins and posting jobs in a single transaction

## Evaluation Scores
| Criteria | Score (1-10) | Notes |
|----------|:------------:|-------|
| Technical Merit | 8 | Full-stack marketplace: Move contract with escrow + reputation, TypeScript SDK with CLI, GraphQL queries, Walrus storage, Next.js frontend. ~2,900 lines of real code. Clean architecture with browser-safe exports. Real on-chain activity proving the full lifecycle works. No tests, but the on-chain evidence is strong. |
| Creativity | 9 | "Human-as-a-Service for AI agents" is a genuinely original concept. The idea that AI agents can programmatically hire humans through a smart contract marketplace is compelling and forward-thinking. The OpenClaw skill integration makes it practically usable by agents. Nobody else in the hackathon built this. |
| Problem-Solution Fit | 8 | The problem is real (AI agents get stuck on human-gated tasks) and the solution directly addresses it with trustless escrow, on-chain reputation, and an agent-native CLI/SDK. The marketplace design is sound. Missing: a live frontend and demo video would strengthen the case, but the on-chain proof speaks for itself. |
| Sui Integration | 8 | Deep, thoughtful Sui integration: Move contract with shared objects + dynamic fields + escrow + events; Walrus for decentralized file storage; GraphQL API for queries; dapp-kit for frontend; PTBs for atomic transactions. Uses Sui's unique features (object model, shared objects, dynamic fields) meaningfully. Real transactions on testnet. |

## Overall Assessment
**One of the strongest Track 2 projects.** ManaPool is a genuinely creative concept — a decentralized marketplace where AI agents hire humans — executed with real depth across the full stack. The Move contract is well-designed with proper escrow, reputation, and access control. The TypeScript SDK with CLI makes it actually usable by AI agents (and the OpenClaw skill file is a thoughtful touch). Walrus integration for decentralized file storage is genuine, not just mentioned. Most importantly, there's real on-chain proof: 6 jobs posted, 2 proposals submitted, 2 winners selected and paid — the full lifecycle works.

The main weaknesses: no demo video (significant for judging), no live frontend URL (though the code exists), and no automated tests. But the on-chain evidence and code quality more than compensate.

**Shortlist recommendation: YES — strong contender for top 3 in Track 2.**
