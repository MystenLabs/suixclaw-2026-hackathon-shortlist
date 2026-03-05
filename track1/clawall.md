# ClaWall — Audit

## Project Info
| Field | Value |
|-------|-------|
| **DeepSurge ID** | `717c6d03-bd57-4fc3-bab3-01b404bebed9` |
| **Name** | ClaWall |
| **Track** | Track 1: Safety & Security |
| **Team** | tejas0111 |
| **GitHub** | https://github.com/tejas0111/clawall |
| **Website** | https://clawall.netlify.app |
| **Demo Video** | Embedded mp4 on website + in repo (src/demos/demo.mp4) |
| **Package ID** | `0x9f4d442bc7a3fbb33375daa4f8dd4912287de271475cd8d35afaf072ffaa8bab` |
| **Network** | Testnet |
| **Submitted** | 2026-02-10 |

## Problem & Solution
- **What is it?** A multi-layer AI enforcement system — intent firewall, risk scoring, Telegram-based governance (approve/reject/freeze), on-chain constrained transfers, and Walrus audit logging.
- **What problem does it solve?** AI agents executing blockchain transactions can drain wallets, run dangerous commands, or bypass human intent. ClaWall puts a constraint layer between the AI and execution.
- **Who has this problem?** Anyone running autonomous agents that handle real money or execute system commands.
- **Does the solution fit?** Yes — multi-layer approach (intent firewall → risk scoring → governance → constrained transfer → audit) is well-architected. The on-chain `TransferConstraint` pattern enforces max amount, allowed recipient, and expiry at the Move level.
- **Would someone use this?** The architecture is sound. The Telegram governance bot for approve/reject is practical. The constrained transfer model is a genuinely useful pattern.

## Eligibility Checklist
- [x] Submitted to DeepSurge
- [x] Uses at least one Sui Stack component (Move + Walrus)
- [x] Working demo (embedded video shows live Telegram approval flow)
- [ ] Complete DeepSurge profile with wallet address

## Move Compilation
- ✅ Compiles cleanly with `sui move build` (warnings only — duplicate aliases, minor)

## Demo Verification
- **Video:** Embedded mp4 showing live threat simulation — intercept, Telegram approval, freeze, and audit in real time. Shows Telegram bot (@test_agent_approval_bot) with Approve/Reject buttons.
- **Website:** https://clawall.netlify.app — polished dark-theme landing page with architecture diagram, risk level table, demo video, install instructions
- **On-chain:** 20+ `mint_constraint` transactions on testnet from 16-18 days ago. Active usage of the constraint contract.

## Code Review Notes
- **Move contract:** 107 lines. `TransferConstraint` pattern with max_amount, allowed_recipient, expiry, nonce, and proposal_blob_id (Walrus link). `GuardCap` for admin. Events on execution. Clean, purposeful contract.
- **JS enforcement layers:** ~2,100 lines across multiple modules:
  - `brain.mjs` (258 lines) — orchestration + Sui SDK integration
  - `intent-firewall.mjs` (92 lines) — classifies intent types
  - `risk-engine.mjs` (177 lines) — scores risk 0-100 based on amount, patterns, context
  - `telegram-bot.mjs` (408 lines) — governance via Telegram with approve/reject/freeze commands
  - `walrus.mjs` (109 lines) — audit log upload to Walrus
  - Policy modules for browser, filesystem, OS, script enforcement
- **Well-architected:** Clear separation of concerns across enforcement, risk, governance, and audit layers

## Sui Integration Analysis
- **Move smart contract** — `TransferConstraint` object enforces max amount, allowed recipient, expiry at the contract level. Uses Clock for time verification. Events for audit trail. Deployed on testnet with real transactions.
- **Walrus** — Audit logs uploaded to Walrus with blob IDs stored in constraint objects
- **@mysten/sui SDK** — Used in brain.mjs for transaction building and constraint minting

## Evaluation Scores
| Criteria | Score (1-10) | Notes |
|----------|:------------:|-------|
| Technical Merit | 8 | **RE-AUDIT (Mar 4):** Major upgrade — +16,963 lines, 8 new commits. Move contract doubled (107→219 lines): added multi-coin Vault (Bag-based generic storage), GlobalFreeze emergency kill switch with PolicyAdminCap, PolicyAnchor for on-chain policy hash verification. 8 new test files (hardening, security, red-team benchmark, quarantine forensics, market data). Setup pipeline, uninstall script, prompt quarantine system. Well-structured multi-layer defense. |
| Creativity | 7 | Multi-layer defense (firewall → risk → governance → constrained transfer → audit) is a solid architecture. Telegram governance is a nice UX touch. Red-team benchmarking and prompt quarantine are good additions. |
| Problem-Solution Fit | 8 | Directly addresses the "agents handling money" problem. The constrained transfer pattern (max amount, allowed recipient, expiry enforced on-chain) is exactly right. GlobalFreeze adds emergency response. |
| Sui Integration | 7 | **RE-AUDIT:** Move contract significantly improved: multi-coin Vault with Bag<TypeName, Balance<T>>, GlobalFreeze shared object with events, PolicyAnchor for on-chain policy verification, execute_transfer_from_vault (vault-based instead of direct coin). 5 on-chain events verified. Walrus for audit logs. Proper capability pattern (GuardCap + PolicyAdminCap). |

## Overall Assessment
**Solid Track 1 project.** ClaWall has a well-thought-out multi-layer architecture with real on-chain enforcement. The Move contract compiles, is deployed, and has 20+ real transactions. The Telegram governance bot adds practical UX. Walrus audit logging completes the picture.

Main weaknesses: Move contract is relatively simple (107 lines), testnet only, and the YouTube link on DeepSurge points to the website rather than an actual video (though the website does have an embedded demo).

**Shortlist recommendation: Yes — solid candidate for top 10 in Track 1.**
