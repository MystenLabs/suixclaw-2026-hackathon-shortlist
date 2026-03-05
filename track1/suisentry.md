# SuiSentry — Audit

## Project Info
| Field | Value |
|-------|-------|
| **DeepSurge ID** | `00a266f2-a02d-4c88-85da-929b27741397` |
| **Name** | SuiSentry |
| **Track** | Safety & Security |
| **GitHub** | https://github.com/Walrus-RFP/SuiSentry |
| **Website** | N/A |
| **Demo Video** | ❌ Wrong video linked (see below) |
| **Package ID** | `0x4ea60657acda50ea3cf89f834a07849c0d6bb20c445a44fa4b08c445059abac9` |
| **Network** | Testnet |
| **Listed** | True |
| **Submitted** | 2026-03-04T06:50:33.130Z |

## Description
SuiSentry is a runtime security sidecar for OpenClaw agents. It intercepts tool calls (shell, browser, wallet, cron), enforces a configurable policy engine, and anchors denied actions to the Sui blockchain as an immutable audit trail. Includes a CLI with panic mode, snapshot hashing, TUI dashboard, and daemon management.

## Eligibility Checklist
- [x] Submitted to DeepSurge
- [ ] Developed by AI agents (or mostly AI agents) — 11 commits, appears AI-assisted (renamed from "ClawVault" to "SuiSentry" in final commit)
- [x] Uses at least one Sui Stack component — Move contract deployed, SDK referenced
- [ ] Working demo verifiable by humans — **Demo video link points to wrong video entirely**
- [ ] Complete DeepSurge profile with wallet address

## Evaluation Scores
| Criteria | Score (1-10) | Notes |
|----------|:------------:|-------|
| Technical Merit | 6 | Well-structured TypeScript monorepo (5 packages: cli, sidecar, policy, sui-client, + Move contract). ~1,457 LOC across the project. Real architectural thinking: sidecar tails gateway logs, policy engine evaluates rules with severity levels, CLI has panic/recover/snapshot/monitor/daemon commands. React-based TUI dashboard (Ink) is a nice touch. However, the sidecar intercepts by *reading log files* rather than actually intercepting tool calls — it's reactive, not preventive. The "quarantine" just writes to an error log, it doesn't actually stop the gateway. 11 commits total. |
| Creativity | 6 | The "security sidecar" concept is well-framed — treating agent security like a SOC with real-time monitoring, policy enforcement, and audit trails. Panic mode with config backup/restore is practical. Security profiles (paranoid/balanced/permissive) are a nice UX pattern. Remote policy sync is forward-thinking. However, several other submissions tackle similar agent-security-with-on-chain-audit-trail concepts. |
| Problem-Solution Fit | 5 | The problem is real (agents with root access need guardrails). The solution addresses it conceptually but has significant gaps in practice: (1) The sidecar reads logs after-the-fact rather than intercepting calls — a malicious action would already have executed by the time it's detected. (2) The "quarantine" doesn't actually stop the gateway. (3) Zero on-chain events means the Sui anchoring was never tested end-to-end. (4) The demo video is wrong, so there's no proof it works. |
| Sui Integration | 3 | Move contract exists and is deployed on testnet — it's a minimal event emitter (AuditEvent with hash, event_type, severity). Compiles cleanly. Package ID resolves on-chain. However: **zero on-chain events** — the contract was never actually called. The TypeScript client shells out to `sui client call` (not SDK programmatic usage). `@mysten/sui` is listed as a dependency but never imported in code — the actual Sui interaction is via CLI exec. No Walrus, no Seal, no dapp-kit, no PTBs. |

**Total: 20/40**

## Demo Verification
- **YouTube link** (`61rC7RgXoq0`): ❌ **WRONG VIDEO.** Links to "LogiSense: Tactile Digital Navigation" by Violina Doley — a completely unrelated project about tactile navigation for the visually impaired. 1:08 long, 3 views. This is a major submission error.
- **No alternative demo** found in repo or DeepSurge profile.
- Demo scripts exist in `demo/` (run-demo.sh, agent-shell.js) but these are local simulations that write fake log lines and watch the sidecar react. Not a real demo of the system protecting a live agent.

## Code Review Notes
- **Monorepo structure** (pnpm workspace): `@suisentry/cli`, `@suisentry/sidecar`, `@suisentry/policy`, `@suisentry/sui-client`
- **Move contract** (`suisentry.move`, ~30 lines): Minimal — single `log_event` function that emits an `AuditEvent`. No shared objects, no access control, no state storage. Events are fire-and-forget.
- **Sidecar** (~250 lines): Tails gateway log files using `chokidar`. Parses lines for keywords (cron.run, system.run, browser, wallet.sign). Classifies severity. Runs through policy engine. On deny: writes to audit log, calls `submitAudit()` for Sui anchoring, and if 3+ denies in 30s, "quarantines" the gateway (writes to error log + sets internal flag).
- **Policy engine** (~100 lines): Loads JSON rules from `~/.openclaw/suisentry.policy.json`. Pattern matching against log lines. Supports allow/deny/ask decisions with severity thresholds. Fallback to hardcoded defaults.
- **CLI** (~400 lines): Full-featured — status, health, init (with security profiles), log viewer, snapshot (config hashing), panic (config lockdown), recover (restore from backup), monitor (TUI), start/stop daemon.
- **Sui client** (`audit.ts`, ~130 lines): Hashes events with SHA-256, calls `sui client call` via `execa` to submit on-chain. Falls back gracefully if env vars not set.
- **Renamed from "ClawVault"** in final commit — visible in TUI which still says "CLAWVAULT".

## Sui Integration Analysis
- **Move contract:** Deployed at `0x4ea60657...` on testnet. Compiles cleanly. Minimal but valid.
- **On-chain activity:** ❌ **Zero events.** Package exists but was never called.
- **SDK usage:** `@mysten/sui` is a dependency but not imported anywhere — actual chain calls go through `sui` CLI binary via `execa`. This is a weaker integration pattern.
- **No Walrus, Seal, or dapp-kit usage.**

## Overall Assessment
SuiSentry has solid architectural thinking and a well-structured codebase for a hackathon project. The monorepo with separate packages for CLI, sidecar, policy, and Sui client shows good software engineering instincts. The feature set (panic mode, security profiles, TUI dashboard, daemon management) is comprehensive on paper.

However, critical weaknesses undermine it:
1. **Wrong demo video** — the YouTube link points to an entirely unrelated project, meaning there's no verifiable demo
2. **Zero on-chain activity** — the Move contract was deployed but never used
3. **Reactive, not preventive** — the sidecar reads logs after actions happen, it doesn't actually block dangerous tool calls
4. **CLI shelling vs SDK** — Sui interaction is via `execa("sui", ...)` rather than programmatic SDK usage

The project feels like it was built quickly with AI assistance (11 commits, renamed from ClawVault at the last minute) and not tested end-to-end.

**Shortlist recommendation: No**
