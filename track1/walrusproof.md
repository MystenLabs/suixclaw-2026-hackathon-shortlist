# WalrusProof — Audit

## Project Info
| Field | Value |
|-------|-------|
| **DeepSurge ID** | `615cca7e-96c1-458e-8be7-f2338cdbfdcb` |
| **Name** | WalrusProof |
| **Track** | Track 1: Safety & Security |
| **GitHub** | https://github.com/obseasd/walrus-proof |
| **Website** | https://github.com/obseasd/walrus-proof |
| **Demo Video** | https://youtu.be/Iu0WBhT6d8I |
| **Package ID** | `0xb9d87d8952e3bad53a1538d8bf5c262fc796c5416be6eeaf8800261b18c521d6` |
| **Network** | Testnet |
| **Submitted** | 2026-02-12T12:36:57.798Z |

## Problem & Solution
- **What is it?** Cryptographic proof-of-reasoning middleware for AI agents. Creates a hash-linked chain of proof records for every agent action, encrypted via Seal (AES-256-GCM), stored on Walrus, and anchored on Sui via Move contract. Plus a multi-layer prompt injection firewall.
- **What problem does it solve?** When AI agents go rogue or make bad decisions, there's no audit trail. WalrusProof creates an immutable, verifiable, tamper-proof trace of every decision.
- **Who has this problem?** Anyone deploying autonomous agents in high-stakes environments (finance, infrastructure) who needs accountability and auditability.
- **Does the solution fit?** Yes — hash-linked proof chains with on-chain anchoring and encrypted blob storage provide genuine tamper-proof audit trails. The prompt firewall adds a prevention layer.
- **Would someone use this?** The proof chain concept is genuinely useful for agent accountability. The combination of Sui anchoring + Walrus storage + Seal encryption addresses a real gap in the agent security stack.

## Description
Python middleware with three pillars: (1) ProofEngine — builds hash-linked chains of action proofs (SHA-256), each proof records input/output hashes, timestamps, and chain position; (2) PromptFirewall — multi-method injection detection (14+ patterns, delimiter analysis, entropy analysis, Unicode homograph detection); (3) On-chain anchoring — Move contract stores proof chain state, Walrus stores encrypted proof data, Sui events for indexing. Includes Seal encryption client and audit report generation.

## Eligibility Checklist
- [x] Submitted to DeepSurge
- [x] Developed by AI agents (or mostly AI agents) — Single commit, likely AI-generated
- [x] Uses at least one Sui Stack component — Move contract deployed to testnet + Walrus + Seal
- [x] Working demo verifiable by humans — demo.py generates full audit report with chain verification
- [ ] Complete DeepSurge profile with wallet address

