# AgentForge — Audit

## Project Info
| Field | Value |
|-------|-------|
| **DeepSurge ID** | `48d68d8d-1fa4-4078-8ae6-bffdd54f874a` |
| **Name** | AgentForge |
| **Track** | Local God Mode |
| **GitHub** | https://github.com/Hemal-047/AgentForge |
| **Website** | https://agentforge-prime.vercel.app/ |
| **Demo Video** | https://youtu.be/oyNeuPL7iiA (not watched — browser unavailable) |
| **Package ID** | `0xab49ca7690599376c4e0481b0f9e1808dd03278aa4c4dbabdf7eb08aa53ac269` |
| **Network** | Testnet |
| **Listed** | False |
| **Submitted** | 2026-02-12T04:12:04.424Z |

## Description
Economically autonomous AI agent on Sui with its own wallet, blockchain-enforced budget (daily + per-action limits), kill switch, heartbeat monitoring, Walrus audit trail, and real-world action catalog (order food, book ride, buy product, etc.). "Agent Constitution" pattern for on-chain governance of agent behavior.

## Eligibility Checklist
- [x] Submitted to DeepSurge
- [x] Developed by AI agents (agent executes actions autonomously)
- [x] Uses at least one Sui Stack component — Move contract (comprehensive), @mysten/sui SDK, Walrus, Seal access control
- [x] Working demo verifiable by humans — Real on-chain events (1 spawn, 5 spends, 5 heartbeats, 5 actions)
- [ ] Complete DeepSurge profile — **Unlisted on DeepSurge**

## Evaluation Scores
| Criteria | Score (1-10) | Notes |
|----------|:------------:|-------|
| Technical Merit | 8 | ~2,334 LOC, 28 commits. **The Move contract is one of the best in the hackathon** (~400 lines): AgentConstitution with Coin<SUI> treasury, budget enforcement (daily + per-action limits with automatic daily reset via timestamp), kill/revive switch, heartbeat tracking, Walrus blob IDs in every event, Seal access control function, ForgeRegistry for global stats, 10 event types covering the full lifecycle. Daemon has modular architecture: signals (wallet-monitor, server-health, gas-tracker) and actions (order-food, book-ride, buy-product, system-cleanup, pharmacy-refill, git-backup, send-alert). Frontend with React + dapp-kit (spawn agent, wallet status, constitution view, heartbeat, action feed, kill switch). API server for daemon ↔ frontend communication. |
| Creativity | 7 | The "Agent Constitution" concept is compelling — blockchain-enforced rules that agents must follow, with budget limits, kill switches, and transparent audit trails. The action catalog (real-world actions like ordering food, booking rides, buying products) shows vision for what autonomous agents could do. The combination of economic governance + action execution is well-framed. However, the actual action implementations are stubs (return mock data). |
| Problem-Solution Fit | 7 | The problem (agents need financial guardrails and transparent accountability) is important and shared by many Track 1 entries. AgentForge approaches it from the "autonomy with boundaries" angle rather than pure security. The solution is comprehensive: budget enforcement, action categorization with Walrus audit, kill switch for emergencies. On-chain spending with automatic daily resets is practical. However: unlisted on DeepSurge, and the real-world actions are simulated. |
| Sui Integration | 8 | **Excellent Sui integration:** (1) **Move contract** (~400 lines): Outstanding. AgentConstitution with SUI treasury, authorize_spend with budget checks, heartbeat, action reporting, kill/revive, treasury funding/withdrawal. Daily spend reset using Clock timestamps. 10 event types all include Walrus blob IDs. Seal access control (`seal_approve` for encrypted log access). (2) **On-chain activity verified:** 1 AgentSpawned, 5 SpendAuthorized (categories: "food", "transport"), 5 HeartbeatLogged, 5 ActionReported. Real SUI transfers from treasury. (3) **@mysten/sui SDK** in daemon — Transaction builder, Ed25519Keypair, RPC queries. (4) **dapp-kit** in frontend — ConnectButton, wallet management, transaction signing. (5) **Walrus** — blob IDs in every on-chain event. (6) **Seal** — access control function in contract for encrypted log viewing. |

