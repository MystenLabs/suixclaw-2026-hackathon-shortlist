# RAM — Audit

## Project Info
| Field | Value |
|-------|-------|
| **DeepSurge ID** | `724e2d79-f85c-4ae9-aff5-ddc5ddda5bf4` |
| **Name** | RAM — Voice-Secured Wallet on Sui |
| **Track** | Safety & Security |
| **GitHub** | https://github.com/ducnmm/ram |
| **Website** | https://ramsui.up.railway.app/ |
| **Demo Video** | https://youtu.be/GpgZUrQRNSw |
| **Package ID** | `0x6f99788a7c9de395c05454de9aa02ceb55ce5df7badde5f74b9ddb8d1c3a1c70` (submission) / `0x736b816583ded8dbcb298fd51499fa0ec4d27d942fd8163e90935ffd8b12d7f8` (published) |
| **Network** | Testnet |
| **Submitted** | 2026-02-10T15:20:14.549Z |

## Description
RAM is a voice-protected cryptocurrency wallet on Sui. Before high-value transfers, users must record a voice confirmation. The audio is analyzed in real-time for stress/duress indicators inside an AWS Nitro Enclave (via Nautilus TEE framework). If duress is detected, the wallet silently auto-locks for 24 hours. Crucially, the frontend is "blind" — it never learns whether duress was detected; only the blockchain contract knows.

## Eligibility Checklist
- [x] Submitted to DeepSurge
- [x] Developed by AI agents (or mostly AI agents)
- [x] Uses at least one Sui Stack component — Deep Sui integration (Move, Nautilus, dapp-kit, SDK)
- [x] Working demo verifiable by humans — Live site on Railway + 1:09 YouTube demo
- [x] Complete DeepSurge profile with wallet address

## Evaluation Scores
| Criteria | Score (1-10) | Notes |
|----------|:------------:|-------|
| Technical Merit | 9 | Full-stack system across 4 layers: Move contracts (1152 lines across 6 modules), Rust Nautilus server (voice stress analysis + enclave signing), Rust backend (Axum API + Sui event indexer), React frontend with dapp-kit. DSP-based voice stress analysis is real engineering — pitch jitter via autocorrelation, energy variance, zero-crossing rate, high-frequency ratio. Includes unit tests for DSP. 128 files total. |
| Creativity | 9 | Voice-based duress detection for crypto wallets is a genuinely novel concept. The "blind frontend" design is especially clever — the app intentionally doesn't reveal whether duress was detected, preventing attackers from knowing the wallet locked. The "silent lockdown" happens only on-chain. This is creative security thinking, not just another transaction firewall. |
| Problem-Solution Fit | 8 | Addresses a real (if niche) threat: coerced cryptocurrency transfers. The solution is elegant — you can't fake a calm voice under duress (at least not easily). The 24-hour lock gives time for the situation to resolve. Practical concern: voice stress analysis accuracy varies, and a false positive locks your wallet for a day. But as a hackathon concept, the fit is strong. |
| Sui Integration | 9 | Exemplary Sui stack integration. Move contracts use shared objects, Bag for multi-coin balances, Clock for time-based locking, proper event emissions (7 event types). **Nautilus TEE framework** — the enclave module is the standard Mysten Labs enclave.move with PCR verification and signature validation. The Move contract verifies enclave-signed payloads before executing operations. Frontend uses @mysten/dapp-kit (useCurrentAccount, useSuiClient, useSignAndExecuteTransaction) + Transaction builder. Rust backend runs a Sui event indexer polling suix_queryEvents. |

## Demo Verification
- **YouTube video (1:09, unlisted):** Real demo — shows wallet connected with 0.09 SUI balance, transfer page with recipient address input, amount input with SUI toggle, "Send" button. Shows the voice auth recording interface. Video by "Đức Nguyễn" for Sui Vibe Hackathon.
- **Live site:** https://ramsui.up.railway.app/ — UP and functional. Clean UI with wallet card, Transfers/Deposit/Withdraw action cards. Connect wallet button present.
- **On-chain verification:** Package `0x6f99788a7c9de395c05454de9aa02ceb55ce5df7badde5f74b9ddb8d1c3a1c70` exists on testnet with 5 modules (bioguard, core, events, transfers, wallet). Second package `0x736b816583ded8dbcb298fd51499fa0ec4d27d942fd8163e90935ffd8b12d7f8` also deployed. Zero events observed (wallet creation/transfers may not have happened on this specific package version, or the demo used a different deployment).

