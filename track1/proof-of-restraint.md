# proof-of-restraint — Audit

## Project Info
| Field | Value |
|-------|-------|
| **DeepSurge ID** | `8a206441-7de2-400b-98bb-71078214da1c` |
| **Name** | proof-of-restraint |
| **Track** | Safety & Security |
| **GitHub** | `https://github.com/Albert0919/proof-of-restraint` |
| **Website** | N/A |
| **Demo Video** | N/A |
| **Package ID** | `0x79fd958c0b53a659913afc49cae307b897287ffd1c7da6432b5635b34826b4de` (claimed, not found on testnet) |
| **Network** | Devnet (based on log evidence) |
| **Listed** | True |
| **Submitted** | 2026-03-02T12:39:43.217Z |

## Description
Instead of only proving execution, this project proves safe refusal. For risky requests, it outputs ALLOW | CHALLENGE | REJECT with risk reasons, stores full payload on Walrus, and anchors decision hash on Sui.

## Eligibility Checklist
- [x] Submitted to DeepSurge
- [x] Developed by AI agents (or mostly AI agents) — code structure suggests AI-assisted
- [x] Uses at least one Sui Stack component — real Sui SDK + Walrus publisher client code
- [ ] Working demo verifiable by humans — evidence not verifiable (devnet reset + Walrus blob expired)
- [x] Complete DeepSurge profile with wallet address

## Evaluation Scores
| Criteria | Score (1-10) | Notes |
|----------|:------------:|-------|
| Technical Merit | 5 | Small but coherent codebase (19 files): `core/` (policy evaluator, hash utility, service orchestrator, signer, config, types), `adapters/audit/` (Sui anchoring + Walrus publishing), `scripts/process-request.ts`, `tests/` (2 test files using vitest). Policy engine uses regex-based risk scoring with 4 rules (instruction override, secret exfiltration, destructive shell, wallet drain). Risk scoring is additive with source/action-type modifiers. Clean service layer with parallel Walrus+Sui execution. ~300 LOC total, functional but minimal. |
| Creativity | 6 | "Proving safe refusal" is a novel angle — most systems only audit what agents did, not what they refused to do. The ALLOW/CHALLENGE/REJECT framework with risk scoring and reasons is a clean abstraction. However, the policy rules are just 4 regex patterns — production systems would need much more sophisticated detection. |
| Problem-Solution Fit | 5 | The concept is valuable — auditable refusal decisions matter for agent safety. But the implementation is too thin to be practical: 4 hardcoded regex rules, no dynamic policy loading, no integration with actual agent frameworks. The live log shows it works end-to-end, but it's more of a proof-of-concept than a usable tool. |
| Sui Integration | 4 | Real `@mysten/sui` SDK usage in `adapters/audit/sui.ts` — creates Transaction, calls `moveCall` with configurable package/module/function, signs and executes. Real Walrus publisher API usage in `adapters/audit/walrus.ts` — PUT to `/v1/blobs` with proper blob ID extraction. Live execution log from Feb 21 shows successful Walrus+Sui anchoring. However: package ID from DeepSurge description NOT FOUND on testnet, log evidence (different blob+digest) also not found (devnet reset likely). No on-chain evidence currently verifiable. |

## Demo Verification
- **GitHub:** Public repo with 19 files, clean structure.
- **Live execution log:** `docs/verification/proof-restraint-live.log` shows successful run on Feb 21 — REJECT verdict with risk score 100, Walrus blob ID `eV5fETp6iIlY1h1AvH3c0P7yf2TUjQ83aBYApc61myE`, Sui digest `8s6e53jMx7TYSf5HjG4kCWbUoBY1GBhP1vkRLAM5VCKr`.
- **Verification attempt:** Both Walrus blob and Sui digest from log return NOT FOUND (devnet reset explains Sui, Walrus blob may have expired). Package ID from DeepSurge description also NOT FOUND on testnet.
- **Tests:** 2 vitest tests (policy evaluation) — pass based on code inspection.

## Code Review Notes
- **Policy engine (`core/policy.ts`):** 4 regex rules with additive scoring. Source modifier (+15 for external), action modifier (+25 for wallet). Risk clamped to 0-100. ≥70 = REJECT, ≥45 = CHALLENGE, else ALLOW. Simple but correct.
- **Service layer (`core/service.ts`):** Clean orchestration — parse input with Zod, evaluate policy, hash payload, parallel Walrus publish + Sui anchor. Good use of `Promise.all`.
- **Sui adapter:** Proper `@mysten/sui` usage with configurable package/module/function. `signAndExecuteTransaction` pattern.
- **Walrus adapter:** Proper PUT to publisher API with content-type `application/octet-stream`, optional API key, blob ID extraction from response.
- **Signer:** Environment-based key loading (MNEMONIC/PRIVATE_KEY).
- **Missing:** No Move contract source code in repo (only references package ID). No OpenClaw integration/skill definition. No frontend/dashboard.

## Sui Integration Analysis
- **Sui SDK:** Real `@mysten/sui` with Transaction builder + moveCall ✓
- **Walrus:** Real publisher API client ✓
- **Move contract:** Source not in repo, claimed package not found on testnet ✗
- **On-chain activity:** Log shows past successful execution, but nothing verifiable now ✗
- **Evidence quality:** Two different sets of evidence (description vs log), neither verifiable ✗

## Overall Assessment
**Legitimate code with unverifiable evidence.** Unlike my initial assessment (which had no code), the repo contains real, functional code — proper Sui SDK usage, Walrus publisher integration, and a clean service layer. The live execution log from Feb 21 shows it worked at some point. However, the project is thin (~300 LOC, 4 regex rules) and crucially, none of the on-chain evidence is currently verifiable — the package, transaction, and Walrus blob are all gone (likely devnet resets + blob expiry). The Move contract source isn't even in the repo.

**Shortlist recommendation: No — real but minimal code, no verifiable on-chain evidence, no Move source in repo.**
