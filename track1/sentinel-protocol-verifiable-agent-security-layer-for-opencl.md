# Sentinel Protocol: Verifiable Agent Security Layer for OpenClaw on Sui — Audit

## Project Info
| Field | Value |
|-------|-------|
| **DeepSurge ID** | `a38e4a47-d503-4f1c-92b1-be6be46d5d01` |
| **Name** | Sentinel Protocol: Verifiable Agent Security Layer for OpenClaw on Sui |
| **Track** | Safety & Security |
| **GitHub** | https://github.com/dongowu/sentinel-protocol |
| **Website** | https://github.com/dongowu/sentinel-protocol |
| **Demo Video** | https://youtu.be/tpqgaW6TXyI |
| **Package ID** | `0x9ab7b272a0e6c959835ff29e3fdf050dc4c432f6794b8aa54533fefcad985eca` |
| **Network** | Testnet |
| **Submitted** | 2026-02-08T15:39:11.905Z |

## Description
Sentinel is a verifiable pre-execution security layer purpose-built for the OpenClaw + Sui stack. Every action an OpenClaw agent attempts is intercepted by Sentinel's policy gate, scored by a multi-signal risk engine (rule-based + behavioral + semantic), and — when blocked or approved — cryptographically anchored to the Sui blockchain as tamper-evident audit evidence.

## Eligibility Checklist
- [x] Submitted to DeepSurge
- [x] Developed by AI agents (or mostly AI agents) — `.claude/settings.local.json` present
- [x] Uses at least one Sui Stack component (Move contracts + Walrus)
- [x] Working demo verifiable by humans
- [x] Complete DeepSurge profile with wallet address

