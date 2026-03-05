# Sui Safety Middleware MVP — Audit

## Project Info
| Field | Value |
|-------|-------|
| **DeepSurge ID** | `55bbe288-16ce-42fd-af92-ecc4c755fc3f` |
| **Name** | Sui Safety Middleware MVP |
| **Track** | Safety & Security |
| **GitHub** | https://github.com/1131764933/sui-safety-middleware-mvp |
| **Website** | https://sui-safety-middleware-mvp-frontend.vercel.app/ |
| **Demo Video** | https://www.youtube.com/watch?v=WfrVkump0SU |
| **Package ID** | `0xab52ad97fc2a24e3070b7999fc7eeca5baef006269ac39245f3da7d5caecd5fd` |
| **Network** | Testnet |

## Eligibility Checklist
- [x] Submitted to DeepSurge
- [x] Developed by AI agents (or mostly AI agents)
- [x] Uses at least one Sui Stack component
- [x] Working demo verifiable by humans
- [x] Complete DeepSurge profile with wallet address

## Demo Verification
- YouTube video exists: **Yes** — titled "Sui Safety Middleware"
- Website: **Live on Vercel** ✅
- On-chain verification: Package ID verified on Sui Testnet — **exists as `package` type** ✅

## Code Review Notes
- **Repo structure:** Monorepo with `apps/frontend`, `apps/backend`, `contracts/safety_middleware`, `api/`, `scripts/`, `tests/`, `docs/`
- **Lines of code:** ~1,565 lines across Move, JS/TS, and MJS files
- **Move contracts:** 2 modules — `policy.move` (47 lines) and `audit.move` (35 lines)
  - `policy.move`: PolicyObject with owner, daily_limit, whitelist. Basic CRUD with owner assertion.
  - `audit.move`: AuditObject storing tx_digest, action, status. Has `create_and_transfer` for audit logging.
  - `policy_tests.move`: 28 lines of basic unit tests
  - **Assessment:** Contracts are minimal — functional but very thin. No shared objects, no events, limited logic.
- **API layer (router.mjs):** Express-style handler routing to precheck, approval, execute, audit endpoints. In-memory stores (Map/Array).
- **Backend:** Precheck, approval confirmation, execution, and audit route handlers. AI risk explanation integration mentioned.
- **Frontend:** Vite + TypeScript. Basic app flow.
- **Tests:** Multiple test files (app-flow, ai, execute, precheck, routes) — good test coverage for the scope.
- **Demo scripts:** Shell scripts for low-risk, high-risk-review, and failure-fallback scenarios.
- **Documentation:** Extensive Chinese and English docs — brainstorming templates, chain analysis, security assumptions, demo runbook. Lots of planning docs relative to code.

## Sui Integration Analysis
**Basic but real Sui integration:**
- **Move smart contracts** — Policy and Audit modules deployed on testnet. Verified on-chain.
- **Contract design:** Very minimal — PolicyObject is essentially a struct with owner + daily_limit + whitelist. AuditObject just stores tx metadata. No complex logic, no events from policy module, no interaction between modules.
- **Frontend/Backend** — The middleware logic (precheck, approval gating, blocking) lives in JS, not in the Move contracts. The on-chain part is essentially a record-keeping layer.
- **Missing:** No Walrus, no Seal, no dapp-kit usage visible. No PTBs. The "middleware" concept is implemented off-chain with contracts as passive storage.

**Key observation:** The security logic (rule-based prechecks, human-in-the-loop approval, blocking) is implemented server-side. The Move contracts just store policy configs and audit records. This makes the "on-chain safety middleware" claim somewhat misleading — the middleware itself runs off-chain.

## Evaluation Scores
| Criteria | Score (1-10) | Notes |
|----------|:------------:|-------|
| Technical Merit | 4 | Working but thin. Move contracts are ~80 lines with minimal logic. Backend is functional but basic. Good test coverage relative to scope. Lots of docs but light on code. |
| Creativity | 5 | Transaction pre-screening and human-in-the-loop approval is a reasonable idea for agent safety. Not highly original — several other submissions do similar things. |
| Problem-Solution Fit | 5 | The problem (agent transactions need safety checks) is real. The solution works for a demo but the on-chain component is too thin to provide real security — the actual safety logic is off-chain and bypassable. |
| Sui Integration | 4 | Package deployed and verified. But contracts are minimal — no events, no complex logic, no interaction between policy and audit. Sui is used as a passive store, not leveraging object model or PTBs. |

## Red Flags
- Description is bilingual (Chinese/English) — description in Chinese mentions this is a "hackathon-ready demo" which is honest
- High ratio of documentation/planning files to actual code
- Move contracts are very basic — could be generated in minutes
- Website link is `http://127.0.0.1` for some similar projects but this one has a real Vercel deployment

## Overall Assessment
**Below-average submission for Track 1.** The concept (safety middleware for agent transactions) is sound and relevant. But the implementation is shallow — Move contracts are ~80 lines of basic struct management, the security logic lives entirely off-chain in JS, and Sui is used only as a passive record store.

The demo scripts and test files show effort, and the project is honest about being an MVP. But compared to other Track 1 submissions with deeper on-chain logic, this doesn't stand out technically.

**Shortlist recommendation: No — insufficient depth for top consideration in Track 1.**
