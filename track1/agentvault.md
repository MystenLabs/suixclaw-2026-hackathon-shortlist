# AgentVault — Audit

## Project Info
| Field | Value |
|-------|-------|
| **DeepSurge ID** | `fd06d97e-a618-43f3-b93b-01c296890196` |
| **Name** | AgentVault |
| **Track** | Safety & Security |
| **GitHub** | https://github.com/beaniebro/agentvault |
| **Website** | https://sui-agentvault.vercel.app/ |
| **Demo Video** | https://www.loom.com/share/5fc355be4525482383e1744546d343eb |
| **Package ID** | `0x4e064c7a2de2154802a38dce34d9b4610bac537a940c01ee90e432307f7f010a` |
| **Network** | Testnet |
| **Submitted** | 2026-02-11T12:03:46.123Z |

## Description
AgentVault is an on-chain transaction firewall for autonomous AI agents on Sui. Implements a programmable security pipeline at the smart contract layer — every outbound transfer is validated against owner-defined policies before funds leave the vault. Three-tier security: hard blocks (abort malicious txs), soft blocks (queue for human review), and auto-execution (trusted low-risk transfers).

## Eligibility Checklist
- [x] Submitted to DeepSurge
- [x] Developed by AI agents (or mostly AI agents)
- [x] Uses at least one Sui Stack component
- [x] Working demo verifiable by humans
- [x] Complete DeepSurge profile with wallet address

## Evaluation Scores
| Criteria | Score (1-10) | Notes |
|----------|:------------:|-------|
| Technical Merit | 8 | 524-line Move contract with 26 public/entry fns, 20 unit tests (581 lines), full Next.js frontend (~1800 lines TS/TSX), agent CLI demo with 6 scenarios. Clean architecture, proper error handling, well-structured code. |
| Creativity | 7 | Transaction firewall for AI agents is a well-scoped, practical idea. Three-tier security pipeline (hard block/soft block/auto-execute) is a smart design pattern. Not the most novel concept (several submissions tackle agent spending controls) but the execution and architecture stand out. |
| Problem-Solution Fit | 8 | Directly addresses a real and growing problem: AI agents managing real assets need guardrails. The hard/soft block distinction is practically useful — not everything is black and white. Pending approval queue for ambiguous transactions is exactly what an owner would want. |
| Sui Integration | 8 | Deep Sui integration: custom Move contract with shared objects, on-chain events for all security actions, @mysten/dapp-kit for wallet connection, @mysten/sui SDK in agent CLI, Walrus testnet for audit trail storage (blocked txs that Sui would discard). Real on-chain activity verified — VaultCreated, TransferExecuted, TransferQueued events all confirmed on testnet. |

## Demo Verification
- **Loom video (2:34):** Real walkthrough — creates vault, shows dashboard with pending approvals, deny/allow lists, settings, activity feed. Demonstrates all three security tiers with actual on-chain transactions. Narrator explains each feature clearly.
- **Live site:** https://sui-agentvault.vercel.app/ — UP and functional. Clean dark UI with sidebar navigation (Dashboard, Create Vault, Pending, Activity, Settings). Connect Wallet button present.
- **On-chain verification:** Package exists on testnet. Queried events via RPC — confirmed 8+ events including VaultCreated (3 vaults), TransferExecuted (2 transfers of 0.001 SUI to allowlisted address), TransferQueued (4 queued: 2 for "exceeds auto-approve limit" at 8 SUI, 2 for "unknown recipient"). All match the demo scenarios in agent CLI.

## Code Review Notes
- **Move contract (vault.move, 524 lines):** Single module with Vault shared object. Security pipeline in `request_transfer`: auth check → epoch reset → amount validation → hard blocks (per-tx limit, daily limit, denylist) → soft blocks (unknown recipient, auto-approve threshold, rate limit) → auto-execute. Clean separation of owner functions (13 entry fns: create, deposit, withdraw, update_limits, deny/allow list management, approve/reject pending, set/revoke agent) and agent function (request_transfer). Proper error constants and event emissions for all actions.
- **Tests (vault_tests.move, 581 lines, 20 tests):** Comprehensive coverage — tests for vault creation, deposits, withdrawals, all three transfer tiers (execute, block, queue), limit enforcement, denylist/allowlist behavior, pending approval/rejection, agent revocation. Good test suite.
- **Frontend (Next.js 15, ~21 files):** Pages for dashboard, vault creation, pending approvals, activity feed, settings. Uses @mysten/dapp-kit hooks (useCurrentAccount, useSuiClient). Custom hooks for vault data (useVault, useOwnedVaults, useVaultEvents). Walrus client for audit log read/write.
- **Agent CLI (agent.ts, ~230 lines):** 6 demo scenarios covering all security tiers. Uses @mysten/sui SDK for transaction building and signing. Writes audit logs to Walrus after each operation. Hardcoded package/vault IDs match deployed testnet contract.
- **Walrus integration:** Both frontend (walrus-client.ts) and agent CLI write audit entries to Walrus testnet publisher. Frontend reads back via aggregator. Stores blob IDs in localStorage for retrieval. Clever use case — captures blocked transactions that would otherwise be lost (Sui discards aborted tx data).
- **Minor note:** Private key hardcoded in agent CLI (expected for demo), Move.toml uses `mainnet-v1.39.3` rev (fine for testnet deployment).

## Sui Integration Analysis
- **Move smart contract:** Custom module with shared objects, proper access control, epoch-based rate limiting, event emissions ✓
- **@mysten/sui SDK:** Transaction building, signing, event querying in agent CLI ✓
- **@mysten/dapp-kit:** Wallet connection, React hooks in frontend ✓
- **Walrus:** Audit trail storage on testnet — both write (publisher) and read (aggregator) ✓
- **On-chain events:** 6 event types (VaultCreated, TransferExecuted, TransferBlocked, TransferQueued, TransferApproved, TransferRejected) ✓
- **Object model:** Shared Vault object with one-vault-per-agent architecture ✓
- **PTBs:** moveCall-based transaction building in agent CLI ✓

## Overall Assessment
**Strong submission.** AgentVault delivers a complete, well-architected product across all layers: a thoughtful Move contract with a three-tier security pipeline, a polished frontend with full CRUD for vault management, and an agent CLI that demonstrates all security scenarios with real on-chain transactions. The Walrus integration for audit trails is a practical touch — capturing blocked transaction data that Sui would otherwise discard. Code quality is high throughout, tests are comprehensive, and the demo video clearly shows everything working. One of the more complete Track 1 submissions.

**Shortlist candidate: YES**
