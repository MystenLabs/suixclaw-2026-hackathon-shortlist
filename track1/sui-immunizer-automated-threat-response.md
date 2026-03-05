# Sui-Immunizer (Automated Threat Response) — Audit

## Project Info
| Field | Value |
|-------|-------|
| **DeepSurge ID** | `6fe3d3ac-4b66-4b48-b0c8-846c1d9df264` |
| **Name** | Sui-Immunizer (Automated Threat Response) |
| **Track** | Safety & Security |
| **GitHub** | https://github.com/DudeGuuud/Sui_Immunizer |
| **Website** | https://sui-immunizer.vercel.app/ |
| **Demo Video** | https://youtu.be/ZIuXFNzpyxo (not watched) |
| **Package ID** | `0x4c7dc2e5d5ed5d797b9090498fbd1b4957c01f2995f3f728c4aca9342f8e4f7a` |
| **Network** | Testnet |
| **Listed** | True |
| **Submitted** | 2026-02-21T21:10:55.289Z |

## Description
Decentralized, AI-powered vulnerability response system. Vendors publish Seal-encrypted "skill" blobs (remediation playbooks) to Walrus, indexed on-chain. Subscribers with NFTs can decrypt and auto-execute them via OpenClaw agents. Full cycle: vendor publishes vulnerability alert → agent polls Sui events → decrypts skill with Seal → executes remediation → reports result on-chain.

## Eligibility Checklist
- [x] Submitted to DeepSurge
- [x] Developed by AI agents (OpenClaw integration with runEmbeddedPiAgent for auto-execution)
- [x] Uses at least one Sui Stack component — Move (Seal access control), Seal (encrypt/decrypt), Walrus (blob storage), dapp-kit
- [x] Working demo verifiable by humans — On-chain events verified, Walrus blobs contain encrypted data
- [x] Complete DeepSurge profile with wallet address

## Evaluation Scores
| Criteria | Score (1-10) | Notes |
|----------|:------------:|-------|
| Technical Merit | 9 | ~2,941 LOC, 16 commits. **Best Seal integration in the hackathon.** Move contract (~280 lines): AdminCap, Registry (subscription pricing), VendorRegistry, VendorNFT, SubscriberNFT (time-based expiry), SkillBlob (on-chain index to Walrus), two `seal_approve` entry functions (subscriber with Clock expiry check, vendor). Agent (`agent.ts`, ~300 lines): polls VulnerabilityAlert events, Seal SessionKey creation with TTL + auto-refresh, subscription verification (checks owned SubscriberNFT/VendorNFT), Walrus blob fetch + Seal decrypt, OpenClaw `runEmbeddedPiAgent()` for AI execution, on-chain ImmunizationStarted + SystemImmunized reporting. Frontend (`web/`): Next.js with dapp-kit, Seal encrypt/upload, fetch/decrypt with vendor address as identity, SessionKey init with wallet signing. |
| Creativity | 8 | Subscription-based vulnerability response marketplace is a novel concept. Vendors publish Seal-encrypted remediation playbooks, subscribers auto-apply them. The Seal identity design (using vendor address) is elegant — all skills from same vendor share access key. NFT-gated decryption with time-based expiry is a real subscription model. The full flow (alert → decrypt → execute → report) is a complete autonomous security response loop. 5% platform fee on subscriptions adds economic sustainability. |
| Problem-Solution Fit | 8 | Directly addresses Track 1 (Safety & Security). Zero-day vulnerability response is a real problem, and automating it with encrypted playbooks is practical. The subscription model incentivizes vendors to publish timely patches. NFT-gated access ensures only paying subscribers get remediation. On-chain immunization reports create accountability. The agent auto-execution via OpenClaw closes the loop — no human intervention needed. |
| Sui Integration | 9 | **Deepest Seal integration in the hackathon:** (1) **Move contract** (~280 lines): AdminCap, shared registries, VendorNFT/SubscriberNFT with subscription pricing and time-based expiry. `seal_approve_subscriber` checks Clock for NFT expiry. `seal_approve_vendor` for vendor self-access. SkillBlob stores Walrus blob_id on-chain. Events: VulnerabilityAlert, VendorRegistered, PriceUpdated, ImmunizationStarted, SystemImmunized. (2) **Seal** (`@mysten/seal`): Full SealClient usage in both agent and frontend. SessionKey with TTL, personal message signing, encrypt with threshold=2, decrypt with txBytes containing seal_approve call. Vendor address as identity. (3) **Walrus**: Real encrypted blobs uploaded and verified (returned binary = encrypted data). (4) **@mysten/sui SDK**: SuiJsonRpcClient, Transaction builder, Ed25519Keypair, event polling. (5) **dapp-kit**: Frontend with wallet connection, transaction signing, SessionKey init. (6) **On-chain events verified**: VendorRegistered×2, VulnerabilityAlert×2 (with Walrus blob IDs), PriceUpdated×5+. |