## Evaluation Scores
| Criteria | Score (1-10) | Notes |
|----------|:------------:|-------|
| Technical Merit | 8 | Genuinely impressive multi-language system: Go server (3375 LOC), 4 Move contracts (748 LOC), Rust CLI (533 LOC), TypeScript OpenClaw plugin (383 LOC). 89 files total, ~5K LOC of real code. 23 Go tests (827 LOC). Architecture is production-grade: policy gate → behavioral detection → hash chain → Merkle batching → Walrus storage → Sui anchoring. Tamper-evident proof chain with SHA-256 chain hashes and binary Merkle tree is well-implemented. Rust CLI handles AES-256-GCM encryption + Ed25519 signing. The behavioral detection engine (agent profiling with novelty scoring) is a real implementation, not just keywords. |
| Creativity | 7 | The "verifiable audit chain" approach — hash chain + Merkle tree + Walrus CID + on-chain anchor — is a more rigorous take than most security submissions. The four-decision model (ALLOW/REQUIRE_APPROVAL/BLOCK/KILL_SWITCH) with one-time execution tokens (30s TTL) and automatic kill-switch trigger on consecutive risk is thoughtful. The Lazarus Protocol (dead man's switch vault) is a creative bonus module. However, the core concept (pre-execution security gate for agent actions) is a common theme in Track 1 — several other submissions do the same thing. The differentiation is in execution quality, not concept novelty. |
| Problem-Solution Fit | 8 | Directly addresses the Track 1 brief: building an immune system for agents with root access. The evidence chain (local hash → Rust signature → Merkle batch → Walrus blob → Sui event) is comprehensive and tamper-evident. The OpenClaw plugin integration is native — `sentinel_gate` tool auto-injects into agent sessions via bootstrap hook, so agents can't bypass the gate. The fail-closed anchor mode (if Sui anchoring fails, block the action) is a strong security design choice. The behavioral detection adds a learning layer beyond static rules. The main weakness: the risk engine's static keyword matching is relatively simple alongside the behavioral layer. |
| Sui Integration | 8 | Four deployed Move modules with real on-chain activity: `sentinel_audit` (core anchoring with Registry + AuditAnchoredEvent), `sentinel_audit_integration` (enhanced records with rule/anomaly dimensions), `community_rules` (on-chain governance with voting), `lazarus_protocol` (dead man's switch). **50+ on-chain AuditAnchoredEvent transactions verified** with varying risk scores (16–100) and both blocked/allowed decisions — this is genuine usage, not just a deploy-and-forget. Walrus integration for Merkle batch storage is implemented in the proof chain. The Go server calls `sui client call` to anchor decisions. Community rules module has on-chain voting with vote power thresholds. Move contracts include unit tests. |

## Demo Verification
- Demo video at https://youtu.be/tpqgaW6TXyI — link is valid
- Extensive evidence directory with JSON artifacts from real CLI sessions: gate blocks, approval confirmations, kill switch arm/disarm, proof chain verification, status dumps
- Evidence includes benchmark results showing risk scoring across multiple test cases
- SHA256SUMS.txt provided for evidence integrity

## Code Review Notes
**Architecture (4 layers):**
1. **Move contracts** (748 LOC, 4 modules): `sentinel_audit` — shared Registry with admin/operator roles, AuditAnchoredEvent emission with policy versioning; `sentinel_audit_integration` — enhanced audit with rule/anomaly tracking, stats queries; `community_rules` — on-chain rule governance with submit/vote/reject lifecycle, vote power thresholds (≥100 power or ≥3 votes to activate); `lazarus_protocol` — dead man's switch with 30-day heartbeat, encrypted blob reference
2. **Go server** (3375 LOC, 23 tests): HTTP gateway (`/sentinel/gate`, `/sentinel/status`, `/sentinel/approval/*`), PolicyGate with behavioral profiling (agent learns normal patterns, scores novel operations higher), kill switch with manual arm and auto-trigger on consecutive blocks, one-time execution tokens with TTL, Merkle-batched proof chain with Walrus upload, Sui on-chain anchoring via `sui client call`, capability sandbox (shell/fs/browser/wallet/network), OpenClaw client integration
3. **Rust CLI** (533 LOC): AES-256-GCM file encryption, Ed25519 audit record signing, deterministic hash computation for audit records, Walrus blob upload/download with encryption
4. **TypeScript OpenClaw plugin** (383 LOC): 3 agent tools (`sentinel_gate`, `sentinel_status`, `sentinel_approval`), bootstrap hook for rule injection, CLI commands (`openclaw sentinel status/gate`), fail-safe design (gate errors default to BLOCK)

**Strengths:**
- Multi-language, multi-layer design is well-integrated
- Proof chain implementation is cryptographically sound (hash chain + Merkle tree + Walrus + Sui)
- Behavioral detection adds learning capability beyond static rules
- OpenClaw plugin is native, not bolted on
- 23 Go tests covering gateway, benchmarks, eval modes, behavioral detection, anchor fail-closed
- Move contracts have unit tests
- Fail-closed anchor mode is a strong security posture

**Weaknesses:**
- Static keyword matching in `SentinelGuard.Evaluate()` is relatively naive (substring matching for "ignore previous", "private key", etc.) — can be bypassed with obfuscation
- No frontend/dashboard — CLI and HTTP API only
- Rust CLI's Walrus integration duplicates the Go server's Walrus upload (two separate implementations)
- Community rules module exists on-chain but no evidence of actual community participation

## Sui Integration Analysis
**Move contracts (4 modules, 748 LOC):**
- `sentinel_audit`: Shared Registry object, admin/operator access control, `record_audit` with Clock timestamp, policy versioning, AuditAnchoredEvent emission
- `sentinel_audit_integration`: Enhanced audit records with rule matching and behavioral anomaly dimensions, stats/query functions, unit tests
- `community_rules`: Full governance lifecycle — submit rules with pattern/category, vote with power thresholds, vote against, automatic status transitions (PENDING → ACTIVE/REJECTED), duplicate vote prevention
- `lazarus_protocol`: Dead man's switch — vault creation, heartbeat keepalive, will execution after 30-day threshold, encrypted blob ID reference

**On-chain verification:**
- Package ID `0x9ab7...85eca` confirmed on testnet with all 4 modules in bytecode
- **50+ AuditAnchoredEvent transactions verified** — varied risk scores (16, 24, 70, 85, 100), both blocked=true and blocked=false decisions
- Real usage patterns — not just test transactions, shows actual gate evaluations being anchored

**Walrus:** Merkle batch upload to Walrus publisher via Go proof chain; Rust CLI supports encrypt-and-store/decrypt flows

## Overall Assessment
Sentinel Protocol is one of the strongest Track 1 submissions. The multi-language architecture (Go + Move + Rust + TypeScript) is ambitious and well-executed, with ~5K LOC of real, purposeful code across 89 files. The cryptographic audit chain (hash → sign → Merkle → Walrus → Sui) is the most rigorous evidence system seen in the hackathon. 50+ real on-chain transactions demonstrate genuine usage, not just deployment. The OpenClaw plugin integration is native and thoughtful.

The main differentiator from other security-gate submissions is the **depth of the evidence layer** — most competitors stop at "evaluate and log," while Sentinel builds a full tamper-evident chain with Merkle batching and on-chain anchoring. The behavioral detection adds a learning dimension.

Weaknesses are the relatively simple static keyword matching (though the behavioral layer compensates) and the lack of a visual dashboard.

**Shortlist: YES** — Strong contender for Track 1 top tier. Deep technical execution, real on-chain usage, native OpenClaw integration.

**Total: 31/40**
