# OneKey Air-Gap Sui — Audit

## Project Info
| Field | Value |
|-------|-------|
| **DeepSurge ID** | `2ab27374-ac26-4ef0-9f91-cb90520a5067` |
| **Name** | OneKey Air-Gap Sui |
| **Track** | Track 1 — Safety & Security |
| **GitHub** | [fabw222/onekey_air_gap](https://github.com/fabw222/onekey_air_gap) |
| **Website** | [fabw222.github.io/onekey_air_gap](https://fabw222.github.io/onekey_air_gap/) |
| **Demo Video** | [Loom](https://www.loom.com/share/a85e97c768f24415a686933c2b0d5625) |
| **Package ID** | N/A (SDK/middleware — no on-chain package) |
| **Network** | Claims Mainnet (network-agnostic SDK; no deployed contract) |
| **Listed** | True |
| **Submitted** | 2026-03-03T07:08:13.950Z |

## Description
OneKey Air-Gap Sui is a TypeScript SDK/middleware that adds hardware-enforced human approval to every blockchain transaction made by AI agents on Sui. It implements a four-gate security pipeline: **Build → Parse → Review → Sign**. When an AI agent proposes a transaction, the middleware BCS-decodes the transaction bytes, runs a dry-run simulation, flags suspicious patterns (high gas, non-standard packages, publish/upgrade commands, duplicate transfers, dry-run failures), and requires explicit human "approve" in a terminal UI before forwarding raw bytes to a OneKey hardware wallet for physical button-press confirmation. The private key never leaves the device's secure element.

## Eligibility Checklist
- [x] Submitted to DeepSurge
- [ ] Developed by AI agents (or mostly AI agents) — unclear, only 4 commits; not explicitly stated
- [x] Uses at least one Sui Stack component — @mysten/sui SDK, BCS transaction parsing, Sui JSON-RPC dry-run
- [ ] Working demo verifiable by humans — requires physical OneKey hardware (mock mode available for local testing, not publicly verifiable)
- [x] Complete DeepSurge profile with wallet address

## Evaluation Scores
| Criteria | Score (1-10) | Notes |
|----------|:------------:|-------|
| Technical Merit | 7 | Well-architected TypeScript SDK with clean separation (signer → device-manager → reviewer → parser). BCS decoding, dry-run enrichment, 7 warning triggers, Ed25519 hardware signing pipeline. Tests cover hex utils, tx parser, and mock signer. 1,239 LOC across 17 files. Solid but not massive scope. |
| Creativity | 8 | Novel angle: hardware wallet as human-in-the-loop security for AI agents. The "air gap" concept applied to AI agent wallet safety is creative and addresses a real, emerging threat. The four-gate pipeline (Build → Parse → Review → Sign) is well-conceived. |
| Problem-Solution Fit | 8 | Directly addresses the prompt-injection / hot-wallet drain problem for AI agents. The solution is practical and the threat model is sound. The terminal review UI with warning triggers provides real security value. Hardware signing adds a genuine physical barrier. |
| Sui Integration | 6 | Uses @mysten/sui SDK for BCS decoding, Transaction building, SuiClient for dry-run. Correct Ed25519 signature serialization with Sui scheme flag. Handles PTBs (SplitCoins, MergeCoins, TransferObjects, MoveCall, Publish, Upgrade). However: **no on-chain package deployed**, no Move contracts, no Walrus/Seal usage. It's a client-side SDK that wraps the Sui SDK — deep but entirely off-chain. |

## Demo Verification
- **Demo video**: Loom link provided — not publicly verifiable without watching
- **Mock mode**: The SDK includes `--mock` flag for running demos without hardware; this allows code review but not end-to-end hardware verification
- **Landing page**: GitHub Pages site deployed at fabw222.github.io/onekey_air_gap (1,100+ line polished HTML)
- **Limitation**: Full demo requires a physical OneKey hardware wallet connected via USB, making it unverifiable for most reviewers without the device
- **Network claim**: Claims "Mainnet" on DeepSurge but the SDK is network-agnostic (configurable) and no actual mainnet transactions were found

## Code Review Notes
**Repository**: 17 TypeScript files, 1,239 LOC total, 4 git commits

**Architecture** (clean separation of concerns):
- `src/core/onekey-signer.ts` — Main signer class with parse→review→sign pipeline
- `src/core/device-manager.ts` — OneKey hardware SDK wrapper (USB/emulator/mock)
- `src/core/transaction-reviewer.ts` — Terminal UI with chalk-based colored output
- `src/utils/transaction-parser.ts` — BCS decoder using @mysten/sui/bcs, dry-run enrichment
- `src/utils/hex.ts` — Hex/bytes conversion utilities
- `src/middleware.ts` — Factory function `createAirGapClient()`

**Strengths**:
- Proper BCS transaction parsing using official Sui SDK primitives
- 7 distinct warning triggers: high gas, non-standard packages, publish, upgrade, duplicate transfers, dry-run failure, balance changes
- Correct Ed25519 signature serialization (scheme flag + 64-byte sig + 32-byte pubkey)
- CJS→ESM interop handling for OneKey SDK
- Mock mode for development without hardware
- Tests (vitest): hex utilities, transaction parser with actual Transaction building, mock signer instantiation
- `OpenClawSuiTool` demo pattern shows practical AI agent integration

**Weaknesses**:
- Only 4 commits — limited development history
- No CI/CD pipeline
- Tests don't cover the review UI or device manager (only parser and hex)
- No rate limiting or transaction queuing
- Terminal-only review UI — no web/mobile interface

## Sui Integration Analysis
**Sui SDK usage**: Deep and correct
- Uses `@mysten/sui/bcs` for transaction byte decoding (TransactionData BCS schema)
- Uses `@mysten/sui/client` SuiClient for dry-run simulation
- Uses `@mysten/sui/transactions` Transaction builder
- Uses `@mysten/sui/utils` for base64 conversion
- Correctly handles PTB command types: MoveCall, TransferObjects, SplitCoins, MergeCoins, Publish, Upgrade, MakeMoveVec
- Correct Sui address resolution from Pure inputs (32-byte → hex)
- Ed25519 signature format matches Sui's expected `[0x00, sig(64), pubkey(32)]` serialization

**What's missing**:
- No Move smart contracts — entirely client-side TypeScript
- No on-chain package deployment
- No Walrus or Seal integration
- No on-chain activity to verify
- "Mainnet" claim is misleading — the SDK defaults to testnet and no mainnet usage was demonstrated

## Overall Assessment
OneKey Air-Gap Sui is a **well-engineered, focused security middleware** that solves a genuine and timely problem: preventing AI agents from unilaterally draining wallets. The four-gate pipeline is architecturally sound, the BCS parsing is correct, and the OneKey hardware integration is real (not simulated). The code quality is high for a hackathon project.

**Key strengths**: Creative concept, clean architecture, correct Sui SDK usage, practical threat model, working mock mode with demos.

**Key concerns**: No on-chain component (pure client-side SDK), only 4 commits, demo requires physical hardware making it hard to verify, "Mainnet" claim is unsubstantiated. The Sui integration is deep at the SDK level but entirely off-chain — no Move contracts, no deployed packages, no on-chain activity.

**Weighted average**: (7 + 8 + 8 + 6) / 4 = **7.25**

**Shortlist recommendation: YES** — Strong concept with solid execution in the Safety & Security track. The hardware air-gap approach to AI agent security is novel and practical. Despite the lack of on-chain deployment, the deep Sui SDK integration and the relevance of the security problem make this a worthy shortlist candidate.
