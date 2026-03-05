# Injection Hunter (728ce007) — Audit

## Project Info
| Field | Value |
|-------|-------|
| **DeepSurge ID** | `728ce007-42cb-4ba5-b924-486fd7ff5463` |
| **Name** | Injection Hunter |
| **Track** | Safety & Security |
| **GitHub** | https://github.com/bytesloop/injection_hunter |
| **Website** | N/A (points to GitHub) |
| **Demo Video** | ❌ No demo video (YouTube link points to GitHub) |
| **Package ID** | `0x2fbbd7e553561aceed6001316e679b3a2dd9ad3d4e760cdbd9cc10bbd6f7fea8` |
| **Object ID** | `0xc1c004bfd995d9a1069a856971237522e7b945494238d16cf027bb8cb75bfe8a` |
| **Network** | Testnet |
| **Listed** | True |
| **Submitted** | 2026-03-03T09:34:04.485Z |

## Description
Prompt injection detection middleware for AI agents. Multi-layer detection via regex pattern matching, with rule hashes stored on Sui blockchain for transparency and verifiability. Includes OpenClaw skill integration.

## Eligibility Checklist
- [x] Submitted to DeepSurge
- [ ] Developed by AI agents — unclear, 1 commit
- [x] Uses at least one Sui Stack component — Move contract deployed with on-chain RuleHash object
- [ ] Working demo verifiable by humans — **No demo video**
- [ ] Complete DeepSurge profile with wallet address

## Evaluation Scores
| Criteria | Score (1-10) | Notes |
|----------|:------------:|-------|
| Technical Merit | 4 | Small project (~1,032 LOC) with 1 commit. Scanner is a basic regex engine that checks input against 7 patterns (ignore instructions, role play, system prompt extraction, jailbreak, command injection, Chinese override commands, encoding bypass). It works but is trivially bypassable. Move contract (`rules.move`) stores rule hashes on-chain — the concept is sound but the contract is simple. **Sui client is fully mocked** — `publishRuleHash()` returns fake tx hash, `getOnChainHash()` returns hardcoded zeros, `verifyRules()` doesn't actually query the chain. The @mysten/sui import has a try/catch fallback to mock mode. Test file exists for Move but is basic. |
| Creativity | 4 | The concept of storing rule hashes on-chain for verifiability is interesting — you can prove which rules were active when a scan occurred. However, prompt injection detection via regex is a well-known (and well-criticized) approach. Multiple other hackathon submissions tackle the same problem with more sophistication. The bilingual pattern support (English + Chinese) is a nice touch. |
| Problem-Solution Fit | 4 | The problem (protecting AI agents from prompt injection) is important. The solution works for basic cases but has significant limitations: (1) Regex-only detection is easily bypassed with paraphrasing, encoding, or novel attack patterns. (2) No ML/LLM-based analysis despite having an `ai_analysis_prompt` in rules.json that's never used. (3) Sui client is mocked, so the on-chain verification doesn't actually work. (4) No demo to prove it functions end-to-end. |
| Sui Integration | 4 | **Move contract** (`rules.move`, ~90 lines): Deployed on testnet. RuleHash struct stores version, SHA-256 hash, description, timestamp, updater address. Shared object with update and verify functions. **On-chain object exists and contains real data** (hash: `1ecc4cce...`, version 1, timestamp 2026-03-01). Move tests pass. **However:** The JavaScript Sui client is **fully mocked** — never makes real RPC calls. `getOnChainHash()` returns zeros, `publishRuleHash()` returns `'0x' + 'a'.repeat(64)`. Comments say "TODO: Implement real Sui transaction". The @mysten/sui SDK is an optional dependency (try/catch import). The on-chain object was likely created via `sui client call` directly, not through the JS wrapper. |

**Total: 16/40**

## Demo Verification
- **YouTube link:** ❌ Points to GitHub repo URL, not a video.
- **Website link:** ❌ Also points to GitHub.
- **CLI demo exists** (`demo.js`): Runs test cases locally (7 predefined inputs), shows scan results. But this is a local script, not a live demo.
- **No visual/video proof** of the system working.

## Code Review Notes
- **Scanner** (`scanner.js`, ~120 lines): Loads rules from JSON, applies regex patterns to input, calculates severity (critical/high/medium), tracks scan history, outputs summary. CLI mode available. Clean but basic.
- **Rules** (`rules.json`): 7 patterns including English and Chinese injection attempts. Includes unused `ai_analysis_prompt` field.
- **Sui client** (`sui-client.js`, ~130 lines): ⚠️ **Fully mocked.** Optional @mysten/sui import. All methods return mock data. Has CLI mode for `info`, `verify`, `publish` but none actually interact with the blockchain.
- **Move contract** (`rules.move`, ~90 lines): Real and deployed. RuleHash with shared object pattern. `create_rule_hash`, `update_hash`, `verify`, `get_info` functions. Two basic test functions. The main module (`injection_hunter.move`) is **empty** — just a commented-out boilerplate.
- **OpenClaw skill** (`openclaw_skill/SKILL.md`): Proper skill definition with usage instructions and CLI commands. Chinese documentation.
- **1 commit**: Entire project in a single "first commit".

## Sui Integration Analysis
- **Move contract:** ✅ Deployed on testnet. On-chain RuleHash object exists with real data.
- **On-chain object:** ✅ `0xc1c004bf...` is a shared RuleHash with hash `1ecc4cce...`, version 1.
- **JavaScript Sui client:** ❌ **Fully mocked.** Never queries the chain. All methods return hardcoded/fake data.
- **@mysten/sui SDK:** ⚠️ Optional dependency, falls back to mock mode.
- **Walrus/Seal:** ❌ Not used.

## Overall Assessment
Injection Hunter (728ce007) is a minimal prompt injection scanner with an on-chain rule hash concept. The Move contract is real and deployed with actual data on-chain, which is better than some submissions. However:

1. **No demo video** at all
2. **JS Sui client is fully mocked** — the bridge between the scanner and the blockchain doesn't work
3. **Only 1 commit** — appears hastily assembled
4. **Regex-only detection** is trivially bypassable
5. **Shares the same name** as another submission (`9aaf1a99`) but is a completely different (and weaker) project

Note: This is different from Injection Hunter (`9aaf1a99`) which was already audited separately.

**Shortlist recommendation: No**
