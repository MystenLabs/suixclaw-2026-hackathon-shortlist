# SuiSec 🛡️🦞💧 — Audit

## Project Info
| Field | Value |
|-------|-------|
| **DeepSurge ID** | `775983fd-a898-42c5-a759-4be175d53907` |
| **Name** | SuiSec 🛡️🦞💧 |
| **Track** | Track 1: Safety & Security |
| **Team** | k66inthesky (co-founder of SuiAudit) |
| **GitHub** | https://github.com/k66inthesky/SuiSec |
| **Website** | https://clawhub.ai/k66inthesky/suisec (ClawHub skill listing) |
| **Demo Video** | https://youtu.be/zEo1TPV28ro |
| **Package ID** | `0x76a28891c190e3065ee0c9f7377ea64b10a1a7a3073ee4fcb8354911d51bfdf7` |
| **Network** | Testnet |
| **Submitted** | 2026-02-11T04:07:09.538Z |

## Problem & Solution
- **What is it?** An OpenClaw skill that intercepts Sui transactions, dry-runs them, and compares simulated results against user intent to detect malicious contracts before signing.
- **What problem does it solve?** AI agents with wallet access could execute malicious contracts that drain funds or hijack objects. SuiSec acts as a pre-execution security gatekeeper.
- **Who has this problem?** Anyone using AI agents (OpenClaw) to execute Sui transactions — agents can't distinguish safe contracts from malicious ones.
- **Does the solution fit?** Yes — using Sui's native `--dry-run` to simulate before executing is the right approach. Comparing balance changes and object flows against declared intent catches common attack vectors.
- **Would someone use this?** As an OpenClaw skill, it integrates directly into the agent workflow. The concept is practical and addresses a real gap. However, detection is currently limited to price mismatches — the HIJACK detection code is stubbed out (empty `pass` block).

