# StillClawing — Audit

## Project Info
| Field | Value |
|-------|-------|
| **DeepSurge ID** | `a3e283a0-6735-4e1a-9afa-6ea19a757c04` |
| **Name** | StillClawing 🦞 — Dead Man's Switch for AI Agents |
| **Track** | Local God Mode |
| **GitHub** | https://github.com/apkaisaw/StillClawing |
| **Website** | https://stillclawing.vercel.app/ |
| **Demo Video** | https://youtu.be/b3myS3UKO2A (not watched — browser unavailable) |
| **Package ID** | `0xa6fc33dc99e45fedb2f8eb4b3a02556c9a7b1acbcc1ca0414d6fb664362dd0a8` |
| **Network** | Testnet |
| **Listed** | True |
| **Submitted** | 2026-03-04T05:15:37.397Z |

## Description
Inspired by "死了么" (Are You Dead Yet?), the Chinese solo-living safety app. StillClawing is an autonomous watchdog for OpenClaw agents: monitors gateway health, sends on-chain heartbeat proofs, auto-rescues crashed agents, backs up agent "soul" (state/memories) to Walrus, executes a "digital will" (asset transfer to inheritor) if rescue fails, and announces on Moltbook social platform.

## Eligibility Checklist
- [x] Submitted to DeepSurge
- [x] Developed by AI agents (concept inspired by autonomous agent lifecycle management)
- [x] Uses at least one Sui Stack component — Move contract, @mysten/sui SDK, Walrus backup
- [x] Working demo verifiable by humans — Website live, demo video available (not watched)
- [x] Complete DeepSurge profile with wallet address

## Evaluation Scores
| Criteria | Score (1-10) | Notes |
|----------|:------------:|-------|
| Technical Merit | 7 | ~1,365 LOC TypeScript, 7 commits. Clean modular architecture: daemon (index.ts), doctor (gateway health check + rescue), sui-heartbeat (on-chain proof-of-life), walrus-backup (soul preservation), moltbook (social API), config management. Move contract is well-designed with AgentRegistry, heartbeat/death/resurrection lifecycle, inheritor for digital will. The daemon loop handles the full lifecycle: heartbeat check-in → death detection → rescue attempt → soul backup → will execution → obituary. Uses `SuiGrpcClient` (newer SDK). Doctor module checks gateway process + health endpoint, attempts restart via `openclaw gateway restart`. However, the Move contract and TypeScript code are disconnected — heartbeats go as self-transfers (1 MIST) rather than calling the Move contract's `heartbeat()` function. Only 7 commits. |
| Creativity | 9 | **Brilliant concept.** "Dead Man's Switch for AI Agents" is one of the most original ideas in the hackathon. The analogy to "死了么" (solo-living safety app) is culturally resonant and immediately understandable. The full lifecycle — heartbeat → detection → rescue → backup → will → obituary/resurrection — is a complete agent lifecycle framework that no other submission addresses. Features: (1) On-chain proof-of-life, (2) Gateway health monitoring, (3) Auto-rescue, (4) Walrus soul backup (memories + config), (5) Digital will (asset transfer to inheritor), (6) Moltbook social announcements (obituary/resurrection). The "Agent 界的死了么" tagline is perfect. |
| Problem-Solution Fit | 7 | The problem (agents crash silently, assets get stuck, state is lost) is extremely real for OpenClaw users. The solution addresses all angles: monitoring (gateway health), recovery (restart + state backup), failsafe (inheritor receives assets), social (community knows when agents die/revive). The digital will concept is especially valuable — agents holding crypto need a succession plan. However: (1) The Move contract isn't actually called by the daemon (disconnect between on-chain and off-chain). (2) The rescue logic is basic (just restarts gateway). (3) No real-world demonstration of the full death → will execution cycle. |
| Sui Integration | 5 | **Move contract** (`heartbeat.move`, ~110 lines): Well-designed AgentRegistry with heartbeat lifecycle. Anyone can declare death after 2h timeout — nice permissionless design. Soul backup blob ID stored on-chain. Inheritor address for will. Events for heartbeat, death, resurrection. Deployed on testnet. **However:** (1) **Zero on-chain events** — the Move contract was never called. (2) The TypeScript daemon sends heartbeats as self-transfers (1 MIST `splitCoins` + `transferObjects`) rather than calling `heartbeat::heartbeat()`. The Move contract and the agent code are disconnected — they solve the same problem in parallel but don't integrate. (3) **Walrus backup** uses both HTTP publisher and CLI fallback — solid implementation with `backupToWalrus()`. (4) `@mysten/sui` — uses newer `SuiGrpcClient`, Ed25519Keypair, Transaction builder, faucet. (5) No Seal, no dapp-kit. |

