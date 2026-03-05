# Lulu AI Firewall — Audit

## Project Info
| Field | Value |
|-------|-------|
| **DeepSurge ID** | `08910ac9-d4a6-4666-9186-9772927cc8d5` |
| **Name** | Lulu AI Firewall |
| **Track** | Track 1: Safety & Security |
| **Team** | EasonC13-agent (Eason) |
| **GitHub** | https://github.com/EasonC13-agent/lulu-ai-firewall-sui-hackathon |
| **Website** | https://lulu.suimate.ai |
| **Demo Video** | None (YouTube link points to website) |
| **Pitch** | https://docs.google.com/presentation/d/1zYE1JzCIhaYqVKaG0sYgnaMgWSdkYPx6/edit |
| **Package ID** | `0x42a47edd3066dd10e516ec2715ba61fbca91eec0be12288c97b0edb04d092678` |
| **Network** | Testnet |
| **Submitted** | 2026-02-11 |

## Problem & Solution
- **What is it?** An AI-powered assistant for macOS's LuLu firewall that analyzes network connections, tells users if they're safe/malicious, and lets them allow/block from Telegram — with optional pay-per-use AI access via Sui micropayments.
- **What problem does it solve?** LuLu firewall shows cryptic alerts like "python3 wants to connect to 185.199.108.133:443" and most users can't tell if it's safe. They either allow everything (useless) or block everything (broken). This is especially dangerous for AI agents with root access making outbound connections.
- **Who has this problem?** Anyone running LuLu on macOS — particularly developers running AI agents (OpenClaw) who need to understand and control what their agents are connecting to.
- **Does the solution fit?** Yes — AI analysis of firewall alerts is a natural use case. The agent context is especially compelling: an AI agent analyzing what another AI agent is doing on the network. The Sui payment tunnel adds a monetization/access layer.
- **Would someone use this?** Yes for the firewall analysis. The Telegram integration is practical for remote management. The Sui payment layer is more speculative but architecturally sound.

## Description
LuLu AI consists of three independent components:
1. **lulu-monitor** (Agent Skill) — Background service that detects LuLu alerts via AppleScript, sends them to an AI agent (via OpenClaw) for analysis, delivers results to Telegram with one-tap Allow/Block buttons
2. **LuLu AI Companion** (Mac App) — Native SwiftUI menu bar app with AI analysis overlay, WHOIS/Geo IP enrichment, setup wizard
3. **3mate Platform** — Web platform with Sui Tunnel micropayments for pay-per-use AI API access (in progress)

## Eligibility Checklist
- [x] Submitted to DeepSurge
- [x] Uses at least one Sui Stack component
- [ ] Working demo video (no actual YouTube demo — link points to website)
- [ ] Complete DeepSurge profile with wallet address

## Demo Verification
- **Video:** ❌ No demo video — the YouTube link on DeepSurge just points to the landing page. However, the project has:
  - A detailed **building demo conversation** at skills.suimate.ai/demo.html showing the entire vibe-coding development process
  - Screenshots of Telegram notifications with real alerts and Allow/Block buttons
  - Screenshot of the Mac Companion app showing AI analysis overlay
- **Website:** https://lulu.suimate.ai — clean documentation site with architecture diagrams, examples, and links to all repos
- **Platform:** https://platform.3mate.io — live web dashboard (requires wallet connection to test)
- **On-chain:** Package v2 deployed on Sui testnet (2026-02-11). Real transactions visible on Suiscan:
  - `create_creator_config` ✅
  - `mint` (test USDC) ✅
  - `open_tunnel` ✅
  - `add_authorized_key` ✅
  All from 18 days ago — matches the deployment timeline.

## Code Review Notes
- **Multi-repo architecture:** 4 repos total (submission hub + lulu-monitor + LuLuAICompanion + platform.3mate.io)
- **Move contracts:** 1,376 lines including 915 lines of tests (42 tests, claimed 100% coverage). Tunnel payment protocol with Ed25519 signature verification, multi-key authorization, grace period close, nonce replay protection. Well-structured, v2 upgrade from v1.
- **Swift Mac app:** 3,109 lines. Native SwiftUI with Accessibility API monitoring, Claude API client, WHOIS/Geo enrichment, Keychain integration, History manager.
- **Agent Skill:** Node.js + AppleScript. Detects LuLu alerts, integrates with OpenClaw gateway, Telegram bot for remote control.
- **Web platform:** ~2,000 lines React/TypeScript. Dashboard, tunnel management, API key management, balance tracking. Uses Firebase auth, @mysten/dapp-kit for wallet.
- **Total:** ~8,100 lines across Move, Swift, JS, TypeScript

## Sui Integration Analysis
- **Move smart contracts** — Tunnel payment protocol on testnet with proper Ed25519 sig verification, multi-key support, nonce protection, grace period. Sophisticated contract design.
- **@mysten/dapp-kit** — Wallet connection for the web platform
- **Gas Station** — Sponsored transactions for tunnel operations
- **Test USDC** — Custom test coin for the payment system
- **On-chain verification** — Real testnet transactions proving the tunnel flow works

## Evaluation Scores
| Criteria | Score (1-10) | Notes |
|----------|:------------:|-------|
| Technical Merit | 8 | Multi-component system (Move contracts, Swift app, Agent Skill, Web platform). 42 Move tests with 100% coverage claim. Solid engineering across multiple languages. |
| Creativity | 9 | "AI agent watching what other AI agents do on the network" is a compelling Track 1 concept. The Sui payment tunnel for pay-per-use AI is novel. Builds on real open-source firewall (LuLu). |
| Problem-Solution Fit | 9 | Directly addresses the hackathon's Track 1 brief — building the "immune system" for agents with root access. Firewall analysis for AI agent network activity is a real, timely problem. |
| Sui Integration | 7 | Move contracts are well-written with proper testing, but deployed on testnet only. The payment tunnel is the main Sui component — the firewall analysis itself doesn't require Sui. Integration is solid but Sui is more of a monetization layer than core to the security functionality. |

## Concerns
- **No demo video** — biggest gap. Screenshots and building demos exist but no screencast showing the full flow working end-to-end
- **3mate Platform "in progress"** — the Sui payment integration isn't fully complete
- **Testnet only** — no mainnet deployment
- **Sui integration is optional** — the firewall analysis works without Sui; the blockchain is only for the payment layer

## Overall Assessment
**Strong Track 1 contender.** Lulu AI is one of the most well-thought-out safety projects — it directly addresses the "agents with root access" threat model from the hackathon brief. The multi-component architecture (Agent Skill + Mac App + Platform) shows serious ambition and execution. Move contracts are well-tested (42 tests, 100% coverage). The code is real and substantial (~8K lines across 4 repos).

The main weaknesses are: no demo video (critical miss for judging), testnet-only deployment, and Sui being more of a payment layer than core to the security function. But the problem-solution fit is excellent and the engineering quality is high.

**Shortlist recommendation: Yes — strong candidate for top 10 in Track 1.**
