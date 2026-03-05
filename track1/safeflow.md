# SafeFlow — Audit

## Project Info
| Field | Value |
|-------|-------|
| **DeepSurge ID** | `89867ace-ee49-4274-a817-b58ddacce054` |
| **Name** | SafeFlow (Sui Edition) |
| **Track** | Safety & Security |
| **GitHub** | https://github.com/FWangZil/safeflow-sui |
| **Website** | https://dash.safeflow.space |
| **Demo Video** | https://www.youtube.com/watch?v=pAd18KE81DI (browser unavailable — not watched) |
| **Package ID** | `0xcc76747b518ea5d07255a26141fb5e0b81fcdd0dc1cc578a83f88adc003a6191` |
| **Network** | Testnet |
| **Listed** | True |
| **Submitted** | 2026-03-04T04:39:43.601Z |

## Description
On-chain fund management and streaming payment protocol for AI Agents (OpenClaw). Uses Sui's Object Model to create an AgentWallet (human-owned, shared object) with SessionCap (agent-held capability) that enforces rate limits, spend caps, and expiry. Every payment requires a Walrus blob ID as audit trail. Includes a Producer API for payment intents and a Next.js dashboard with dapp-kit.

## Eligibility Checklist
- [x] Submitted to DeepSurge
- [x] Developed by AI agents (Claude skills in .claude/ with SKILL.md files)
- [x] Uses at least one Sui Stack component — Move contract, @mysten/sui SDK, dapp-kit, Walrus
- [x] Working demo verifiable by humans — Real on-chain payments verified
- [x] Complete DeepSurge profile with wallet address

## Evaluation Scores
| Criteria | Score (1-10) | Notes |
|----------|:------------:|-------|
| Technical Merit | 9 | Exceptionally well-architected project with 21 commits. **Move contract is production-quality**: AgentWallet<T> (generic, phantom type param for any coin), SessionCap with rate limiting (spend per second + total cap + expiry), shared object pattern. The payment execution has 5 sequential checks (expiry → wallet match → total limit → rate limit → balance). **Full-stack implementation**: Move contracts with tests, TypeScript agent SDK (@safeflow/sui-sdk), e2e runner, Walrus verification script, Producer API (Node.js HTTP server with HMAC signing, intent lifecycle management), Next.js dashboard with dapp-kit. Claude Code skills (.claude/) provide agent-installable capabilities. Extensive documentation (architecture docs in EN/CN, runbooks, role flows, Marp slides). |
| Creativity | 8 | "Streaming payments with capability-based authorization" is a genuinely novel approach to the agent wallet problem. The SessionCap pattern (human creates → transfers to agent → agent uses to spend with rate limits) perfectly leverages Sui's object model. Requiring a Walrus blob ID for every payment (audit trail baked into the protocol) is elegant design. The Producer API adding a business layer (payment intents with merchant orders, HMAC-signed webhooks) shows real-world thinking beyond hackathon scope. Multiple Claude skills for different deployment patterns (self-deploy vs shared contract) shows ecosystem thinking. |
| Problem-Solution Fit | 8 | The problem (how to safely let AI agents spend money with guardrails) is THE core challenge for autonomous agents. SafeFlow's solution is comprehensive: (1) Human-owned wallet = human always controls funds. (2) SessionCap with time-based rate limits prevents runaway spending. (3) Walrus audit trail for every payment = transparent reasoning. (4) Expiry = time-bounded authorization. (5) Producer API = real payment intent workflow. This directly addresses "Wallet Air-Gap" from the hackathon brief. The on-chain verification (5 payments executed) proves it works end-to-end. |
| Sui Integration | 9 | **Best-in-class Sui integration for Track 1:** (1) **Move contract** (`wallet.move`, ~130 lines): AgentWallet<phantom T> (generic for any coin type), SessionCap with rate limiting, shared objects, proper events, Clock usage, comprehensive error handling. (2) **On-chain activity verified**: 2 WalletCreated, 2 SessionCapCreated, 5 PaymentExecuted events. Real SUI transfers (1M and 10M MIST). (3) **@mysten/sui SDK**: Full programmatic usage — SuiClient, Ed25519Keypair, Transaction builder. (4) **dapp-kit**: Next.js dashboard with ConnectButton, useSignAndExecuteTransaction, useSuiClient. (5) **Walrus**: Every PaymentExecuted event includes walrus_blob_id field. Verification script queries on-chain events → extracts blob IDs → fetches from Walrus aggregator. Some blob IDs are demo/fallback values but the integration is real. (6) Move tests exist (`wallet_tests.move`, `agent_wallet_tests.move`). |

