# clawguard (ClawDefender) — Audit

## Project Info
| Field | Value |
|-------|-------|
| **DeepSurge ID** | `b861f6d4-abaf-401e-ba7f-b73fcc50587d` |
| **Name** | clawguard |
| **Track** | Safety & Security |
| **GitHub** | `https://github.com/jayjoshix/clawdefender` |
| **Website** | `https://clawdefender.vercel.app/` |
| **Demo Video** | N/A |
| **Package ID** | `0x5379bf93b2b4733478e126f377d43b4cdc69ef6de7d7d163412fd3a0007c3fb2` |
| **Network** | Testnet |
| **Listed** | True |
| **Submitted** | 2026-03-02T18:30:30Z |

## Description
ClawGuard is an immune system for root-capable local agents (like OpenClaw). It forces every action through a Policy Firewall, requires Signed Human Approvals for risky tools, and maintains a Tamper-Evident Log Chain anchored on Sui. Actions are hashed, encrypted (Seal), stored permanently (Walrus), and anchored on-chain (Sui Receipt).

## Eligibility Checklist
- [x] Submitted to DeepSurge
- [x] Developed by AI agents (or mostly AI agents) — code structure suggests AI-assisted
- [x] Uses at least one Sui Stack component — Move (Seal policy), Walrus bundler, SDK
- [x] Working demo verifiable by humans — on-chain receipt `0x2764f514...` verifiable
- [x] Complete DeepSurge profile with wallet address

## Evaluation Scores
| Criteria | Score (1-10) | Notes |
|----------|:------------:|-------|
| Technical Merit | 7 | ~7800 LOC TypeScript across well-structured packages: `packages/clawguard` (policy evaluator, hash-chain logging, approval system, bundler, server, Telegram integration, tool wrappers), `packages/openclaw-adapter` (OpenClaw integration with Telegram e2e, sign-approval). Move contract for Seal-based access control. Comprehensive feature set: YAML-based policy engine with glob matching, nonce-based replay resistance, hash-chain tamper-evident logs, expiry enforcement (300s TTL), signed human approvals. Tests for hash-chain and policy evaluator. E2E logs committed. Dockerfile for deployment. |
| Creativity | 7 | "Immune system for agents" is a strong metaphor executed well. The combination of policy firewall + signed human approvals (via Telegram) + tamper-evident hash-chain + Seal encryption + on-chain anchoring creates a layered defense. Nonce-based replay resistance and fail-closed log verification on startup are thoughtful security details. |
| Problem-Solution Fit | 7 | Directly addresses the risk of root-capable agents. The YAML policy system (allow/deny by tool + pattern) is practical for real OpenClaw deployments. Telegram-based human approval for risky operations is a clever UX choice. The threat model documentation shows security-first thinking. |
| Sui Integration | 6 | Move contract (`seal_policy`) with `AccessCap` and `SessionReceipt` structs. `seal_approve_access` function follows Seal's ownership-based access control pattern. `SessionReceipt` anchors session data on-chain (session_id, policy_sha256, final_log_hash, walrus_blob_id, bundle_sha256). Bundler in `packages/clawguard/src/bundler/` handles Walrus upload + Sui anchoring. Demo output shows verifiable receipt `0x2764f514...`. However, zero on-chain events detected via RPC query — the receipt may exist as an object but wasn't captured in event queries. |

## Demo Verification
- **GitHub:** Public repo with 95 files, well-organized monorepo.
- **On-chain:** Package exists on testnet. Zero events detected (receipt may be object-based, not event-emitting). README provides verifiable receipt ID `0x2764f514d173c3cb2671607f2409745e691238914092b724597b8f041b376511`.
- **Website:** Vercel deployment at `clawdefender.vercel.app`.
- **E2E logs:** Three sets of e2e logs committed (`logs-e2e-177048...`), showing real execution traces.
- **Demo output log:** `demo-output.log` committed.

## Code Review Notes
- **Architecture:**
  - `packages/clawguard/src/policy/`: YAML-based policy evaluator with schema validation, glob matching for tool+argument patterns
  - `packages/clawguard/src/logging/`: SHA256 hash-chain for tamper-evident action logs. `verifyLogChain()` runs on startup — fail-closed if tampered
  - `packages/clawguard/src/approval/`: Signed human approval system with nonce tracking, expiry enforcement (MAX_APPROVAL_TTL 300s)
  - `packages/clawguard/src/server/`: HTTP server + Telegram bot for approval requests
  - `packages/clawguard/src/bundler/`: Proof bundling for Walrus upload + Sui anchoring
  - `packages/clawguard/tools/`: Tool wrappers (browser, shell) that enforce policy
  - `packages/openclaw-adapter/`: OpenClaw integration with Telegram e2e testing
- **Move contract:** Clean Seal-compatible design with `AccessCap` (decrypt permission) and `SessionReceipt` (audit record). Test scaffolding included.
- **Security properties:** Nonce-based replay resistance, TTL-bounded approvals, hash-chain integrity verification, Seal encryption for bundles.
- **Testing:** Unit tests for hash-chain and policy evaluator. Integration tests for Telegram approval flow. E2E wrapper scripts.

## Sui Integration Analysis
- **Move contract:** Deployed, Seal-compatible access control pattern ✓
- **Seal:** `seal_approve_access` gate function, `AccessCap` for encrypted bundle access ✓✓
- **Walrus:** Bundler uploads proof bundles, `SessionReceipt` stores `walrus_blob_id` ✓
- **SDK:** Used in bundler and demo scripts ✓
- **On-chain activity:** Receipt object claimed but no events emitted — partial ✓

## Overall Assessment
**Solid security-focused submission with comprehensive architecture.** ClawGuard demonstrates real security thinking: policy-based firewalling, signed human approvals via Telegram, hash-chain tamper evidence, Seal encryption, and on-chain anchoring. The 7800 LOC codebase is well-structured with proper testing. The Seal integration is one of the better implementations in this hackathon. Main weakness: zero on-chain events detected and the receipt verification needs manual checking.

**Shortlist recommendation: YES — well-architected security system with Seal integration, hash-chain logging, and signed approval flow.**