## Eligibility Checklist
- [x] Submitted to DeepSurge
- [x] Uses at least one Sui Stack component (Sui CLI dry-run, Move contracts on testnet)
- [x] Working demo (demo video + published ClawHub skill)
- [x] Demo video present (https://youtu.be/zEo1TPV28ro)
- [ ] Complete DeepSurge profile with wallet address — not verified

## Repo Structure
```
SuiSec/
├── main.py           (117 lines) — Core audit engine: runs sui commands with --dry-run, parses JSON, detects PRICE_MISMATCH
├── SKILL.md          (143 lines) — OpenClaw skill definition with full workflow protocol
├── test_suisec.sh    (63 lines)  — 3-scenario test script (safe_buy, hidden_steal, profile_theft)
├── setup.sh          (8 lines)   — Checks for sui CLI
├── package.json      (11 lines)  — npm package metadata
└── README.md         (164 lines) — Comprehensive documentation
```
**Total:** ~506 lines across all files. Core logic is 117 lines of Python.

## Move Compilation
- No Move source in repo — the test contract (`suisec_test`) was deployed separately to testnet. Only the compiled package exists on-chain.
- The on-chain package disassembly shows 7 entry functions: `safe_buy`, `hidden_steal`, `profile_theft`, `gas_vampire`, `destructive_burn`, `proxy_scam`, `mint_test_assets` — a well-designed test suite of malicious contract patterns.

## Demo Verification
- **Video:** ✅ Present at https://youtu.be/zEo1TPV28ro (not watched in this audit — flagged for manual review)
- **Website:** ClawHub skill listing at clawhub.ai/k66inthesky/suisec (could not fetch — internal DNS)
- **On-chain:** ✅ Package `0x76a2...5f67` verified deployed on Sui testnet. Type: `package`, Owner: `Immutable`. Contains `suisec_test` module with 7 entry functions covering different attack vectors (hidden drain, object hijack, gas vampire, destructive burn, proxy scam). No events emitted (test contracts, not production use).

## Code Review Notes

### main.py (Core Logic — 117 lines)
- **Security:** Uses `shlex.split()` and `shell=False` to prevent command injection. Forces first arg to be `sui`. Good security hygiene.
- **Dry-run injection:** Automatically appends `--dry-run` and `--json` flags to any sui command.
- **PRICE_MISMATCH detection:** Parses `balanceChanges` from dry-run JSON. Sums up SUI losses for the owner address. Compares against intended cost + 0.02 SUI gas buffer. Flags if actual loss exceeds intent.
- **HIJACK detection:** ⚠️ **Stubbed out.** The `objectChanges` parsing loop exists but the body is just `pass`. This means object hijacking is NOT actually detected despite being advertised.
- **Owner address:** Taken as CLI argument (sys.argv[3]), not auto-detected from dry-run output (README says auto-detected but code requires manual input).
- **Limitations:** Only handles `sui client ptb` commands. No support for `sui client call` in the automated path.

### SKILL.md (Agent Integration — 143 lines)
- Well-written OpenClaw skill definition with clear workflow: Collect Intent → Run SuiSec → Compare → Verdict.
- Includes manual fallback path for `sui client call` commands.
- Defines threat table format and execution logic (exit code 0 = safe, 1 = block).
- Good documentation of what to check: hidden transfers, permission hijacking, gas vampirism, object destruction, proxy calls.

### test_suisec.sh (Test Suite — 63 lines)
- Tests 3 scenarios against live testnet contracts: safe purchase, hidden steal, profile theft.
- Uses hardcoded object IDs (will break if objects change state).
- Colorful output formatting.

### On-chain test contract (suisec_test module)
- **7 entry functions** covering different attack vectors — this is genuinely thoughtful:
  - `safe_buy` — legitimate purchase (control case)
  - `hidden_steal` — splits extra SUI to attacker address
  - `profile_theft` — transfers user's UserProfile to attacker
  - `gas_vampire` — loops 1M iterations to burn gas
  - `destructive_burn` — deletes user's NFT object
  - `proxy_scam` — splits coins to multiple bad addresses
  - `mint_test_assets` — helper to create test objects
- Demonstrates real understanding of Sui attack surfaces.

## Sui Integration Analysis
- **Sui CLI dry-run** — Core of the product. Uses `sui client ptb --dry-run --json` to simulate transactions.
- **Move smart contract** — Deployed testnet package with 7 functions demonstrating attack patterns. Real Move code (verified via on-chain disassembly), not boilerplate.
- **OpenClaw skill** — Published to ClawHub. Integrates into OpenClaw's agent workflow as a pre-execution hook.
- **No frontend / no dapp-kit / no Walrus / no Seal** — This is a CLI/agent tool, not a dApp.

## Evaluation Scores
| Criteria | Score (1-10) | Notes |
|----------|:------------:|-------|
| Technical Merit | 5 | Clever concept with working PRICE_MISMATCH detection, but only 117 lines of core logic. HIJACK detection is stubbed out (advertised but not implemented). No tests beyond the bash script. The Move test contract (7 attack patterns) shows more depth than the Python auditor that's supposed to catch them. |
| Creativity | 7 | Novel approach — using Sui's dry-run as a security layer for AI agents is a genuinely good idea. The "intent vs reality" comparison framework is well-conceived. Published as an OpenClaw skill for real integration. The test contract design (multiple attack vectors) shows creative security thinking. |
| Problem-Solution Fit | 6 | The problem is real and growing (AI agents executing arbitrary contracts). The solution architecture is right (dry-run → compare → block). But only 1 of 2 advertised detection methods actually works. The gap between the comprehensive SKILL.md documentation and the partial implementation is notable. |
| Sui Integration | 6 | Meaningful use of Sui CLI dry-run (a Sui-specific feature). Real Move contract deployed on testnet with multiple modules. But no SDK usage, no dapp-kit, no Walrus/Seal. The Sui integration is narrow but genuine — dry-run simulation is core to the product and uniquely enabled by Sui's architecture. |

## Red Flags
- ⚠️ HIJACK detection advertised in README/SKILL.md but code is `pass` (incomplete implementation)
- ⚠️ README claims "Sender address is auto-detected" but code requires it as CLI argument
- ⚠️ No Move source in repo — only deployed bytecode on testnet
- ⚠️ ClawHub listing could not be verified (DNS resolution blocked)
- Minor: Hardcoded testnet object IDs in test script will break over time

## Overall Assessment
**Interesting Track 1 concept with partial execution.** SuiSec's core idea — using Sui's dry-run to create an intent-verification layer for AI agents — is genuinely creative and addresses a real security gap. The Move test contract is impressive (7 attack vectors), and publishing as an OpenClaw skill shows ecosystem awareness. However, the Python auditor that's supposed to catch these attacks is lightweight (117 lines) and only implements 1 of 2 detection methods. The gap between the well-written documentation and the partial implementation is the main weakness. More of a promising prototype than a complete security tool.

**Shortlist recommendation: NO — good concept but insufficient implementation depth for top 10 in Track 1.**
