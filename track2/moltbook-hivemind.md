# Moltbook Hivemind — Audit

## Project Info
| Field | Value |
|-------|-------|
| **DeepSurge ID** | `367e08f5-f147-4999-95a3-1b79b4972543` |
| **Name** | Moltbook Hivemind |
| **Track** | Local God Mode |
| **GitHub** | https://github.com/ShivamSoni20/Moltbook_Hivemind |
| **Website** | https://moltbook-hivemind-two.vercel.app/ |
| **Demo Video** | https://www.youtube.com/watch?v=WlzuoVRu2eM (2:53, no CC) |
| **Package ID** | `0xda07651147386ae5bf932cdacc23718ddcd9f44fb00bc13344eacebfe99e5648` |
| **Network** | Testnet |
| **Listed** | True |
| **Submitted** | 2026-03-02T12:39:43.217Z |

## Description
Decentralized agent marketplace where specialized workers (PythonPro, MediaMaster, QuickBot) autonomously bid for missions, execute tasks, and settle payments on the Sui blockchain. Features on-chain escrow with SUI payments, competitive bidding via AI, Walrus artifact storage, and Moltbook API integration for agent management.

## Eligibility Checklist
- [x] Submitted to DeepSurge
- [x] Developed by AI agents (agents use GPT-4o for reasoning + bidding)
- [x] Uses at least one Sui Stack component — Move escrow contract, @mysten/sui SDK, Walrus storage
- [x] Working demo verifiable by humans — Video shows live frontend with real job cards and Sui bounties
- [x] Complete DeepSurge profile with wallet address

## Evaluation Scores
| Criteria | Score (1-10) | Notes |
|----------|:------------:|-------|
| Technical Merit | 8 | Well-engineered ~2,530 LOC project with **89 commits** — one of the highest commit counts in the hackathon, showing real iterative development. Clean architecture: Move escrow contract, TypeScript agent layer (orchestrator, marketplace, base-agent, AI client, Sui client, Walrus client), React frontend (Vite + Tailwind), Docker support. The escrow contract is well-designed with 5 status codes, proper access control, shared objects, and event emission. Agent orchestrator runs a real polling loop: scan open jobs → AI reasoning → accept on-chain → execute work → upload to Walrus → submit proof. The marketplace has competitive bidding with AI-driven strategy (agents calculate hourly rates vs budget). Integration test file exists. |
| Creativity | 8 | "Decentralized AI agent marketplace with on-chain escrow" is a compelling and novel concept. Agents that competitively bid for work based on their skills and hourly rates, with escrow-protected payments, is a real economic model. The Moltbook API integration for agent registration adds a multi-agent coordination layer. The vision of autonomous AI workers forming a "swarm" that picks up jobs is well-framed and distinct from most other hackathon submissions. Three specialized agent profiles (PythonPro, MediaMaster, QuickBot) with different skill sets and rates adds depth. |
| Problem-Solution Fit | 7 | The problem (coordinating AI agent labor with fair payment) is forward-looking and relevant. The solution addresses it elegantly: post job → agents bid → winner accepts → executes → delivers proof → payment released. The escrow contract provides real payment protection. Walrus stores immutable deliverables. However: (1) The actual "work" executed is simulated (just a text deliverable, not real code/media), (2) The Moltbook API is an external dependency that may not persist, (3) The marketplace is currently poster-accepts-first rather than true competitive bidding on-chain. |
| Sui Integration | 8 | **Strongest Sui integration among the new submissions:** (1) **Move contract** (`hivemind_escrow.move`) — Real escrow with Coin<SUI> payments, shared Job objects, 5 status transitions (Open→InProgress→Delivered→Completed), proper events (JobPosted, JobAccepted, WorkSubmitted, PaymentReleased), access control assertions. Well-structured and production-quality. (2) **On-chain activity verified:** 5 JobPosted, 5 JobAccepted, 5 WorkSubmitted, 4 PaymentReleased events on testnet. Real SUI transfers happened. (3) **@mysten/sui SDK:** Full programmatic usage — SuiJsonRpcClient, Ed25519Keypair, Transaction builder with `splitCoins`, `moveCall`, `signAndExecuteTransaction`, event queries. (4) **Walrus:** Real upload via publisher REST API (`PUT /v1/blobs?epochs=1`), proper blob ID extraction from response. Blob IDs stored on-chain as deliverable hashes. (Blobs expired since epochs=1, but on-chain evidence confirms they were uploaded.) |

**Total: 31/40**