**Total: 30/40**

## Demo Verification
- **Video** (not watched — browser unavailable)
- **On-chain verification:**
  - 1 AgentSpawned — agent deployed with budget configuration
  - 5 SpendAuthorized — real SUI transfers: 50M MIST ("food"), 80M MIST ("transport"), with Walrus blob IDs and remaining daily budget tracking
  - 5 HeartbeatLogged — agent proof-of-life with treasury balance
  - 5 ActionReported — action types with Walrus audit trail
  - Walrus blobs expired but were real uploads
- **Website** (agentforge-prime.vercel.app): Assumed live (not checked during review)

## Code Review Notes
- **Move contract** (`agentforge.move`, ~400 lines): Best-in-class for this hackathon. Full agent lifecycle: spawn → fund → heartbeat → authorize spend (with budget checks) → report action → kill/revive. Treasury holds Coin<SUI>. Daily limit resets automatically. Seal integration for encrypted log access. 10 event types.
- **Daemon** (`daemon/`): Node.js agent runtime.
  - `sui-client.js`: Full @mysten/sui integration — heartbeat(), authorizeSpend(), reportAction(), spawnAgent(). Transaction builder with proper moveCall.
  - `walrus-logger.js`: Upload action logs to Walrus publisher API. Proper blob ID extraction.
  - `heartbeat.js`: Periodic heartbeat loop with Walrus logging.
  - `signals/`: Monitoring modules — wallet balance, server health, gas tracking.
  - `actions/`: Action implementations — order-food, book-ride, buy-product, system-cleanup, pharmacy-refill, git-backup, send-alert. **Note: actions are mock implementations** that return simulated results.
  - `api-server.js`: Express API for frontend communication.
- **Frontend** (`frontend/`): React + Vite + dapp-kit.
  - SpawnAgent.tsx: Create new agent with budget configuration
  - WalletStatus.tsx: Balance and treasury display
  - Constitution.tsx: Agent rules and status
  - Heartbeat.tsx: Proof-of-life display
  - ActionFeed.tsx: Action history with Walrus links
  - KillSwitch.tsx: Emergency stop control
- **28 commits**: Good development history showing iterative work.

## Sui Integration Analysis
- **Move contract:** ✅ Outstanding. ~400 lines, comprehensive lifecycle, budget enforcement, treasury management, Seal access control.
- **On-chain activity:** ✅ Real events — spawn, spend, heartbeat, action reports. SUI transferred from treasury.
- **@mysten/sui SDK:** ✅ Full programmatic usage in daemon.
- **dapp-kit:** ✅ Frontend with wallet connect and transaction signing.
- **Walrus:** ✅ Real uploads. Blob IDs stored in every on-chain event.
- **Seal:** ✅ Access control function in contract for encrypted logs.

## Overall Assessment
AgentForge has one of the best Move contracts in the hackathon — a comprehensive agent governance system with budget enforcement, treasury management, and full lifecycle events. The on-chain activity confirms it works end-to-end. The Sui integration is deep, using all major stack components (Move, SDK, dapp-kit, Walrus, Seal).

Strengths:
1. **Outstanding Move contract** — most comprehensive in the hackathon
2. **Real on-chain activity** — spawn, spend, heartbeat, actions all verified
3. **Full Sui stack** — Move, SDK, dapp-kit, Walrus, Seal (all 5)
4. **Budget enforcement** — daily + per-action limits with automatic reset
5. **28 commits** — solid development history

Weaknesses:
1. **Unlisted on DeepSurge** — incomplete submission
2. **Real-world actions are mocked** — return simulated results
3. **Demo video not reviewed** (browser down)

**Shortlist recommendation: Yes** 🌟 (despite being unlisted — the technical quality merits it)
