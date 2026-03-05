# DeepClean Butler clawbot — Audit

## Project Info
| Field | Value |
|-------|-------|
| **DeepSurge ID** | `c9809030-86d4-4885-816a-92e0827ec22f` |
| **Name** | DeepClean Butler clawbot |
| **Track** | Local God Mode |
| **GitHub** | `https://github.com/brishibhatia/clawbot` |
| **Website** | `https://clawbot-beta.vercel.app/` |
| **Demo Video** | N/A |
| **Package ID** | `0x769312f41f42c28a12e1a0767906b557ef8b5c6dc39297b5f7b8cc4f939c7fb1` |
| **Network** | Testnet |
| **Listed** | True |
| **Submitted** | 2026-03-02T18:47:52.251Z |

## Description
DeepClean Butler is a verifiable, AI-powered local agent that proactively cleans and organizes your workspace (Desktop, Downloads, etc.) without ever permanently deleting files. For every cleanup run, it produces a cryptographic, tamper-evident "proof bundle" stored on Walrus and anchored immutably on Sui.

## Eligibility Checklist
- [x] Submitted to DeepSurge
- [x] Developed by AI agents (or mostly AI agents) — OpenClaw-native skill with supervised workflow
- [x] Uses at least one Sui Stack component — Move contract + real Walrus storage
- [x] Working demo verifiable by humans — 10+ on-chain events with verifiable Walrus blobs
- [x] Complete DeepSurge profile with wallet address

## Evaluation Scores
| Criteria | Score (1-10) | Notes |
|----------|:------------:|-------|
| Technical Merit | 8 | Impressive monorepo: `apps/deepclean-cli` (plan/run/prove/verify/restore commands), `apps/deepclean-daemon` (scheduler + watcher), `apps/web` (Next.js verification UI), `packages/core` (classifier, executor, planner, policy-engine, proof-bundle, semantic-classifier, seal), `packages/walrus-sui` (sui-client, walrus-client, verify, PoA cache), `packages/openclaw-skill`. ~3400 LOC TypeScript + 122 LOC Move. Tests for classifier, policy-engine, and proof-bundle. 40+ proof bundles committed in `.deepclean/proofs/`. Well-structured with proper separation of concerns. |
| Creativity | 8 | "Verifiable file cleanup with blockchain proof" is a clever, practical local-agent use case. The proof bundle concept — hashing cleanup plan, file tree, and action bundle, then anchoring on Sui with Walrus storage — is well-executed. Includes PoA (Proof of Availability) fields linking Walrus certify transactions. Dual AI classifier support (OpenAI + Gemini). Non-destructive by design (quarantine, never delete). |
| Problem-Solution Fit | 8 | Directly addresses trust in AI file operations. Users can verify exactly what the agent moved/organized. The immutable audit trail means the agent can't hide mistakes. Real-world utility for anyone with a messy desktop. OpenClaw skill integration makes it immediately usable. |
| Sui Integration | 9 | Move contract with `CleanupRun` object (15 fields including bundle_sha256, file_tree_root, plan_hash, policy_hash, walrus_blob_id). On-chain timestamp via `sui::clock::Clock` (not client-supplied — cannot be spoofed). **10+ real events** spanning multiple days. Each event includes Walrus blob IDs. PoA fields for Walrus availability certificates. `packages/walrus-sui` has proper Sui client + Walrus client + verification logic + PoA caching. Seal module in core. This is one of the deepest Sui+Walrus integrations in the hackathon. |

## Demo Verification
- **GitHub:** Public repo with full source, 1214 files, well-organized turborepo monorepo.
- **On-chain:** Package confirmed on testnet. 10+ `CleanupRunRecorded` events with real data: action_count (2-27), unique run_ids, Walrus blob IDs, SHA256 hashes, timestamps spanning Feb 25 - Mar 3. Genuine repeated usage.
- **Proof bundles:** 40+ proof manifests committed in `.deepclean/proofs/`, each with unique run IDs matching on-chain events.
- **Website:** Vercel-hosted verification UI at `clawbot-beta.vercel.app`.

## Code Review Notes
- **Architecture:** Turborepo monorepo with clean package separation:
  - `apps/deepclean-cli`: CLI with plan, run, prove, verify, restore, status commands
  - `apps/deepclean-daemon`: Background daemon with scheduler and file watcher
  - `apps/web`: Next.js verification UI with API route for on-chain verification
  - `packages/core`: Classification (rule-based + AI semantic), policy engine, proof bundle generation, Seal integration
  - `packages/walrus-sui`: Sui + Walrus clients, PoA caching, verification utilities
  - `packages/openclaw-skill`: OpenClaw integration with check-balance and demo
- **Move contract (122 LOC):** Well-documented, uses `sui::clock::Clock` for trusted timestamps, emits `CleanupRunRecorded` events, stores PoA fields. Clean and purposeful.
- **Tests:** Unit tests for classifier, policy-engine, and proof-bundle. E2E evidence in committed proof manifests.
- **Security:** Non-destructive design (quarantine only), cryptographic hash chain for tamper evidence, on-chain anchoring.

## Sui Integration Analysis
- **Move contract:** Deployed, actively used, well-designed with on-chain timestamps and PoA ✓✓
- **Walrus:** Real blob IDs in events, dedicated `walrus-client.ts`, PoA caching ✓✓
- **Seal:** Module present in `packages/core/src/seal.ts` ✓
- **SDK:** `@mysten/sui` used throughout `packages/walrus-sui` ✓
- **On-chain activity:** 10+ events over multiple days — genuine heavy usage ✓✓
- **OpenClaw skill:** Native skill package with supervised workflow ✓

## Overall Assessment
**One of the strongest submissions in the hackathon.** DeepClean Butler is a complete, well-architected system with real code (3400+ LOC TS + 122 LOC Move), real on-chain activity, real Walrus storage, and a practical use case. The turborepo structure with proper package separation shows engineering maturity. 40+ proof bundles committed to the repo demonstrate extensive testing. The Move contract uses on-chain timestamps (not client-supplied) and PoA fields for Walrus certificates — deeper Sui integration than most submissions. This is what a hackathon project should look like.

**Shortlist recommendation: YES — comprehensive implementation, deep Sui+Walrus integration, real usage evidence, practical utility.**
