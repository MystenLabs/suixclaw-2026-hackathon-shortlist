# Shield Claw — Audit

## Project Info
| Field | Value |
|-------|-------|
| **DeepSurge ID** | `c82a8620-a6eb-4a82-80f6-51e4f85a93e4` |
| **Name** | Shield Claw |
| **Track** | Track 1: Safety & Security |
| **GitHub** | https://github.com/mememan-anon/ShieldClaw |
| **Website** | https://shield-claw.vercel.app/ |
| **Demo Video** | https://youtu.be/wD-G8jbDW7k |
| **Package ID** | `0x5921b2d8e7a8da8d84dda83682fadf130cf7195691109020bcad5e9983f94dcf` |
| **Network** | Devnet |
| **Submitted** | 2026-02-13T04:34:26.662Z |

## Problem & Solution
- **What is it?** A security layer for AI agents combining prompt injection defense, skill verification, runtime monitoring, and on-chain security logging via Sui Move contracts.
- **What problem does it solve?** AI agents executing arbitrary skills are vulnerable to prompt injection, unauthorized code execution, and invisible abuse. Security incidents need tamper-proof audit trails.
- **Who has this problem?** Anyone deploying autonomous AI agents that run tools/skills in production environments.
- **Does the solution fit?** Yes — defense-in-depth with detection, verification, monitoring, and on-chain logging covers the major threat surface for agent security.
- **Would someone use this?** Plausibly. The architecture is well-thought-out with real OpenClaw integration hooks. The prompt injection detector and skill verifier have practical utility.

## Description
Multi-layered security framework: prompt injection detector (pattern + heuristic analysis), skill code verifier (hash integrity, security pattern scanning), runtime behavior monitor (CPU/memory/network anomaly detection), and Sui blockchain logging for tamper-proof audit trails. Includes React dashboard for visualization, governance contracts for policy management, and OpenClaw skill hooks.

## Eligibility Checklist
- [x] Submitted to DeepSurge
- [x] Developed by AI agents (or mostly AI agents) — Multiple iterative commits suggest AI-assisted development
- [x] Uses at least one Sui Stack component — Move contracts deployed to devnet + Walrus blob references
- [x] Working demo verifiable by humans — Live Vercel dashboard + demo video
- [ ] Complete DeepSurge profile with wallet address

## Demo Verification
- **Video:** YouTube link provided (https://youtu.be/wD-G8jbDW7k)
- **Website:** https://shield-claw.vercel.app/ — live React dashboard with monitoring charts, event feed, stats grid, health cards, and interactive demo pages (CodeScanner, BlockchainLogger, PromptTester)
- **On-chain:** Package ID `0x5921b...94dcf` deployed to Sui devnet. Confirmed via .env-example with registry, event log, and certificate registry object IDs. The SuiBlockchainClient in code builds and signs real transactions using `@mysten/sui` SDK.
- **Walrus:** EventBatch struct in Move contract stores `walrus_blob_id` for batch event storage.

## Code Review Notes
- **Repo structure:** Backend (Node.js), frontend (React + Vite), contracts (Move), tests, demos
- **Lines of code:** ~11,003 total. Substantial codebase across 60+ source files.
- **Move contracts (4 files, ~600+ lines):**
  - `security_events.move` — SecurityEvent records, EventLog with append-only counter, EventBatch with Walrus blob references. Clean struct design.
  - `governance.move` — Full governance system: proposals, voting, quorum, timelock, security policies. Well-structured with proper access control.
  - `verification.move` — Skill attestation, execution attestation, verification certificates, attestation chains. Hash verification. Certificate registry with revocation.
  - `skill_reputation.move` — Skill reputation tracking with execution stats, security incident recording, score adjustments, trust/safe thresholds.
  - **Quality:** Comprehensive on-chain security framework. 4 contracts covering events, governance, verification, and reputation. Proper error handling, access control, and Sui patterns.
- **Backend (~5,000+ lines):**
  - Defense layer: PromptInjectionDetector (pattern + heuristic), InputSanitizer, Defense orchestrator — multi-method detection with scoring
  - Skill verifier: Hash integrity checking, security pattern scanning
  - Container/executor: Sandboxed execution with eBPF monitoring stubs
  - Blockchain client: Full `@mysten/sui` SDK integration — SuiClient, Transaction building, Ed25519Keypair signing, event logging, reputation recording, attestation creation, event querying
  - OpenClaw hooks: SecurityHooks and ExecutionHooks for pre/post skill execution
  - API server with monitoring endpoints
- **Frontend (~1,500 lines):** React dashboard with SSE-based real-time updates, monitoring charts, interactive demo pages (CodeScanner, BlockchainLogger, PromptTester)
- **Tests:** Both unit and integration test files. Integration tests verify Verify→Sanitize workflow, OpenClaw hooks lifecycle, and defense pipeline.
- **Git history:** 10 commits showing iterative development — contract deployment, scoring fixes, testing finalization. Indicates real development process.

## Sui Integration Analysis
- **Move contracts** — 4 contracts deployed to devnet. Comprehensive on-chain security framework covering event logging, governance, verification, and reputation.
- **@mysten/sui SDK** — Full integration in SuiBlockchainClient: transaction building, signing, event logging, reputation tracking, attestation creation, event querying. Graceful fallback to local hashing when package not available.
- **Walrus** — EventBatch references Walrus blob IDs for batch event storage. Verification module stores walrus_blob_id in attestation records.
- **On-chain state:** .env-example provides real object IDs for registry, event log, and certificate registry on devnet.
- **Net assessment:** This is one of the more thorough Sui integrations in Track 1. Real deployed contracts, real SDK usage with transaction signing, and Walrus references for data storage. The governance and attestation systems go beyond basic logging.

## Evaluation Scores
| Criteria | Score (1-10) | Notes |
|----------|:------------:|-------|
| Technical Merit | 7 | ~11K lines, 4 Move contracts, multi-layered defense system, tests, React dashboard. Substantial engineering effort with real architecture. |
| Creativity | 7 | Defense-in-depth for agent security with on-chain governance and attestation chains is well-conceived. The governance + reputation layer goes beyond basic security logging. |
| Problem-Solution Fit | 7 | Addresses real agent security concerns comprehensively — detection, verification, monitoring, and audit trail. The eBPF monitoring is stubbed but the architecture is sound. |
| Sui Integration | 7 | 4 contracts deployed on devnet with real SDK transaction building. Governance, attestation chains, and reputation scoring on-chain. Walrus blob references. Only devnet (not testnet/mainnet) limits the score slightly. |

## Overall Assessment
**Solid Track 1 contender.** ShieldClaw is one of the more comprehensive security-focused submissions. It goes beyond just prompt injection detection to include on-chain governance, skill attestation chains, and reputation tracking. The 4 Move contracts are well-designed, the backend has real detection logic (not just regex), and the Sui SDK integration is functional with proper transaction building.

Strengths: depth of architecture, governance system, iterative git history showing real development, deployed contracts, comprehensive test coverage. Weaknesses: devnet only (not testnet/mainnet), eBPF monitoring is stubbed, and the prompt injection detection is still primarily pattern-based (no ML/semantic analysis).

**Shortlist recommendation: Yes — competitive in Track 1 upper tier.**
