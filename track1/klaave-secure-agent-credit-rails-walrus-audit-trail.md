# Klaave (Secure Agent Credit Rails + Walrus Audit Trail) — Audit

## Project Info
| Field | Value |
|-------|-------|
| **DeepSurge ID** | `42de72f3-0605-46d7-870f-18f7630221c9` |
| **Name** | Klaave (Secure Agent Credit Rails + Walrus Audit Trail) |
| **Track** | Safety & Security |
| **GitHub** | https://github.com/R3DRVM/claave-acl |
| **Website** | https://claave-acl.vercel.app/ |
| **Demo Video** | https://youtu.be/iS37hnw-YRo |
| **Package ID** | N/A — no Sui deployment |
| **Network** | Monad (EVM chain 143), NOT Sui |
| **Submitted** | 2026-02-07T02:20:03.898Z |

## Description
Klaave claims to be "secure, agent-native credit rails" with USDC lending pools, bond-backed borrowing, and a Walrus audit trail for Sui x OpenClaw hackathon. In reality, the project is deployed entirely on Monad (an EVM chain) using Solidity smart contracts and Foundry tooling. No Sui or Walrus integration exists.

## Eligibility Checklist
- [x] Submitted to DeepSurge
- [ ] Developed by AI agents (or mostly AI agents)
- [ ] Uses at least one Sui Stack component — **FAILS: zero Sui integration**
- [x] Working demo verifiable by humans — frontend works on Monad
- [ ] Complete DeepSurge profile with wallet address

## Evaluation Scores
| Criteria | Score (1-10) | Notes |
|----------|:------------:|-------|
| Technical Merit | 5 | Competent EVM project — multiple Solidity contracts (AgentCreditLine, ACLPool, ProtocolReserve, KCLStaking, MockUSDC), Foundry tests, React/Vite frontend with wallet connection. ~52 files. Working Vercel deployment. Shows real engineering effort — but for the wrong chain. |
| Creativity | 5 | Agent-native credit rails with bond-backed borrowing is an interesting DeFi concept for autonomous agents. The lend/borrow model with fee-yield and slashing mechanics is well-thought-out. But this is a DeFi protocol, not really a safety/security tool (wrong track). |
| Problem-Solution Fit | 3 | Submitted to Safety & Security track but it's a DeFi lending protocol. The "audit trail" mentioned in the title doesn't exist. The Walrus integration promised in the description is completely absent from the codebase. |
| Sui Integration | 0 | **Zero Sui integration.** Entire project is built on Monad (EVM chain 143) using Solidity, Foundry, and ethers.js. No Move contracts, no Sui SDK, no dapp-kit, no Walrus, no Seal. A grep for "walrus" and "sui" across the entire codebase returns zero relevant matches. The submission description claims Walrus integration that does not exist. |

## Demo Verification
- **YouTube video:** Not checked — moot given disqualification.
- **Live site:** https://claave-acl.vercel.app/ — UP and functional. Shows "KLAAVE — Agent-native credit lines on Monad". Has Lend/Borrow/Keeper tabs, pool stats, demo rail walkthrough. But connects to chain 143 (Monad), not Sui.
- **On-chain verification:** No Sui deployment. Contracts are Solidity deployed on Monad.

## Code Review Notes
- **Smart contracts (Solidity):** AgentCreditLine.sol, ACLPool.sol, ProtocolReserve.sol, KCLStaking.sol, MockUSDC.sol, plus variants (AgentCreditLineKCL.sol, AgentCreditLineKCLFee.sol). Built with Foundry.
- **Frontend (React/Vite):** Uses ethers.js, EVM wallet connection. Claave-specific ABIs and constants for Monad chain.
- **Scripts:** Deployment scripts (Foundry), keeper scripts, UniV4 pool finding, nad.fun launch — all EVM-specific.
- **No Sui code anywhere:** No Move files, no @mysten imports, no Walrus client, no Sui SDK references.

## Sui Integration Analysis
- **Move contracts:** None ✗
- **Sui SDK:** None ✗
- **dapp-kit:** None ✗
- **Walrus:** None (despite being in the project title) ✗
- **Seal:** None ✗
- **On-chain activity:** Zero on Sui ✗

## Overall Assessment
**Disqualified — wrong chain.** Klaave is a competently built EVM DeFi protocol on Monad, but it has absolutely zero Sui ecosystem integration. The submission claims Walrus integration in its title and description, but no Walrus code exists anywhere in the repository. This appears to be an existing Monad project submitted to the Sui x OpenClaw hackathon without any actual Sui work. Fails the fundamental eligibility requirement of using at least one Sui Stack component.

**Shortlist recommendation: No — disqualified. Zero Sui integration. Deployed on Monad (EVM), not Sui.**
