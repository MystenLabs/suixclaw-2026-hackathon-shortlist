# Pet - AI-driven intelligent desktop companion — Audit

## Project Info
| Field | Value |
|-------|-------|
| **DeepSurge ID** | `6fd71642-2a86-4257-a271-57f222a0ba85` |
| **Name** | Pet - AI-driven intelligent desktop companion |
| **Track** | Track 2: Local God Mode |
| **GitHub** | https://github.com/wangeguo/pet |
| **Website** | https://github.com/wangeguo/pet |
| **Demo Video** | https://youtu.be/sb4dzoH1f1o |
| **Package ID** | N/A |
| **Network** | Mainnet (claimed, but no blockchain code) |
| **Submitted** | 2026-02-13T11:38:46.226Z |

## Problem & Solution
- **What is it?** A desktop pet application — AI-driven 3D companion that lives on your desktop as a floating window. Generate custom 3D pet models via Meshy AI, interact via drag/click, and an AI Brain (LLM) dynamically generates pet behaviors.
- **What problem does it solve?** Desktop companionship — a fun, personalized virtual pet with AI-generated behavior.
- **Who has this problem?** Users who want desktop decoration, virtual pets, or AI-generated content.
- **Does the solution fit?** As a desktop pet app, yes. As a hackathon submission requiring Sui Stack integration, no.
- **Would someone use this?** Possibly as a desktop novelty. It's a well-engineered Rust app, but it has no blockchain functionality.

## Description
Multi-process Rust desktop application using Bevy for 3D rendering, Iced for settings UI, system tray integration, and an IPC-based architecture. Supports GLB/glTF model rendering in transparent borderless windows, replay-based deterministic behavior scripts, drag/click interaction, and AI-powered behavior generation via LLM. Cross-platform (macOS, Linux, Windows).

## Eligibility Checklist
- [x] Submitted to DeepSurge
- [ ] Developed by AI agents (or mostly AI agents) — Has AGENTS.md and appears AI-assisted
- [ ] Uses at least one Sui Stack component — **NO. Zero Sui/blockchain integration.**
- [ ] Working demo verifiable by humans — Desktop app demo video exists, but no on-chain demo
- [ ] Complete DeepSurge profile with wallet address

## Demo Verification
- **Video:** YouTube link provided (https://youtu.be/sb4dzoH1f1o)
- **App:** Real desktop application with Bevy rendering, system tray, and multi-window architecture. The codebase is mature (version 0.4.0, 21+ git commits including dependency bumps).
- **On-chain:** No Package ID. No Move contracts. No Sui SDK. No blockchain integration of any kind.
- **Sui references:** Zero. Grep for "sui", "blockchain", "walrus", "web3", "@mysten" across the entire codebase returns no results. The roadmap mentions "external agent systems (e.g., OpenClaw)" as a future phase item only.

## Code Review Notes
- **Repo structure:** Rust workspace with 6 crates: app, common, theater, tray, manager, settings
- **Lines of code:** 6,042 lines of Rust + supporting configs. This is a substantial, well-structured codebase.
- **Architecture:** Multi-process with IPC routing. Main process (app) spawns child processes (theater, tray, manager, settings). Inter-process communication via custom protocol.
  - `theater` — Bevy-based 3D renderer with animation systems (movement, rotation, scale, bounce, keyframe), replay-based behavior scripts, pet interaction plugins
  - `common` — Shared library for config, models, scripts, paths, storage, error handling
  - `manager` — Pet creation and management UI (Iced) with Meshy AI integration for 3D model generation
  - `settings` — Configuration UI (Iced) for appearance, AI, general settings
  - `tray` — System tray icon and menu
- **Code quality:** High. Rust edition 2024, proper error handling with thiserror, async with tokio, clean module organization. Integration tests present. Justfile for build automation.
- **No Move contracts.** No blockchain code of any kind.
- **Git history:** 21+ commits including dependency bumps, feature additions, bug fixes. This is a real, actively developed project — not a hackathon-only build.

## Sui Integration Analysis
- **None.** Zero Sui stack integration. No Move contracts, no Sui SDK, no Walrus, no Seal, no blockchain code. The roadmap mentions OpenClaw integration as a future aspiration but nothing is implemented.

## Evaluation Scores
| Criteria | Score (1-10) | Notes |
|----------|:------------:|-------|
| Technical Merit | 7 | Impressive Rust application — 6K lines, multi-process architecture, Bevy 3D rendering, IPC, system tray. Well-engineered with clean code quality. |
| Creativity | 6 | Desktop AI pet is fun but not novel. The Meshy AI model generation and replay-based behavior system are nice touches. |
| Problem-Solution Fit | 2 | As a desktop pet app: fine. As a hackathon submission requiring Sui integration: does not fit. |
| Sui Integration | 0 | No Sui integration whatsoever. No contracts, no SDK, no blockchain code. |

## Overall Assessment
**Does not meet eligibility criteria.** Pet is a technically impressive Rust desktop application — the multi-process Bevy architecture, replay-based behavior system, and AI model generation are well-executed. The 6K lines of clean Rust code demonstrate real engineering skill.

However, **this project has zero Sui blockchain integration.** No Move contracts, no Sui SDK usage, no Walrus, no Seal, nothing. The hackathon requires at least one Sui Stack component, and Pet doesn't meet this fundamental criterion. The roadmap mentions OpenClaw integration as a future phase, but nothing is implemented.

This appears to be a pre-existing project that was submitted to the hackathon without adding any Sui integration.

**Shortlist recommendation: No — fails eligibility requirement for Sui Stack usage.**
