# Agents (Aegis Protocol) — Audit

## Project Info
| Field | Value |
|-------|-------|
| **DeepSurge ID** | `878b5ef5-9fb0-4884-aa58-f448986bd28a` |
| **Name** | Agents (Aegis Protocol) |
| **Track** | Safety & Security |
| **GitHub** | https://github.com/nerv00kaworu/aegis-protocol |
| **Website** | https://github.com/nerv00kaworu/aegis-protocol |
| **Demo Video** | https://youtu.be/X61fbfZe-XI |
| **Package ID** | `0x00eaeb964c2acd0dbf26264cbd13c2008def9b55957b3cdf7e8907492d7b3ab3` |
| **Network** | Testnet |
| **Submitted** | 2026-02-08T14:58:37.165Z |

## Description
"The First Community-Powered Skill Firewall for OpenClaw." Aegis is a decentralized security protocol that enables agents to share threat intelligence via Sui. Local guard scans for malicious patterns, threats are recorded on-chain, and all Aegis-protected agents become immune.

## Eligibility Checklist
- [x] Submitted to DeepSurge
- [ ] Developed by AI agents (or mostly AI agents) — cannot verify, repo is gone
- [x] Uses at least one Sui Stack component — Move contract deployed
- [ ] Working demo verifiable by humans — repo 404, demo is 15-second scripted terminal
- [ ] Complete DeepSurge profile with wallet address

## Evaluation Scores
| Criteria | Score (1-10) | Notes |
|----------|:------------:|-------|
| Technical Merit | 2 | GitHub repo returns 404 — no source code available for review. On-chain contract is extremely minimal: single `Blacklist` struct with just `add_threat` and `check_threat` functions. Zero on-chain events (contract was never actually used). Demo is a 15-second scripted terminal recording — no evidence of working software. |
| Creativity | 6 | The concept is genuinely interesting — a community-powered threat intelligence network for agent skills, where one detection immunizes all agents. "One Infected, All Immunized" is a compelling vision. But it's just a vision with no implementation behind it. |
| Problem-Solution Fit | 5 | The problem is real — agents installing untrusted skills is a security concern. But the solution as implemented (a simple blacklist of byte vectors) doesn't actually solve it. No scanning logic, no signature verification, no integration with OpenClaw skill installation. |
| Sui Integration | 2 | Move contract deployed but never used (0 events). Contract is trivially simple — just a shared Blacklist object with vector<u8> entries. No SDK usage verifiable (repo gone). No frontend. No Walrus. No dapp-kit. |

## Demo Verification
- **YouTube video (0:15):** Extremely short — 15-second terminal recording showing a simulated agent session. Shows "npx molthub install super-calculator", Aegis scanning files, checking digital signatures on Sui, detecting a threat, and blocking execution. Appears to be scripted terminal output rather than actual running software. 0 views.
- **Live site:** No website — points to GitHub repo which is 404.
- **On-chain verification:** Package `0x00ea...3ab3` exists on testnet with module `aegis`. Contains only `Blacklist` struct and two functions (`add_threat`, `check_threat`). **Zero events** — the contract was deployed but never called.

## Code Review Notes
- **GitHub repo:** 404 — repository has been deleted or made private. No source code available.
- **On-chain contract analysis (via RPC):** Single module `aegis` with one struct `Blacklist` and two functions:
  - `add_threat(blacklist: &mut Blacklist, threat: vector<u8>, ctx: &mut TxContext)` — entry function
  - `check_threat(blacklist: &Blacklist, threat: vector<u8>) -> bool` — read-only
- No events defined, no access control visible, no complex logic.
- The "MoltHub" package manager referenced in the demo doesn't appear to exist.

## Sui Integration Analysis
- **Move contract:** Deployed but minimal (Blacklist + 2 functions). Never used on-chain. ✗
- **SDK usage:** Cannot verify — repo gone ✗
- **dapp-kit:** None ✗
- **Walrus:** None ✗
- **On-chain activity:** Zero events, zero transactions against the contract ✗

## Overall Assessment
**Weak submission.** The concept of a community-powered threat intelligence network for agent skills is genuinely interesting, but the execution falls far short. The GitHub repo is 404, the demo is a 15-second scripted terminal recording, the on-chain contract is trivially simple and was never actually used, and there's no frontend, no SDK integration, and no evidence of working software. The gap between the ambitious description ("14 entry functions, global immunity") and what actually exists (2 functions, 0 transactions) is too large.

**Shortlist recommendation: No — fails minimum eligibility (no accessible code, no working demo).**