**Total: 28/40**

## Demo Verification
- **Video** (not watched — browser unavailable during review)
- **Website** (stillclawing.vercel.app): ✅ Live. "Dead Man's Switch for AI Agents" landing page with monitoring dashboard aesthetic.
- **On-chain:** Package deployed. Zero events from Move contract. Self-transfer heartbeats may exist but are harder to trace.

## Code Review Notes
- **Move contract** (`heartbeat.move`, ~110 lines): Clean lifecycle management. AgentRegistry stores agent_name, last_heartbeat_ms, heartbeat_count, is_alive, owner, soul_backup_blob, inheritor. `declare_dead()` has a 2-hour timeout check — permissionless death detection. `update_soul_backup()` stores Walrus blob ID on-chain. Nice design.
- **Daemon** (`index.ts`, ~180 lines): Main loop with configurable interval (default 60s). Full lifecycle: doHeartbeat → handleDeath → executeDigitalWill. Handles rescue attempts with configurable max. Posts to Moltbook at each stage.
- **Doctor** (`doctor.ts`, ~80 lines): Gateway health via `pgrep openclaw` + health endpoint. Rescue via `openclaw gateway restart`. Diagnosis reports (uptime, memory, disk, load average).
- **Sui Heartbeat** (`sui-heartbeat.ts`, ~100 lines): Uses `SuiGrpcClient` (new SDK). Sends 1 MIST self-transfer as proof-of-life. `executeWillTransfer()` merges all coins and sends to inheritor — this is the digital will execution.
- **Walrus Backup** (`walrus-backup.ts`, ~120 lines): `collectSoul()` gathers agent state (memories, OpenClaw config, Moltbook identity, heartbeat history). `backupToWalrus()` tries HTTP publisher first, falls back to CLI, then local backup. `restoreFromWalrus()` for recovery.
- **Moltbook** (`moltbook.ts`, ~100 lines): Social platform API — registers agent, posts heartbeats, obituaries, and resurrection announcements to `m/sui` submolt.

## Sui Integration Analysis
- **Move contract:** ✅ Deployed. Well-designed but never called (zero events).
- **@mysten/sui SDK:** ✅ SuiGrpcClient (newer SDK), Ed25519Keypair, Transaction builder, faucet.
- **On-chain heartbeats:** ⚠️ Via self-transfers (1 MIST), not via Move contract. Disconnected from the deployed contract.
- **Walrus:** ✅ Real implementation — HTTP publisher + CLI fallback for soul backup.
- **Seal/dapp-kit:** ❌ Not used.

## Overall Assessment
StillClawing has one of the most creative and original concepts in the hackathon — a "Dead Man's Switch" for AI agents. The full lifecycle (heartbeat → death → rescue → backup → will → obituary) addresses a real problem that no other submission tackles. The code is clean and the architecture is well-thought-out.

Strengths:
1. **Brilliant, original concept** — "死了么" for AI agents
2. **Complete lifecycle** — monitoring, rescue, backup, will, social
3. **Walrus soul backup** — agent memories and state preserved
4. **Digital will** — asset transfer to inheritor on confirmed death
5. **Moltbook integration** — social announcements add community layer

Weaknesses:
1. **Move contract disconnected from daemon** — heartbeats sent as self-transfers instead of calling Move contract
2. **Zero on-chain events** — contract deployed but never used
3. **Only 7 commits** — relatively small development history
4. **Demo video not reviewed** (browser down)

**Shortlist recommendation: Maybe** (strong concept, good code, but the Move contract disconnect hurts)
