# Sui-Butler — Audit

## Project Info
| Field | Value |
|-------|-------|
| **DeepSurge ID** | `d3bf212b-2fe5-4053-8e93-97cb7dd2fb25` |
| **Name** | Sui-Butler |
| **Track** | Local God Mode |
| **GitHub** | https://github.com/kordotsui/sui-butler |
| **Website** | https://sui-butler.ai (domain not resolving) |
| **Demo Video** | https://youtube.com/watch?v=sui-butler-demo (placeholder URL — video does not exist) |
| **Package ID** | `0x5f1d297a11647415180f555671aea78cee6bf2280263412d77ad6f4521f4c628` |
| **Network** | Testnet |
| **Submitted** | 2026-02-07T06:38:31.029Z |

## Description
Sui-Butler is a decentralized, autonomous AI assistant framework built on Sui. It enables AI agents (OpenClaw) to manage their own operational budgets securely through on-chain Budget Objects and Agent Capabilities. By leveraging Sui's object-centric model, Sui-Butler provides a transparent, verifiable, and programmable economy for agents, allowing them to autonomously pay for their own resources (APIs, compute, etc.) while keeping the human owner in control.

## Eligibility Checklist
- [x] Submitted to DeepSurge
- [ ] Developed by AI agents (or mostly AI agents) — not verifiable
- [x] Uses at least one Sui Stack component — Move contract deployed on testnet with real transactions
- [ ] Working demo verifiable by humans — no working demo video, no live website
- [ ] Complete DeepSurge profile with wallet address

## Evaluation Scores
| Criteria | Score (1-10) | Notes |
|----------|:------------:|-------|
| Technical Merit | 4 | Clean, well-structured Move contract (187 lines) with proper error codes, events, access control, and comprehensive tests (168 lines, 4 test cases including negative tests). But the project is **Move contract only** — no frontend, no SDK integration, no CLI, no agent framework as described. Total codebase is 375 lines (Move + tests + config). For an "autonomous AI assistant framework," there's no AI or agent code whatsoever. |
| Creativity | 6 | The concept of on-chain budget management for AI agents is genuinely interesting and timely. Using Sui's object model (shared Budget objects + owned AgentCap capabilities) to create a delegation pattern is a natural fit. The idea of agents autonomously managing budgets with owner oversight is compelling. However, only the smart contract layer exists — the creative vision isn't realized. |
| Problem-Solution Fit | 4 | The problem (agents need to pay for resources autonomously, humans need oversight) is real and growing. The Move contract does solve the on-chain portion cleanly — budget creation, deposits, capability-based spending, withdrawal, and closure. But the "solution" stops at the contract. There's no agent integration, no OpenClaw skill, no SDK wrapper, no demonstration of an agent actually using the budget. It's a foundation without a building. |
| Sui Integration | 6 | **Strongest aspect of this project.** The Move contract is well-written and properly leverages Sui primitives: shared objects (Budget), owned objects (AgentCap), capability-based access control, Balance/Coin handling, event emission (5 event types). **Deployed on testnet** with real transactions: BudgetCreated event + 10 SUI deposited into the budget (10,000,000,000 MIST). Budget object exists on-chain with balance intact. Published.toml confirms toolchain v1.64.2. However, no Sui SDK usage, no PTBs from a client, no dapp-kit — purely Move-side. |

## Demo Verification
- **YouTube video:** URL `https://youtube.com/watch?v=sui-butler-demo` is a **placeholder** — the video ID "sui-butler-demo" does not correspond to a real YouTube video. **Red flag per audit template.**
- **Live site:** `https://sui-butler.ai` — domain does not resolve. No website exists.
- **On-chain verification:**
  - Package `0x5f1d...c628` exists on testnet as an immutable package object. ✓
  - Module `butler` is deployed with all expected structs (Budget, AgentCap) and functions (create_budget, deposit, spend, withdraw, issue_agent_cap, close_budget). ✓
  - **BudgetCreated** event emitted (tx: `HZNLMSaJxhYeLHnqjPzHtE8dT5aZNaJDsUS4aJTQXQUW`). ✓
  - **DepositEvent** — 10 SUI deposited (tx: `3dPgiRQfbkSsTxJZbTMtfehVqTv3a1vCi3ECTtUZDXPJ`). ✓
  - Budget object `0xaafe...81f3` is live with balance of 10,000,000,000 MIST (10 SUI), total_spent = 0. ✓
  - No SpendEvent found — the agent spending flow was never demonstrated on-chain. ✗
  - Only 2 total transactions against the contract. Minimal usage.

## Code Review Notes
- **Move contract (sui_butler.move, 187 lines):** Clean, idiomatic Sui Move. Structs: `Budget` (shared, key) with owner/balance/total_spent; `AgentCap` (key+store) with budget_id reference. 5 event types for full audit trail. Functions implement a complete budget lifecycle: create → deposit → issue_agent_cap → spend → withdraw → close_budget. Proper access control: owner-only for issue_agent_cap, withdraw, close_budget; cap-based for spend; open for deposit. Error codes are well-named (EInsufficientFunds, ENotAuthorized, EInvalidAmount, ECapMismatch). Uses `balance::zero()`, `coin::put`, `coin::take`, `coin::from_balance` correctly. Object cleanup in `close_budget` properly unpacks and deletes UID.
- **Tests (sui_butler_tests.move, 168 lines):** 4 test functions covering: (1) full lifecycle — create, deposit by stranger, issue cap, agent spend, owner withdraw, close; (2) unauthorized spend with mismatched cap (expected_failure); (3) unauthorized close by stranger (expected_failure); (4) insufficient funds (expected_failure). Good coverage of both happy path and error paths.
- **No other code exists.** No TypeScript/JavaScript, no frontend, no SDK integration, no CLI tool, no agent framework, no OpenClaw skill. The entire project is a single Move module + tests.
- **Move.toml:** Minimal — no external dependencies beyond implicit Sui framework. Edition 2024.

## Sui Integration Analysis
- **Move contract:** Well-written, deployed, functional. Uses shared objects, owned capabilities, Balance<SUI>, events. ✓
- **On-chain activity:** Package deployed, 2 transactions (create + deposit). Budget object exists with 10 SUI. ✓
- **Sui SDK (@mysten/sui):** Not used — no client code exists. ✗
- **dapp-kit:** Not used — no frontend. ✗
- **Walrus:** Not used. ✗
- **Seal:** Not used. ✗
- **PTBs:** No client-side PTB construction. ✗
- **OpenClaw integration:** None — despite being described as an "AI assistant framework." ✗

## Overall Assessment
**Clean contract, incomplete project.** Sui-Butler has a genuinely well-crafted Move smart contract that properly leverages Sui's object model for agent budget management. The capability-based access control (owner issues AgentCap, agent uses it to spend) is a textbook-quality example of Sui's ownership model. Tests are comprehensive with good negative case coverage. The contract is deployed on testnet with real transactions.

However, the project is dramatically incomplete relative to its description. It claims to be an "autonomous AI assistant framework" but contains zero AI/agent code. There's no frontend, no SDK integration, no CLI, no OpenClaw skill — just a 187-line Move contract. The demo video URL is a placeholder (not a real YouTube video). The website domain doesn't resolve. Only 2 on-chain transactions exist, and the spend flow was never demonstrated. This is a smart contract looking for an application.

**Shortlist recommendation: No — too incomplete. Strong Move fundamentals but the project is just a contract with no application layer, no demo, and no agent integration as claimed.**