**Total: 34/40**

## Demo Verification
- **Video**: Browser was unavailable during review — video not watched. (YouTube: pAd18KE81DI)
- **On-chain verification** (compensates for missed video):
  - Package deployed: ✅
  - 2 wallets created, 2 session caps created, 5 payments executed
  - Real SUI transfers: 1M MIST ($0.001 SUI) and 10M MIST ($0.01 SUI)
  - `walrus_blob_id` in events: "demo_success_001", "demo_fail_001", "fallback:c61b1f..." (mix of demo and real hashes)
- **Website** (dash.safeflow.space): Not checked (browser down). Appears to be Next.js dashboard.

## Code Review Notes
- **Move contract** (`wallet.move`, ~130 lines): Outstanding design.
  - `AgentWallet<phantom T>`: Generic for any coin type (SUI, USDC, etc.)
  - `SessionCap`: rate limit (max_spend_per_second), total cap (max_spend_total), expiry (expires_at_ms), state tracking (total_spent, last_spend_time_ms)
  - `execute_payment`: 5 sequential assertions — expiry → wallet match → total limit → rate limit → balance. Walrus blob ID required as parameter.
  - Events: WalletCreated, SessionCapCreated, PaymentExecuted (with walrus_blob_id)
  - Shared object for wallet (anyone can read), SessionCap transferred to agent
- **Agent SDK** (`@safeflow/sui-sdk`): Published as importable package. SafeFlowAgent class, ProducerApiClient, skill integration.
- **E2E Runner** (`e2e_runner.ts`): Full end-to-end test — load agent key → connect to producer API → poll for intents → execute payment → verify on-chain.
- **Walrus Verify** (`walrus_verify.ts`): Queries transaction by digest → extracts PaymentExecuted event → gets walrus_blob_id → fetches from Walrus aggregator → generates site URL.
- **Producer API** (`server.mjs`): HTTP server with HMAC-signed intents, intent lifecycle (pending → processing → completed/failed/expired), file-based persistence, CORS, health check.
- **Web Dashboard** (`web/`): Next.js + dapp-kit. Wallet creation, session cap management, payment monitoring. ConnectButton, useSignAndExecuteTransaction.
- **Claude Skills** (`.claude/`): Two skills — `executing-safeflow-payments` (self-deploy) and `using-safeflow-shared-contract` (shared contract with owner handoff). Proper SKILL.md format with shell scripts.
- **Documentation**: Architecture docs (EN + CN), e2e runbooks, role flow diagrams, deployment guides, agent skill installation guide, Marp presentation slides. Comprehensive.

## Sui Integration Analysis
- **Move contract:** ✅ Production-quality. Generic types, capability pattern, rate limiting, Walrus integration baked in.
- **On-chain activity:** ✅ Real payments executed with SUI coin transfers.
- **@mysten/sui SDK:** ✅ Full programmatic usage.
- **dapp-kit:** ✅ Next.js dashboard with wallet connect + transaction signing.
- **Walrus:** ✅ Audit trail in every payment event. Verification script fetches blobs.
- **Seal:** ❌ Not used (would be a natural addition for encrypted payment intents).

## Overall Assessment
SafeFlow is one of the strongest Track 1 submissions. The Move contract is elegantly designed — using Sui's object model (shared wallet + transferable capability) to solve the agent wallet authorization problem in a way that's native to the platform. The SessionCap rate-limiting mechanism is a real innovation that other projects should adopt.

Strengths:
1. **Production-quality Move contract** — generic types, 5-check payment validation, rate limiting
2. **Real on-chain payments** — 5 verified PaymentExecuted events with SUI transfers
3. **Full-stack** — Move + agent SDK + e2e runner + producer API + web dashboard + agent skills
4. **Walrus audit trail** built into the protocol (not bolted on)
5. **Comprehensive documentation** — bilingual, with runbooks and architecture diagrams
6. **Claude Code skills** — agent-installable, shows ecosystem thinking

Weaknesses:
1. Demo video not reviewed (browser was down)
2. Some Walrus blob IDs are demo values rather than real uploads
3. No Seal integration for encrypted intents

**Shortlist recommendation: Yes** 🌟
