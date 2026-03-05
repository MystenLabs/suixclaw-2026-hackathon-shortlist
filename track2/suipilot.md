# SuiPilot — Audit

## Project Info
| Field | Value |
|-------|-------|
| **DeepSurge ID** | `8e914153-faff-47a1-a2da-704d69f9f8ad` |
| **Name** | SuiPilot |
| **Track** | Track 2: Local God Mode |
| **GitHub** | https://github.com/obseasd/sui-pilot |
| **Website** | https://github.com/obseasd/sui-pilot |
| **Demo Video** | https://youtu.be/fegMmesxUNA |
| **Package ID** | `0xe3b4ef0f0c31c73e3af8353a3ab223148a8481b12e38345b3d33373e6cd915e1` |
| **Network** | Testnet |
| **Submitted** | 2026-02-12T12:43:04.599Z |

## Problem & Solution
- **What is it?** "The Infinite Money Glitch" — an autonomous local agent that manages your system (file cleanup, organization) AND operates a DeFi portfolio on Sui (staking, swaps), tracking all costs and revenue on-chain via a Move contract. The goal: the agent earns more through DeFi than it costs to run.
- **What problem does it solve?** AI agents cost money to run (API calls, compute, gas). SuiPilot tries to make the agent self-sustaining by combining local utility (file management) with DeFi yield generation.
- **Who has this problem?** Anyone running always-on AI agents who wants them to generate revenue to offset costs.
- **Does the solution fit?** The concept is creative but the execution is more prototype than production. The DeFi agent uses RPC calls to check balances but doesn't actually execute swaps or stakes autonomously (no private key signing implemented).
- **Would someone use this?** Not in current form — the file system manager is a basic organizer, and the DeFi agent is read-only without transaction execution.

## Description
Python-based agent with three components: (1) SystemManager for local file scanning, categorization, and cleanup; (2) SuiDefiAgent for portfolio monitoring, balance checking, and DeFi operation planning on Sui; (3) CostTracker for P&L tracking with on-chain logging via a deployed Move contract. Includes a CLI and interactive demo.

## Eligibility Checklist
- [x] Submitted to DeepSurge
- [x] Developed by AI agents (or mostly AI agents) — Single commit, likely AI-generated
- [x] Uses at least one Sui Stack component — Move contract deployed to testnet + Sui RPC integration
- [ ] Working demo verifiable by humans — Demo script runs locally but DeFi operations are simulated
- [ ] Complete DeepSurge profile with wallet address

## Demo Verification
- **Video:** YouTube link provided (https://youtu.be/fegMmesxUNA)
- **On-chain:** Package `0xe3b4ef...915e1` deployed to Sui testnet. Published.toml confirms testnet deployment with chain-id `4c78adac`, toolchain 1.65.2. The contract is live and verifiable.
- **DeFi operations:** The defi_agent.py calls Sui RPC for balance queries and staking position reads. It does NOT execute transactions — no keypair/signing implementation. Swaps and stakes are planned but not executed.
- **File system:** SystemManager does real file scanning, categorization, and cleanup planning. Dry-run mode by default.

## Code Review Notes
- **Repo structure:** Python project — cost_tracker.py, defi_agent.py, system_manager.py, cli.py, demo.py, contracts/
- **Lines of code:** ~14,509 total (mostly build artifacts). Actual source: ~1,500 lines Python + 163 lines Move.
- **Move contract (1 file, 163 lines):**
  - `pilot_tracker.move` — AgentProfile (shared object) with P&L tracking: total_actions, total_cost_mist, total_revenue_mist, treasury (Balance<SUI>). ActionLog records per operation. Events for creation, action recording, profit milestones (every 100 actions). `is_profitable()` and `net_pnl()` view functions.
  - **Quality:** Clean, focused contract. Proper use of shared objects, Balance type for treasury, events for indexing. The milestone event every 100 actions is a nice touch. Simple but correct.
- **Python backend (~1,500 lines):**
  - `cost_tracker.py` — CostEntry/RevenueEntry dataclasses, P&L calculation, category breakdown. Well-structured.
  - `defi_agent.py` — SuiDefiAgent with RPC client, portfolio management, balance queries, staking position reads. Uses `suix_getBalance`, `suix_getStakes`. Price caching. **No transaction signing** — the agent can read state but not execute operations.
  - `system_manager.py` — File scanning, categorization (documents, images, code, etc.), duplicate detection (hash-based), cleanup recommendations with dry-run mode.
  - `demo.py` — Interactive demo showing full pipeline: scan → organize → DeFi check → cost tracking.
  - `cli.py` — Command-line interface.
- **Dependencies:** Minimal (requests, pyyaml, pytest). No Sui SDK for Python — uses raw RPC.
- **Single git commit** — "Add OpenClaw skill, CLI, and comprehensive tests"

## Sui Integration Analysis
- **Move contract** — 1 contract deployed to testnet. P&L tracker with treasury, action logging, profit verification. Verified via Published.toml.
- **Sui RPC** — Direct JSON-RPC calls for balance queries and staking position reads. No SDK — raw HTTP requests to fullnode.
- **Transaction execution** — Not implemented. The defi_agent has methods for swaps/stakes but they don't sign or submit transactions.
- **On-chain state:** SUIPILOT_PACKAGE_ID hardcoded in defi_agent.py matching the Published.toml — consistent.
- **Net assessment:** Contract is deployed and well-designed. RPC integration is functional for reads. But the core "Infinite Money Glitch" thesis (agent earns via DeFi) is unproven — no actual DeFi transactions can be executed.

## Evaluation Scores
| Criteria | Score (1-10) | Notes |
|----------|:------------:|-------|
| Technical Merit | 5 | ~1,500 lines Python + 163 lines Move. Clean code but limited scope. No transaction execution undermines the core thesis. |
| Creativity | 7 | "Infinite Money Glitch" concept is clever and memorable. Self-sustaining agent via DeFi yield is an interesting angle for Track 2. |
| Problem-Solution Fit | 4 | The concept is appealing but the execution doesn't deliver on the promise — the agent can't actually execute DeFi operations. File management + read-only DeFi isn't "self-sustaining." |
| Sui Integration | 5 | Deployed testnet contract is good. RPC reads work. But no transaction execution means the on-chain P&L tracker is write-less — the agent can't record actions or fund treasury without manual intervention. |

## Overall Assessment
**Creative concept, incomplete execution.** The "Infinite Money Glitch" framing is the best part of SuiPilot — the idea of a self-sustaining agent that earns via DeFi to offset its costs is compelling and aligns well with Track 2's autonomous agent theme. The Move contract is well-designed for P&L tracking.

However, the critical gap is that the agent cannot execute transactions. Without transaction signing, the DeFi agent is read-only (check balances, view staking positions) and the P&L tracker contract can never be written to by the agent itself. The file system manager works but is basic. Single git commit suggests this was built in one session.

**Shortlist recommendation: No — needs transaction execution to deliver on its core thesis.**
