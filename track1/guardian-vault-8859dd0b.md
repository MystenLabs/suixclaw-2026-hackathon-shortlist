# Guardian Vault — Audit

## Project Info
| Field | Value |
|-------|-------|
| **DeepSurge ID** | `8859dd0b-d2b3-429b-a1a9-bb96187aca61` |
| **Name** | Guardian Vault |
| **Track** | Safety & Security |
| **GitHub** | https://github.com/kiprotich-langat/guardian-vault |
| **Website** | https://github.com/kiprotich-langat |
| **Demo Video** | https://youtu.be/CNoNs_p3UKY |
| **Package ID** | N/A — never deployed |
| **Network** | Testnet (claimed) |
| **Listed** | True |
| **Submitted** | 2026-02-10T08:56:16.637Z |

## Description
Guardian Vault claims to protect OpenClaw AI agents from security vulnerabilities. Features prompt injection detection, immutable audit trail (Walrus), encrypted credentials (Seal), execution monitoring, and community governance (Sui Move).

## Eligibility Checklist
- [x] Submitted to DeepSurge
- [ ] Developed by AI agents (or mostly AI agents) — unclear
- [x] Uses at least one Sui Stack component — Move contract exists (undeployed)
- [x] Working demo verifiable by humans — demo video shows CLI running, but key components are simulated
- [ ] Complete DeepSurge profile with wallet address

## Evaluation Scores
| Criteria | Score (1-10) | Notes |
|----------|:------------:|-------|
| Technical Merit | 5 | Comprehensive TypeScript codebase (~2223 lines across 7 source files). Well-structured with separate modules for prompt analysis, execution monitoring, Walrus client, and Seal vault. 30+ regex-based injection patterns. 22 tests (claimed, in test file). The Move contract (378 lines) implements a genuine governance system with proposals, voting, and pattern management. However, Walrus integration is entirely **simulated** (fake blob IDs from hashes), Seal is **local AES-256** (not the actual Sui Seal protocol), and the Move contract was **never deployed**. |
| Creativity | 5 | Community governance for threat patterns is an interesting angle — proposing/voting on threat signatures through on-chain governance. But the core (prompt injection detection via regex) is well-trodden ground. The breadth of claimed features (Walrus + Seal + governance + monitoring) is ambitious but none are actually functional. |
| Problem-Solution Fit | 4 | The submission makes alarming security claims ("93.4% of OpenClaw instances have authentication bypass flaws", "770,000 agents exposed") that appear fabricated — these statistics don't come from real CrowdStrike/Cisco research. Undermines credibility. The prompt analyzer itself works for pattern matching but the broader "vault" system doesn't actually protect anything — simulated Walrus, no Seal, no governance. |
| Sui Integration | 2 | Move contract (378 lines) implements a governance system with proposals, voting tokens, pattern management, and events. **But it was never deployed** — no package ID, zero on-chain activity. Walrus integration is **entirely simulated** — `uploadToWalrus()` returns fake hash-based blob IDs with placeholder comments. "Seal" integration is just local `crypto.createHash` / `crypto.createCipheriv` — not the Sui Seal protocol at all. No Sui SDK usage, no dapp-kit, no real blockchain interaction. |

## Demo Verification
- **YouTube video (1:51, unlisted):** Shows terminal running the demo script — initialization, prompt analysis (safe → allowed, malicious → blocked), command injection prevention, credential storage, file access monitoring, network request filtering. Shows "Demo Completed Successfully". But all Walrus blob IDs shown are simulated (hash-based fakes).
- **Live site:** No frontend — CLI demo only.
- **On-chain verification:** **None.** Move contract was never deployed. No package ID found anywhere in the codebase. Zero on-chain transactions.

## Code Review Notes
- **Move contract (threat_governance.move, 378 lines):** Actually well-structured governance system — GovernanceRegistry (shared object), ThreatProposal (shared objects), VotingToken. Functions: propose_threat_pattern, vote, finalize_proposal, execute_proposal, deactivate/reactivate patterns, admin functions. 5 event types. Proper access control. However, **never deployed**.
- **Prompt Analyzer (prompt-analyzer.ts, 404 lines):** 30+ regex patterns with severity scores. Categories: instruction override, system prompt extraction, command injection, credential access, network exfiltration, SOUL.md persistence, Moltbook attacks. Scoring with confidence levels and three-tier verdict (allow/block/quarantine). Reasonable detection engine.
- **Execution Monitor (execution-monitor.ts, 321 lines):** Monitors shell commands, file access, and network requests against pattern-based rules. Well-structured but runs locally.
- **Walrus Client (walrus-client.ts, 394 lines):** Contains extensive commented-out production code showing what it *would* do, but `uploadToWalrus()` is a **placeholder** that returns `blob_${sha256hash}`. Multiple unfinished comments throughout. `retrieveAuditLogs()` also simulated.
- **Seal Vault (seal-vault.ts, 360 lines):** Uses Node.js `crypto` module for AES-256 encryption. Not the Sui Seal protocol. Comment: "In production, use Seal's key generation". `publicKey` and `privateKey` are the same value.
- **Tests (all-tests.ts, 460 lines):** Comprehensive test definitions but would need to verify they actually run.
- **Red flag:** Submission claims fabricated security statistics attributed to CrowdStrike, Cisco, Giskard, and Trend Micro.

## Sui Integration Analysis
- **Move contract:** Written but never deployed. Zero on-chain activity. ✗
- **Walrus:** Completely simulated — stub placeholders, fake blob IDs. ✗
- **Seal:** Not using Sui Seal protocol — just local Node.js crypto. ✗
- **Sui SDK:** Not used anywhere. ✗
- **dapp-kit:** None. ✗
- **On-chain events:** Zero. ✗

## Overall Assessment
**Overpromises, underdelivers.** Guardian Vault has a broad feature set on paper and reasonably well-written TypeScript code, but the critical integrations are all faked. Walrus uploads return simulated blob IDs. "Seal" is just local AES encryption, not the Sui Seal protocol. The Move governance contract is thoughtfully designed but was never deployed. The submission description makes fabricated security claims attributed to major research firms, which undermines credibility. The only thing that genuinely works is the local prompt injection regex engine — which doesn't need a blockchain.

**Shortlist recommendation: No — key claimed features (Walrus, Seal, governance) are simulated or undeployed. Fabricated statistics are a red flag.**