## Demo Verification
- **Video:** YouTube link provided (https://youtu.be/Iu0WBhT6d8I)
- **On-chain:** Package `0xb9d87d...521d6` deployed to Sui testnet. Published.toml confirms deployment with chain-id `4c78adac`, toolchain 1.65.2.
- **Audit report:** `audit_report.json` in repo shows a completed demo run: 12 actions, chain_valid=true, 12 proofs verified. Firewall stats: 7 checks, 3 blocked, 2 suspicious, 2 safe. Each proof has unique IDs, proper hash chaining, and timestamps.
- **Proof chain verification:** ProofEngine.verify_chain() confirms hash chain integrity — genesis hash → sequential position check → prev_hash linkage. Both in-memory and exported chain verification methods.

## Code Review Notes
- **Repo structure:** Python project — proof_engine.py, prompt_firewall.py, sui_client.py, walrus_client.py, seal_client.py, middleware.py, cli.py, demo.py, contracts/
- **Lines of code:** ~14,629 total (mostly build artifacts). Actual source: ~2,500+ lines Python + 132 lines Move.
- **Move contract (1 file, 132 lines):**
  - `proof_chain.move` — ProofChain (shared object) per agent: proof_count, latest_action_hash, latest_walrus_blob_id. ProofRecord (shared objects) with chain_id, position, action_hash, walrus_blob_id, prev_action_hash. Events: ChainCreated, ProofAnchored, InjectionDetected.
  - **Quality:** Well-designed for the use case. Shared objects enable multi-party verification. The InjectionDetected event ties security monitoring to on-chain audit. Hash chain maintenance is correct.
- **Python source (~2,500+ lines):**
  - `proof_engine.py` (~150 lines) — Core proof chain logic. SHA-256 hash linking, genesis hash, chain position tracking, verify_chain() with comprehensive integrity checks, export/import with static verification. Clean and correct.
  - `prompt_firewall.py` (~200+ lines) — Multi-layer detection: 14 regex patterns with weighted scores, 5 delimiter injection patterns, entropy analysis for obfuscated payloads, Unicode homograph detection. ThreatLevel enum (safe/suspicious/blocked) with configurable thresholds. Statistics tracking.
  - `sui_client.py` (~180+ lines) — Sui JSON-RPC client with chain state reading, object queries, balance checks. Hardcoded package ID matching Published.toml.
  - `walrus_client.py` (~100+ lines) — Walrus blob store/read via publisher/aggregator APIs.
  - `seal_client.py` (~150+ lines) — AES-256-GCM encryption for proof data before Walrus upload.
  - `middleware.py` (~200+ lines) — Orchestration layer combining all components.
  - `demo.py` (~170+ lines) — Full demo pipeline generating audit report.
  - `cli.py` (~190+ lines) — Command-line interface.
- **Dependencies:** requests, cryptography, pyyaml, pytest. No Sui Python SDK — raw RPC.
- **Single git commit** — same author as SuiPilot (obseasd). Both projects share similar structure/toolchain.

## Sui Integration Analysis
- **Move contract** — 1 contract deployed to testnet. Proof chain anchoring with hash linkage, Walrus blob references, injection detection events. Verified via Published.toml.
- **Sui RPC** — JSON-RPC calls for object queries and chain state reading.
- **Walrus** — Real integration for encrypted proof blob storage. Store and read via publisher/aggregator APIs.
- **Seal** — AES-256-GCM encryption client for proof data. (Note: this is a custom implementation, not the Sui Seal protocol, but provides real encryption.)
- **Transaction execution** — Like SuiPilot, the SuiClient is primarily read-focused. Transaction building is referenced but signing is not fully implemented.
- **Net assessment:** Three Sui stack components (Move, Walrus, Seal-style encryption). Contract deployed and verified. The proof chain concept maps well to Sui's object model (shared objects for multi-party verification).

## Evaluation Scores
| Criteria | Score (1-10) | Notes |
|----------|:------------:|-------|
| Technical Merit | 6 | ~2,500+ lines with solid architecture. Proof engine with hash chain verification is well-implemented. Multi-layer firewall goes beyond basic regex. Encryption client adds real security value. |
| Creativity | 7 | Proof-of-reasoning chains for AI agents is a strong concept. Combining hash-linked proofs + Walrus storage + on-chain anchoring + Seal encryption is a thoughtful security stack. |
| Problem-Solution Fit | 7 | Agent accountability is a real and growing problem. Hash-linked proof chains with on-chain anchoring genuinely address the "what did the agent do and why" question. The prompt firewall adds prevention. |
| Sui Integration | 6 | Deployed testnet contract, Walrus storage, encryption layer. Three stack components. But transaction signing not fully implemented — proofs can't be autonomously anchored on-chain yet. |

## Concerns
- Same author (obseasd) as SuiPilot — both submitted within 6 minutes of each other, both have single commits. These appear to be parallel submissions from the same developer.
- Transaction execution gap means the full pipeline (detect → encrypt → store on Walrus → anchor on Sui) can't run end-to-end autonomously.
- The "Seal" encryption is a custom AES-256-GCM implementation, not the actual Sui Seal protocol.

## Overall Assessment
**Solid concept with good execution for Track 1.** WalrusProof's proof-of-reasoning chain is one of the more thoughtful approaches to agent accountability in the hackathon. The architecture is sound: hash-linked proofs provide tamper detection, Walrus provides decentralized storage, Sui provides immutable anchoring, and encryption protects sensitive reasoning data.

The prompt firewall is above average — 14+ patterns, delimiter analysis, entropy checking, and Unicode homograph detection is more sophisticated than most submissions. The proof engine's chain verification is clean and correct.

The main weaknesses are: (1) transaction signing not fully implemented, so proofs can't be autonomously anchored; (2) same author as SuiPilot raises questions about development time allocation; (3) custom encryption vs actual Seal protocol.

**Shortlist recommendation: Borderline yes — competitive in the middle tier of Track 1. The proof chain concept has genuine merit.**