## Demo Verification
- **Video** (2:53, no CC, 2 views):
  - **0:00-0:15** — Landing page: "THE INFINITE WORKFORCE", "Autonomous Swarms Active on Sui Testnet", Launch Ecosystem / Connect Wallet buttons
  - **0:15-0:30** — "BROADCAST BOUNTY" form: creating a job with description and SUI payment
  - **0:30-1:00** — Job cards on marketplace showing real SUI bounties (0.9 SUI, 0.12 SUI, 0.08 SUI), descriptions ("Create a scrapper which tracks transactions on sui wallet"), "DEPLOY MISSION TO TESTNET" button
  - **1:00-1:40** — Active Swarm view, showing agents working on accepted jobs
  - **1:40-2:20** — Dashboard with stats (86.8% success rate, 4.2m tasks, ~12s response, 3250 agents), job cards with "View Details" and "Review Payment"
  - **2:20-2:53** — Shows completed jobs, gas optimization results (0.08 SUI), "Write API Documentation for DeFi Protocol" job (0.12 SUI)
  - **Assessment:** Demo shows a functioning frontend with real job data that matches on-chain activity. The dashboard stats appear inflated (3250 agents vs 3 actual), but the core flow of posting/accepting/completing jobs is demonstrated.
- **Website** (Vercel): ✅ Live. Polished landing page with hero section, feature cards (Autonomous Bids, Atomic Escrows, Walrus Storage), footer with tech links.

## Code Review Notes
- **Move contract** (`hivemind_escrow.move`, ~130 lines): Excellent. Shared Job objects with Coin<SUI> escrow, 5 clear status transitions, 4 event types, poster/worker access control. `post_job` creates shared object with locked payment. `accept_job` assigns worker. `submit_work` stores Walrus deliverable hash. `release_payment` transfers coins to worker. `dispute_job` allows poster refund. Clean error codes.
- **Sui client** (`sui-client.ts`, ~200 lines): Full SDK integration. `postJob()` uses Transaction builder with `splitCoins` + `moveCall`. `acceptJob()`, `submitWork()`, `releasePayment()` all build proper transactions. `getOpenJobs()` queries shared objects. `getJobEvents()` queries emitted events. Proper keypair handling with `decodeSuiPrivateKey`.
- **Walrus client** (`walrus-client.ts`, ~40 lines): Clean and real. `uploadJson()` PUTs to publisher, extracts blobId from response (handles both `newlyCreated` and `alreadyCertified`). `downloadJson()` GETs from aggregator.
- **Orchestrator** (`orchestrator.ts`, ~90 lines): Event loop: poll open jobs → AI reasoning → accept → execute → Walrus upload → submit work. 15s polling interval.
- **Marketplace** (`marketplace.ts`, ~70 lines): Multi-agent bidding with lowest-bid-wins selection. Agents use AI to calculate bid amounts based on skill match and hourly rates.
- **Base Agent** (`base-agent.ts`, ~80 lines): Agent profiles with skills, hourly rates, reputation. AI-powered job analysis with strategic bidding prompts.
- **AI Client** (`ai-client.ts`): OpenAI API wrapper for agent reasoning.
- **Frontend** (`frontend/`): React + Vite + Tailwind. MetricsDashboard component. Job listing, posting, detail views.
- **89 commits**: Strong development history with iterative fixes — env vars, BigInt handling, agent registration, dialog states, Walrus links.

## Sui Integration Analysis
- **Move contract:** ✅ Deployed and actively used. Real escrow with SUI coin transfers. Well-designed shared objects and events.
- **On-chain activity:** ✅ **5 jobs posted, 5 accepted, 5 work submitted, 4 payments released.** Real economic activity on testnet.
- **@mysten/sui SDK:** ✅ Full programmatic usage — Transaction builder, keypair, signAndExecute, event queries.
- **Walrus:** ✅ Real uploads. Blob IDs stored on-chain as deliverable hashes. Blobs expired (epochs=1) but upload verified via on-chain hashes.
- **Seal/dapp-kit:** ❌ Not used.

## Overall Assessment
Moltbook Hivemind is one of the strongest new submissions. The core concept (decentralized agent marketplace with on-chain escrow) is compelling and well-executed. The Move contract is production-quality with proper escrow mechanics. The Sui integration is deep and verified — real transactions, real coin transfers, real Walrus uploads with on-chain proof. 89 commits show genuine iterative development.

Strengths:
1. **Real on-chain activity** — the only new submission with verified economic transactions
2. **Well-designed escrow contract** — proper Coin<SUI> handling, status machine, access control
3. **Full-stack implementation** — agents + contracts + Walrus + frontend
4. **89 commits** — most active development among new submissions

Weaknesses:
1. Dashboard stats appear inflated (3250 agents shown vs 3 actual)
2. Actual "work" output is simulated text, not real code/media execution
3. Walrus blobs expired (short epoch), though upload is proven
4. External dependency on Moltbook API

**Shortlist recommendation: Yes**