## Code Review Notes
- **Move contracts (1152 lines, 6 modules):**
  - `core.move` (300 lines): Core structs — RamRegistry (shared, maps address → wallet ID), RamWallet (shared, with Bag balances, linked_address, locked_until_ms). Intent constants matching Rust server. Proper One-Time Witness pattern. Enclave capability creation in init.
  - `wallet.move` (270 lines): Wallet creation (with/without enclave signature, for-address), address linking, deposit (anyone can, checks lock), withdraw (owner-only with enclave signature). Uses generic coin types via type_name.
  - `bioguard.move` (110 lines): Core security — `apply_bioauth` verifies enclave signature, checks replay protection, and if result == DURESS, locks wallet for 24 hours via Clock. Also has manual lock function.
  - `transfers.move` (129 lines): Two transfer modes — with enclave signature (voice-verified) and with wallet auth (direct from dApp). Both check lock status.
  - `events.move` (93 lines): 7 event types (WalletCreated, AddressLinked, Deposited, Withdrawn, Transferred, WalletLocked, BioAuthCompleted).
  - `tests.move` (250 lines): Test suite for wallet creation, deposits, transfers, balances.
- **Nautilus TEE Server (Rust):**
  - `voice_stress.rs` (~400 lines): Real DSP implementation — WAV parsing, feature extraction (pitch jitter via autocorrelation, energy variance, zero-crossing rate, high-frequency ratio, RMS energy, F0 estimation). Stress scoring with thresholds. Includes unit tests for calm voice, trembling voice, and feature extraction. This is legitimate signal processing, not faked.
  - `handlers.rs`: Enclave endpoints for create_wallet, link_address, bio_auth, transfer. BioAuth handler is the core — decodes audio, runs stress analysis, determines OK/InvalidAmount/Duress result, signs payload with enclave key. Returns BLIND response (frontend can't see result).
  - `audio.rs`: Audio pipeline — base64 decode, WebM→WAV conversion (via subprocess), integration with Hume AI for emotion analysis and OpenRouter for transcript extraction. Falls back to DSP-only analysis if APIs unavailable.
- **Backend (Rust/Axum, 752 lines):**
  - Proxy layer between frontend and Nautilus server.
  - Sui event indexer — polls `suix_queryEvents` every 5 seconds, stores events in PostgreSQL with proper cursor management.
  - REST API for wallet events and stats.
- **Frontend (React/Vite):**
  - Full dApp with @mysten/dapp-kit integration. Pages: Home, Transfer, Deposit, Withdraw, History.
  - VoiceAuth component: Real microphone recording via MediaRecorder API, sends audio to backend for analysis.
  - TransferPanel: Builds Sui Transaction with moveCall to bioguard::apply_bioauth, then transfers::transfer_with_signature. Properly chains enclave signature verification with on-chain execution.
  - useRamWallet hook: Queries on-chain registry and wallet objects via suiClient.
  - SuiNS name resolution for addresses.

## Sui Integration Analysis
- **Move contracts:** 6 modules, 1152 lines. Shared objects, Bag for multi-coin, Clock for time-locking, proper events, generic coin type support. ✓✓
- **Nautilus TEE framework:** Uses standard Mysten Labs enclave.move. EnclaveConfig with PCR verification. Enclave signature verification in all critical paths. ✓✓
- **@mysten/dapp-kit:** useCurrentAccount, useSuiClient, useSignAndExecuteTransaction, useResolveSuiNSName. ✓✓
- **@mysten/sui SDK:** Transaction builder with moveCall for all wallet operations. ✓
- **Sui event indexer:** Rust backend polls suix_queryEvents and stores in PostgreSQL. ✓
- **Object model:** RamRegistry (shared) + RamWallet (shared) + VotingToken (owned). Proper use of Bag for dynamic coin storage. ✓✓

## Overall Assessment
**Outstanding submission.** RAM is one of the most technically ambitious and well-executed projects in the hackathon. It delivers a genuinely novel security concept (voice-based duress detection) with deep, thoughtful engineering across four layers: Move smart contracts with proper security patterns, a Nautilus TEE server with real DSP-based voice analysis, a Rust backend with event indexing, and a polished React frontend. The "blind frontend" design where the app intentionally cannot see whether duress was detected is brilliant security thinking. The Sui integration is exemplary — not just using the blockchain for storage, but leveraging Nautilus TEE for enclave-verified signatures that the Move contract validates on-chain. The only weakness is limited on-chain activity (zero events on the queried package), but the code is clearly functional and the live site is up.

**Shortlist recommendation: YES — strong top-10 candidate. One of the most creative and technically deep submissions.**
