# ClawShield — Audit

## Project Info
| Field | Value |
|-------|-------|
| **DeepSurge ID** | `4bd6cfba-43f0-4c6e-98c6-22fcf28ec7e2` |
| **Name** | ClawShield |
| **Track** | Track 1: Safety & Security |
| **Team** | Nader Amin |
| **GitHub** | https://github.com/naderamin/clawshield |
| **Website** | https://www.moltbook.com/post/f4c50fcb-10e7-4120-95a2-406014cba2ef |
| **Demo Video** | https://www.youtube.com/watch?v=t7tD5rOrNR4 (82s) |
| **Package ID** | None |
| **Network** | Claims Mainnet but no deployment |
| **Submitted** | 2026-02-07 |

## Problem & Solution
- **What is it?** A regex-based prompt injection scanner + wallet air-gap policy template, with a Sui attestation stub.
- **What problem does it solve?** External content (web pages, emails) can contain prompt injection attacks. Agents need to detect and strip these before processing. Also, agents shouldn't execute wallet transfers autonomously.
- **Who has this problem?** Anyone running agents that consume untrusted external content.
- **Does the solution fit?** Partially. Regex-based injection detection is a starting point but trivially bypassable. The wallet air-gap is just a markdown policy document, not code. The Sui attestation is a stub that outputs JSON — it doesn't actually transact on-chain.
- **Would someone use this?** Unlikely in its current form. 187 lines of JS with regex patterns is a weekend prototype, not a usable security tool.

## Description
Two components:
1. **Prompt Firewall** — scan.js (133 lines) with regex rules for injection patterns (override instructions, shell commands, secret exfiltration, funds transfer). Scans input files, strips high-severity lines, outputs labeled JSON.
2. **Wallet Air-Gap** — A markdown policy document suggesting agents should propose but not execute transfers.
3. **Sui Attestation** — attest.js (38 lines) outputs a JSON payload with content hash + timestamp. Does NOT submit to Sui — just prints JSON and says "publish this on Sui."

## Eligibility Checklist
- [x] Submitted to DeepSurge
- [ ] Uses at least one Sui Stack component — **NO.** The Sui "attestation" is just a JSON hash generator. It never calls the Sui SDK, never submits a transaction, never interacts with any chain.
- [ ] Working demo — Demo shows `npm run demo` in terminal. No on-chain interaction demonstrated.
- [ ] Complete DeepSurge profile with wallet address

## Demo Verification
- **Video:** 82s screen recording. Shows PowerShell running `npm run demo` which scans clean_input.txt (low risk) and malicious_webpage.txt (high risk, detects override/command/exfil patterns). Also shows the Moltbook post and GitHub repo. No on-chain activity.
- **On-chain:** No package ID. No transactions. The attestation stub just generates JSON locally.

## Code Review Notes
- **Total code:** 187 lines of JavaScript (scan.js 133, attest.js 38, demo.js 16)
- **No Move contracts**
- **No Sui SDK usage** — doesn't import @mysten/sui or any blockchain library
- **No tests**
- **Regex patterns are trivially bypassable** — simple string matching, not semantic analysis
- **Wallet air-gap is a markdown file**, not enforcement code

## Sui Integration Analysis
- **None.** The project has zero actual Sui integration. The attestation stub outputs a JSON payload and tells you to "publish this on Sui using your normal wallet tooling." It doesn't use the Sui SDK, doesn't build transactions, doesn't interact with any network.

## Evaluation Scores
| Criteria | Score (1-10) | Notes |
|----------|:------------:|-------|
| Technical Merit | 2 | 187 lines of JS with regex patterns. No tests, no smart contracts, no real security analysis. |
| Creativity | 3 | Prompt injection detection + wallet air-gap are known concepts. No novel approach. |
| Problem-Solution Fit | 3 | Real problem, but regex-based detection is trivially bypassable. Wallet air-gap is a policy doc, not enforcement. |
| Sui Integration | 1 | Zero actual Sui integration. The attestation stub just prints JSON. |

## Overall Assessment
**Does not meet eligibility criteria.** ClawShield is a minimal prototype — 187 lines of regex-based scanning with no actual Sui integration. The "Sui attestation" is a JSON hash generator that never touches the blockchain. No Move contracts, no SDK usage, no on-chain transactions. The demo shows only local terminal output.

The problem is real but the solution is too shallow to be competitive. A regex scanner is a starting point but not a submission-worthy security tool, especially for a hackathon requiring Sui Stack usage.

**Shortlist recommendation: No.**
