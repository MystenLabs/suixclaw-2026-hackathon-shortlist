# Injection Hunter — Audit

## Project Info
| Field | Value |
|-------|-------|
| **DeepSurge ID** | `9aaf1a99-b6ce-4e22-aada-3f6d0bc0c51a` |
| **Name** | Injection Hunter |
| **Track** | Track 1: Safety & Security |
| **Team** | pipi333 / pp Cream |
| **GitHub** | https://github.com/pipi333/hackathon-injection-hunter |
| **Demo Video** | https://youtu.be/RpPpsJwOLgI (33s) |
| **Package ID** | None |
| **Network** | Testnet (claimed, not deployed) |

## Problem & Solution
- **What is it?** A multi-layer prompt injection detector — regex patterns (33+), dynamic blacklist, semantic analysis, with a Sui Move contract for on-chain threat registry.
- **What problem does it solve?** Prompt injection attacks can hijack AI agents. This scans inputs before they reach the agent.
- **Who has this problem?** Anyone running AI agents that process untrusted input.
- **Does the solution fit?** The detection side is decent (regex + semantic analysis). But the Sui integration is entirely mocked — commented-out code with "deploy contract" (placeholder) notes everywhere.
- **Would someone use this?** The injection detection could be useful standalone. The blockchain component adds nothing in its current form.

## Eligibility Checklist
- [x] Submitted to DeepSurge
- [ ] Uses at least one Sui Stack component — **NO.** Move contract exists in source but is NOT deployed. Sui integration class is mock code with fake tx digests.
- [x] Working demo (33s video of terminal running test suite)
- [ ] Complete DeepSurge profile with wallet address

## Demo Verification
- **Video:** 33 seconds showing PowerShell running `node dist/demo.js`. Loads 33 regex patterns, runs test suite (Normal Query → low, SQL injection → high, etc). No on-chain interaction.
- **On-chain:** No deployed contract. No package ID. No transactions.

## Code Review Notes
- **Total:** ~1,900 lines TypeScript + 121 lines Move
- **Move contract:** 121 lines — ThreatRegistry with scan proofs and stats tables. Reasonable design but **never deployed**.
- **Sui integration class (414 lines):** All mock code. `submitProofToChain()` generates fake tx digest. `hashString()` uses a primitive JS hash, not SHA-256. Comments say "In production, this would..." (placeholder) everywhere. The actual `@mysten/sui` SDK is never imported.
- **Detection layers:** Regex (343 lines, 33 patterns), semantic analyzer (367 lines, no external LLM), blacklist checker (146 lines). The detection code is the real substance.
- **OpenClaw skill:** 133 lines wrapping the hunter as an agent skill.

## Sui Integration Analysis
- **None functional.** Move contract exists in source but is undeployed. SuiIntegration class generates local hashes and mock tx digests. `@mysten/sui` SDK is never imported or used. Zero on-chain activity.

## Evaluation Scores
| Criteria | Score (1-10) | Notes |
|----------|:------------:|-------|
| Technical Merit | 4 | Decent TypeScript injection detection (~1.9K lines). But the Sui integration is entirely mocked. 33-second demo video. |
| Creativity | 4 | Prompt injection detection is a known problem with known approaches. No novel technique. |
| Problem-Solution Fit | 4 | The detection works locally but the "on-chain threat registry" adds nothing when it's all mock code. |
| Sui Integration | 1 | Zero functional Sui integration. Undeployed contract. Mock tx digests. No SDK usage. |

## Overall Assessment
**Does not meet eligibility criteria.** Injection Hunter has reasonable prompt injection detection code, but the Sui integration is entirely mock/placeholder. The Move contract was never deployed, the SDK is never imported, and the integration class generates fake transaction digests. The demo is 33 seconds of terminal output with no blockchain interaction.

**Shortlist recommendation: No.**
