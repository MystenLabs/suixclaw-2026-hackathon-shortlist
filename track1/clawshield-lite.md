# ClawShield Lite — Audit

## Project Info
| Field | Value |
|-------|-------|
| **DeepSurge ID** | `81d81c24-0a5f-4ff9-8567-75991c85a321` |
| **Name** | ClawShield Lite |
| **Track** | Safety & Security |
| **GitHub** | https://github.com/DimitrisTheo-Dev/clawshield_lite |
| **Website** | https://github.com/DimitrisTheo-Dev/clawshield_lite |
| **Demo Video** | https://www.loom.com/share/e43815d663c44e67b7c1c0d775a913fe |
| **Package ID** | `0x53c0acb829e2f9cb9ababb323bf55e9992bf0b09cfce34238c0a5c3558842f1e` |
| **Network** | Devnet |
| **Submitted** | 2026-02-08T17:16:02.372Z |

## Description
ClawShield Lite is a local-first safety layer for high-privilege AI agents. It scans untrusted inputs for prompt injection and social engineering, assigns deterministic verdicts (ALLOW/SANITIZE/BLOCK), and emits tamper-evident receipts. On-chain receipts via Sui Move events and optional Walrus blob logging for extended forensics.

## Eligibility Checklist
- [x] Submitted to DeepSurge
- [x] Developed by AI agents (or mostly AI agents) — AI_BUILD_LOG.md documents the process
- [x] Uses at least one Sui Stack component — Move contract + Walrus integration
- [x] Working demo verifiable by humans — 5-minute Loom video showing CLI in action
- [x] Complete DeepSurge profile with wallet address

## Evaluation Scores
| Criteria | Score (1-10) | Notes |
|----------|:------------:|-------|
| Technical Merit | 6 | Well-structured CLI tool (~1168 lines TS across 15 files). Clean architecture: normalize → rules engine → receipt assembly → optional Sui/Walrus sinks. Policy-driven detection with configurable thresholds, substring + regex matching, risk scoring with bonuses. Includes OpenClaw skill integration (SKILL.md). Good documentation (ARCHITECTURE.md, THREAT_MODEL.md, SECURITY.md). However, the detection engine is relatively simple — substring matching and basic regex, no ML or semantic analysis. |
| Creativity | 5 | Prompt injection detection for agent inputs is a well-understood problem space. The three-tier verdict system (ALLOW/SANITIZE/BLOCK) with deterministic, auditable receipts is a reasonable approach. The "local-first scanner with optional on-chain auditability" framing is sensible but not particularly novel. Several other submissions tackle similar territory. |
| Problem-Solution Fit | 6 | Real problem — agents consuming untrusted content need guardrails. The deterministic approach (no LLM in the loop) is a defensible design choice for a security tool. The sanitization path is practical. However, substring matching has obvious bypass vectors (obfuscation, paraphrasing, encoding). The tool would benefit from more sophisticated detection for production use. |
| Sui Integration | 4 | Move contract is minimal — single `record_receipt` entry function that emits a `ReceiptEmitted` event with scan metadata. No on-chain state, no objects, no access control. Deployed on devnet (which resets), and devnet package is now gone. Walrus integration via CLI wrapper (writes receipt JSON as blob). Both Sui and Walrus are optional and were skipped in the demo. The Sui integration is a logging sink, not core to the product. |

## Demo Verification
- **Loom video (5:00):** Real demo showing the developer running `./demo.sh` which builds the CLI and scans three sample files: benign.txt → ALLOW, ambiguous.txt → SANITIZE, malicious.txt → BLOCK. Shows the code editor with sample files visible. Walrus and Sui posting skipped (env vars not set). Also shows the repo structure and explains the architecture.
- **Live site:** No frontend — CLI tool only. GitHub repo is accessible and matches the demo.
- **On-chain verification:** Package was on devnet which has since reset — object no longer exists. Zero verifiable on-chain events. Walrus posting also not demonstrated.

## Code Review Notes
- **Move contract (33 lines):** Extremely minimal. Single `record_receipt` entry function that takes scan metadata (content_hash, policy_hash, verdict, risk_score, etc.) and emits a `ReceiptEmitted` event. No stored objects, no access control, no complex logic. Essentially an event logger.
- **CLI (TypeScript, ~1168 lines):**
  - `rules_engine.ts` (101 lines): Core scanning — substring matching + regex per rule, risk score calculation with bonuses, verdict based on configurable thresholds.
  - `sui.ts` (236 lines): Sui CLI wrapper — publishes Move package, records receipts by calling the on-chain function. Uses `spawnSync("sui", ...)` to invoke the Sui CLI rather than the SDK.
  - `walrus_cli.ts` (202 lines): Walrus CLI wrapper — stores receipt JSON as blobs. Also uses `spawnSync("walrus", ...)`.
  - `scan.ts` (125 lines): Orchestrates the scan pipeline — evaluate content, optionally post to Walrus, optionally post to Sui.
  - Good separation of concerns, clean TypeScript, proper error handling.
- **Policy (policy.json):** 5 detection rules: override attempts, secret harvesting, wallet signing, command execution, self-modification. Each with substring patterns and severity scores. Configurable thresholds (block ≥ 70, sanitize ≥ 40).
- **Documentation:** Excellent — ARCHITECTURE.md (data flow diagram), THREAT_MODEL.md (concrete attacks), SECURITY.md, AI_BUILD_LOG.md, repo layout in README.
- **OpenClaw Skill integration:** Includes a SKILL.md for agent integration, explaining how to use scan verdicts in agent workflows.
- **Notable:** Uses Sui CLI and Walrus CLI via `spawnSync` rather than SDK — functional but less elegant.

## Sui Integration Analysis
- **Move contract:** Deployed (devnet, now gone). Minimal event emitter — no objects, no on-chain state. ✗
- **Sui CLI wrapper:** Calls `sui client call` to record receipts. Not SDK-based. Partial ✓
- **Walrus CLI wrapper:** Calls `walrus store` to save receipts. Not SDK-based. Partial ✓
- **On-chain activity:** Zero verifiable events (devnet reset). Neither Sui nor Walrus were used in the demo. ✗
- **dapp-kit:** None (CLI tool, no frontend) ✗
- **Overall:** Sui is an optional audit sink, not integral to the product's functionality.

## Overall Assessment
**Competent but shallow Sui integration.** ClawShield Lite is a well-engineered CLI tool with clean architecture, good documentation, and a working demo. The deterministic scanning approach with auditable receipts is sound. However, the Move contract is trivially simple (just an event emitter), both Sui and Walrus integrations are optional and weren't demonstrated, and the package was deployed on devnet (now gone). The core value proposition — prompt injection detection — works entirely offline and doesn't need a blockchain. The Sui integration feels bolted on rather than essential.

**Shortlist recommendation: Borderline no — well-documented and competently built, but Sui integration is too shallow for Track 1 top 10.**
