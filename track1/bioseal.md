# BioSeal — Audit

## Project Info
| Field | Value |
|-------|-------|
| **DeepSurge ID** | `a61a1414-b8fd-4b9c-bf95-0391edfa25cf` |
| **Name** | BioSeal |
| **Track** | Track 1: Safety & Security |
| **Team** | Hemal V (built by agent "Supervisorbhai") |
| **GitHub** | https://github.com/Hemal-047/Bioseal |
| **Website** | https://bioseal.vercel.app |
| **Demo Video** | https://youtu.be/58mD0tuLzZs (4m38s) |
| **Package ID** | `0xf981df0aa26c4516206c1d62b08abac4327d02ac8ce87210290bfcbb42e1a926` |
| **Network** | Testnet |
| **Submitted** | 2026-02-09 |

## Problem & Solution
- **What is it?** An on-chain security layer for AI agents — pre-execution policy enforcement, cryptographic audit logging to Walrus with Seal encryption, and real-time anomaly detection. A "black box flight recorder" for AI agents.
- **What problem does it solve?** AI agents are getting root access but there's no tamper-proof audit trail of what they do. If an agent goes rogue, you can't prove what happened. There's also no pre-execution guardrail to prevent dangerous actions before they happen.
- **Who has this problem?** Anyone running autonomous AI agents (especially with OpenClaw) who needs accountability, compliance, or security oversight.
- **Does the solution fit?** Yes — the verify→execute→log→detect pipeline is the right architecture. Policy checks before execution + immutable audit trail after = proper safety net. The healthcare demo (Seal-encrypted medical records) is a compelling vertical.
- **Would someone use this?** The concept is sound for enterprise/compliance use cases. The healthcare angle makes it tangible. However, the current implementation is more of a proof-of-concept than a production-ready system.

## Description
BioSeal implements a four-step pipeline for every agent action:
1. **VERIFY** — Check against on-chain policies (rate limits, budgets, kill switch)
2. **EXECUTE** — Only if policy allows
3. **LOG** — SHA-256 hash + Seal encryption + Walrus upload + on-chain record
4. **DETECT** — Real-time anomaly detection (dangerous commands, rate spikes, data exfiltration)

Includes a Health Data Vault demo showing Seal threshold encryption of medical records stored on Walrus, with wallet-based decryption.

## Eligibility Checklist
- [x] Submitted to DeepSurge
- [x] Uses at least one Sui Stack component (Move + Walrus + Seal + dapp-kit)
- [x] Working demo verifiable by humans (4m38s video + live site)
- [ ] Complete DeepSurge profile with wallet address

## Demo Verification
- **Video:** 4m38s comprehensive walkthrough of the live dashboard at bioseal.vercel.app:
  1. **Get Started tab** — overview with stats (1 agent, 5 actions, 0 denied, 1 anomaly), pipeline diagram ✅
  2. **Audit Trail tab** — live on-chain logs showing ALLOWED/FLAGGED actions with action hashes, Walrus blob IDs, and "Decrypt (Seal)" buttons ✅
  3. **Health Data Vault** — encrypt medical data (Blood Test, Wearable, Prescription, Genomic templates), upload to Walrus, decrypt with wallet signature ✅
  4. **Decryption verified** — badges showing "Decryption verified by Seal key servers", "Access logged on-chain", "Walrus blob preserved" ✅
  5. **Anomaly detection** — "Dr. AI-Med requests blood test → ALLOWED" vs "Research Agent bulk exports history → FLAGGED" ✅
  - Wallet connected throughout demo. Real data visible.
- **Live site:** https://bioseal.vercel.app — accessible without wallet for read-only view, wallet needed for Health Demo encryption/decryption
- **On-chain:** 20+ transactions on testnet from 20 days ago — `register_agent`, `verify_action` (×7), `log_step` (×5), `flag_anomaly` (×4), `log_denial` (×2). Significant on-chain activity proving real usage.

## Code Review Notes
- **Move contracts:** 541 lines (bioseal.move) with 3 modules: agent_audit, agent_policy, health_data. Proper struct definitions, events, access control, policy enforcement.
- **Frontend:** ~2,100 lines React/TypeScript. Components for AuditTrail, AgentRegistry, AnomalyDashboard, PolicyManager, HealthDemo, ReputationBadge. Uses useSeal hook for encryption.
- **Agent Skill:** bioseal-agent.js (verify→log→detect pipeline) with SKILL.md for OpenClaw integration
- **Build Log:** Detailed BUILD_LOG.md showing the agent (Supervisorbhai) building the project in phases over 2026-02-09

## Sui Integration Analysis
- **Move smart contracts** — 3 modules on testnet: agent_audit (registration, step logging, anomaly flagging), agent_policy (rate limits, budgets, kill switch), health_data
- **Seal** — Threshold encryption for health data records. `useSeal` hook in frontend. Wallet-based decryption with on-chain verification.
- **Walrus** — Encrypted blobs stored on Walrus with blob IDs logged on-chain. Real Walrus uploads visible in audit trail.
- **@mysten/dapp-kit** — Wallet connection, transaction signing
- **Sui Events** — StepLogged, AnomalyFlagged, ActionDenied events for the audit trail
- **Uses 4 Sui stack components** (Move, Seal, Walrus, dapp-kit) — one of the broadest integrations in Track 1

## Evaluation Scores
| Criteria | Score (1-10) | Notes |
|----------|:------------:|-------|
| Technical Merit | 7 | Solid Move contracts, working frontend with Seal/Walrus integration. But Move code is straightforward (no complex crypto or advanced patterns), and frontend is ~2K lines. Good but not exceptional depth. |
| Creativity | 8 | "Black box flight recorder" framing is compelling. Healthcare vertical with Seal encryption is a smart demo. Pipeline architecture (verify→log→detect) is well-designed. |
| Problem-Solution Fit | 8 | Directly addresses agent safety with the right architecture. Policy enforcement + immutable audit trail is the correct approach. Healthcare demo makes it tangible but is a bit disconnected from the core agent safety pitch. |
| Sui Integration | 8 | Uses Move + Seal + Walrus + dapp-kit — broad integration. Real on-chain activity (20+ transactions). Seal encryption for health data is a genuine use case, not just a checkbox. |

## Concerns
- Testnet only — no mainnet deployment
- Healthcare demo, while impressive, feels somewhat separate from the core "agent safety" pitch
- No Move tests in the repo (only build artifacts)
- The anomaly detection appears to be frontend logic, not on-chain enforcement
- Agent skill (bioseal-agent.js) is relatively simple

## Overall Assessment
**Good Track 1 project.** BioSeal hits the right notes for the safety track — pre-execution policy checks, tamper-proof audit logging, anomaly detection. The Seal + Walrus integration for encrypted health data is one of the best demonstrations of those technologies in the hackathon. The demo video is thorough and the live site works. The on-chain footprint is substantial (20+ transactions).

Weaknesses: testnet only, Move contracts are straightforward rather than sophisticated, and the anomaly detection is more UI-level than on-chain enforcement. The healthcare vertical is compelling but slightly disconnected from the agent safety narrative.

**Shortlist recommendation: Yes — solid candidate for top 10 in Track 1.**
