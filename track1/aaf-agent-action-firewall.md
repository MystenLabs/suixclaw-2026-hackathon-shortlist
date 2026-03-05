# AAF - Agent Action Firewall — Audit

## Project Info
| Field | Value |
|-------|-------|
| **DeepSurge ID** | `778886ba-0a70-472d-be6b-7f0f760808d5` |
| **Name** | AAF - Agent Action Firewall |
| **Track** | Track 1: Safety & Security |
| **Team** | helloquocbao |
| **GitHub** | https://github.com/helloquocbao/ai_acction_firewall |
| **Website** | https://ai-action-firewall.vercel.app |
| **Demo Video** | ❌ Placeholder (just youtube.com) |
| **Package ID** | `0x887e8ab4f7e5d461ce2605f3cd7e0686fc0113674c31da23ef8368f1746f5f67` |
| **Network** | Testnet |

## Problem & Solution
- **What is it?** An on-chain firewall for AI agent transfers — vault-based custody with scoped permissions (per-transfer cap, total quota, expiry) and a propose→execute workflow.
- **What problem does it solve?** Agents with wallet access can drain funds. AAF enforces spending limits and approval flows at the Move contract level.
- **Who has this problem?** Anyone giving AI agents access to crypto wallets.
- **Does the solution fit?** Yes — vault + scoped permissions + propose/execute is a sound pattern for constraining agent spending. On-chain enforcement means the agent literally cannot exceed its limits.
- **Would someone use this?** The concept is solid. The live UI makes it usable. But it's a narrow tool — only handles SUI transfers, no arbitrary action firewalling despite the name.

## Eligibility Checklist
- [x] Submitted to DeepSurge
- [x] Uses at least one Sui Stack component (Move + dapp-kit)
- [x] Working demo (live website at vercel)
- [ ] Demo video (placeholder YouTube link)
- [ ] Complete DeepSurge profile with wallet address

## Move Compilation
- ❌ Fails locally — Windows-formatted backslash paths in Move.toml. But deployed version exists on testnet so it compiled on the developer's machine.

## Demo Verification
- **Video:** ❌ No video — YouTube link is just youtube.com
- **Website:** ✅ Live at ai-action-firewall.vercel.app. Clean UI showing full workflow: Create AdminCap → Create Vault → Deposit → Issue Permission → Propose Transfer → Execute. Shows package ID, network (testnet), module name. Wallet connection via dapp-kit. Needs wallet to test (flagged for Zee).
- **On-chain:** Package deployed on testnet. Need to verify transactions.

## Code Review Notes
- **Move contract:** 154 lines. Well-structured with AdminCap, Vault (shared object with Balance<SUI>), Permission (scoped with max_amount, max_total, spent_total tracking, expiry, revoke), ActionProposal (propose→execute pattern). Proper error codes and assertions. Real logic, not boilerplate.
- **Frontend:** ~813 lines TypeScript/React. Uses @mysten/dapp-kit and @mysten/sui SDK. Clean error handling with human-readable firewall abort messages. Local storage for object IDs. Step-by-step workflow UI.
- **Total:** ~967 lines (Move + TS)
- **Also includes:** PowerShell demo script, WORKFLOW.md documentation

## Sui Integration Analysis
- **Move smart contract** — Vault custody pattern with Balance<SUI>, scoped Permission objects, ActionProposal flow. Proper use of shared objects, capability pattern (AdminCap), Clock for expiry.
- **@mysten/dapp-kit** — Wallet connection, transaction signing
- **@mysten/sui SDK** — Transaction building for all contract interactions

## Evaluation Scores
| Criteria | Score (1-10) | Notes |
|----------|:------------:|-------|
| Technical Merit | 6 | Clean Move contract with proper patterns (vault, caps, permissions). Working frontend. But ~1K total lines — lightweight. No tests. |
| Creativity | 5 | Vault + permissions + propose/execute is a standard pattern. Several other projects do similar things. The scoped permission model is well-implemented but not novel. |
| Problem-Solution Fit | 7 | The problem is real and the on-chain enforcement is the right approach. But "Agent Action Firewall" only handles SUI transfers — no general action firewalling. |
| Sui Integration | 6 | Good use of Move patterns (shared objects, caps, Clock, Balance). dapp-kit for frontend. But single module, testnet only, and limited to SUI transfers. |

## Overall Assessment
**Decent Track 1 project.** AAF delivers a working, deployed on-chain permission system for agent transfers. The Move contract is clean and uses proper Sui patterns. The live website works. But it's narrow in scope (SUI transfers only), lightweight in code (~1K lines), has no demo video, and several other projects tackle the same problem with more depth.

**Shortlist recommendation: Borderline — lower end of top 10 consideration for Track 1.**