**Total: 34/40**

## Demo Verification
- **Video** (not watched — browser reused for Pantheon, will note)
- **Website** (sui-immunizer.vercel.app): Live (Next.js)
- **On-chain verification:**
  - Package deployed with `alert` module
  - VendorRegistered: "Immunizer Labs" and "ReactSec" vendors
  - VulnerabilityAlert: "CVE-2025-55182 — React Server Components RCE" (severity 10) with Walrus blob `1LQjQQin7YJoBE_eq4BjZOYlcNq0uBa33zPBsnaG68c`
  - VulnerabilityAlert: "Daily Security Check 2026/3/2" (severity 4)
  - Multiple PriceUpdated events (testing price management)
  - Walrus blob verified: returns encrypted binary data (Seal-encrypted)

## Code Review Notes
- **Move contract** (`immunizer.move`, ~280 lines): Excellent design. AdminCap for governance. Registry with configurable subscription price/duration and SUI treasury with 5% fee. VendorRegistry (VecSet of addresses). VendorNFT for publishers. SubscriberNFT with time-based expiry (0 = permanent). SkillBlob as shared object with public title/description but Seal-encrypted content on Walrus. Two seal_approve entry functions with proper access control. Event reporting for immunization start/complete.
- **Agent** (`agent.ts`, ~300 lines): Production-quality. Polls Sui for VulnerabilityAlert events. Seal SessionKey with 10-min TTL and auto-refresh. Checks for SubscriberNFT or VendorNFT ownership. Downloads Walrus blob → Seal decrypt → pass to OpenClaw's `runEmbeddedPiAgent()` for AI-driven remediation. Reports ImmunizationStarted and SystemImmunized on-chain with step summary.
- **Frontend Seal lib** (`seal.ts`, ~180 lines): Complete encrypt/decrypt with Walrus integration. `encryptAndUpload()` for vendors. `fetchAndDecrypt()` for subscribers. `createAndInitSessionKey()` with wallet signing. Well-documented with identity convention explained.
- **Frontend** (`web/`): Next.js with dapp-kit providers, vendor dashboard (publish skills, manage prices), subscriber view (browse alerts, decrypt skills).

## Sui Integration Analysis
- **Move contract:** ✅ Comprehensive with Seal access control, subscription model, event reporting
- **Seal:** ✅ **Best in hackathon** — full SealClient, SessionKey, encrypt/decrypt, NFT-gated access with expiry
- **Walrus:** ✅ Real encrypted blobs uploaded and downloadable
- **@mysten/sui SDK:** ✅ Full usage in agent and frontend
- **dapp-kit:** ✅ Frontend with wallet connection

## Overall Assessment
Sui-Immunizer is the best Seal integration in the hackathon and a strong Track 1 contender. The subscription-based vulnerability marketplace is practical and well-designed. The complete flow (vendor publishes encrypted playbook → subscriber's agent auto-decrypts and applies → reports result on-chain) demonstrates a real-world use case for Seal + Walrus.

Strengths:
1. **Best Seal integration** — full encrypt/decrypt with NFT-gated access and time-based expiry
2. **Complete vulnerability response loop** — alert → decrypt → execute → report
3. **Subscription model** — vendor NFTs, subscriber NFTs, 5% platform fee
4. **Real on-chain activity** — vendors registered, vulnerabilities published, Walrus blobs encrypted
5. **Production-quality agent** — event polling, SessionKey management, OpenClaw integration

Weaknesses:
1. **Demo video not watched** (ran out of browser time)
2. **Only testnet** (no mainnet deployment)
3. **16 commits** — moderate development history

**Shortlist recommendation: Yes** 🌟🌟 (best Seal integration, strong Track 1 entry)
