# WALVIS — Audit

## Project Info
| Field | Value |
|-------|-------|
| **DeepSurge ID** | `09758b25-1c81-48be-bb78-15840497a3d2` |
| **Name** | WALVIS (Walrus Autonomous Learning & Vibe Intelligence System) |
| **Track** | Local God Mode |
| **GitHub** | https://github.com/Kuuga-0/walvis |
| **Website** | N/A (intended to deploy to Walrus Sites) |
| **Demo Video** | ❌ YouTube link just points to GitHub repo URL |
| **Package ID** | None |
| **Network** | Testnet |
| **Listed** | False |
| **Submitted** | 2026-03-04T06:51:18.813Z |

## Description
WALVIS is an AI-powered bookmark/knowledge manager that runs as an OpenClaw skill. Users save links, text, and images via Telegram commands; WALVIS auto-analyzes content with LLM, tags it, and stores everything on Walrus decentralized storage. Includes a React web UI intended for deployment on Walrus Sites with dapp-kit wallet connect.

## Eligibility Checklist
- [x] Submitted to DeepSurge
- [ ] Developed by AI agents (or mostly AI agents) — 2 commits, appears AI-assisted
- [x] Uses at least one Sui Stack component — Walrus storage (upload/download/sync), @mysten/dapp-kit in web UI
- [ ] Working demo verifiable by humans — **No demo video (YouTube link is just GitHub URL)**
- [ ] Complete DeepSurge profile with wallet address

## Evaluation Scores
| Criteria | Score (1-10) | Notes |
|----------|:------------:|-------|
| Technical Merit | 6 | Well-structured ~2,639 LOC TypeScript project. Clean architecture: OpenClaw skill with SKILL.md, local storage layer (`~/.walvis/`), Walrus sync scripts, LLM-powered content analysis, query/search engine with relevance scoring, React web frontend (TanStack Router + Vite), and an OpenClaw hook for auto-bookmark detection. Types are well-defined. Search supports full-text scoring across title/tags/summary/content. Wallet setup script with balance check and faucet support. However, only 2 commits and the project is unlisted. No tests. |
| Creativity | 7 | "AI-powered bookmark manager on decentralized storage" is a compelling personal tool concept. The Walrus integration is thoughtful — using it as a personal knowledge base backend where data persists on decentralized infra. The OpenClaw skill format with SKILL.md personality instructions and command handling is well-designed. Auto-save hook for bare URLs is a nice UX touch. Web UI on Walrus Sites is a creative deployment target. However, bookmark managers exist — the novelty is in the Walrus storage and AI analysis layers. |
| Problem-Solution Fit | 6 | The problem (organizing personal knowledge across links, notes, images) is real and universal. Using Walrus for persistence means your bookmarks survive even if your machine dies — good pitch. AI auto-tagging and summarization adds genuine value over plain bookmarking. However: no demo means we can't verify it actually works end-to-end. The project is unlisted on DeepSurge, suggesting it may be incomplete. No package ID means no Move contracts — this is purely Walrus storage, not on-chain. |
| Sui Integration | 5 | **Walrus integration is real and well-implemented:** `walrus-sync.ts` uploads/downloads space data via Walrus publisher/aggregator REST API with proper blob ID handling and epoch configuration. `walrus-query.ts` has a complete local search engine. Web frontend uses `@mysten/dapp-kit` (SuiClientProvider, WalletProvider) and `@mysten/sui` for network config. Wallet setup script calls `suix_getBalance` RPC directly. **However:** No Move contracts at all (no package ID), no on-chain transactions, no Seal integration. The dapp-kit usage in the web UI is configured but the app primarily reads from Walrus aggregator rather than doing on-chain operations. Walrus is the primary Sui stack component used. |

**Total: 24/40**

## Demo Verification
- **YouTube link:** ❌ Points directly to `https://github.com/Kuuga-0/walvis` — no actual demo video exists.
- **No alternative demo** found.
- **Unlisted** on DeepSurge project page.
- The project appears to be a working codebase but unverifiable without a demo.

## Code Review Notes
- **OpenClaw Skill** (`SKILL.md`): Well-written personality/command spec for the WALVIS agent. Defines command parsing (@walvis save, -q query, -s sync, -ls list, -new/-use spaces, -tag filter, -status, -balance, -web). This is a proper OpenClaw skill that could be installed.
- **Storage layer** (`storage.ts`, ~80 lines): Clean local file management at `~/.walvis/`. Manifest tracks spaces, blob IDs, sync timestamps. Spaces are JSON files with bookmark items.
- **Walrus sync** (`walrus-sync.ts`, ~110 lines): Real Walrus upload/download via REST API. `PUT /v1/blobs?epochs=5` for upload, `GET /v1/blobs/{blobId}` for download. Handles both `newlyCreated` and `alreadyCertified` responses correctly. Supports per-space sync and manifest upload.
- **Analyze** (`analyze.ts`, ~100 lines): Sends content to OpenAI-compatible LLM for auto-tagging/summarization. Fetches URL content, strips HTML, sends to LLM with structured JSON output prompt. Graceful fallback on parse failure.
- **Query engine** (`walrus-query.ts`, ~130 lines): Full-text search with weighted scoring (title 10, tags 8, summary 5, content 2). Tag filtering, tag listing with counts, space listing.
- **Web UI** (React + TanStack Router + Vite): Landing page takes a manifest blob ID, fetches from Walrus aggregator, displays spaces and bookmarks with search and tag filtering. Uses `@mysten/dapp-kit` for wallet provider context. Clean dark UI with grid background.
- **Hook** (`handler.ts`): Intercepts bare URL messages for auto-save when auto-save mode is enabled.
- **CLI** (`bin/cli.js`): Interactive setup wizard (not inspected in detail).
- **2 commits total** — likely built quickly.

## Sui Integration Analysis
- **Walrus:** ✅ Real integration — upload/download via publisher/aggregator REST API, blob ID tracking, epoch management, manifest sync.
- **@mysten/dapp-kit:** ✅ Used in web UI — SuiClientProvider, WalletProvider with testnet/mainnet config.
- **@mysten/sui:** ✅ Used for `getFullnodeUrl()` and RPC calls in wallet-setup.
- **Move contracts:** ❌ None. No package ID, no on-chain logic.
- **Seal:** ❌ Not used.
- **On-chain activity:** ❌ No transactions verifiable. No package deployed.

## Overall Assessment
WALVIS is a well-architected personal knowledge management tool with genuine Walrus integration and a solid OpenClaw skill design. The codebase is clean, types are well-defined, and the feature set (AI analysis, sync, search, web UI, auto-save hook) is comprehensive for a hackathon project. The Walrus usage is one of the more authentic in the hackathon — actual blob storage for real user data.

However, critical weaknesses:
1. **No demo video** — YouTube link just points to GitHub
2. **Unlisted on DeepSurge** — suggests incomplete submission
3. **No Move contracts** — purely Walrus storage, no on-chain logic
4. **Only 2 commits** — appears rushed
5. **No package ID** — nothing deployed on-chain

The project has potential but feels incomplete/unfinished for judging.

**Shortlist recommendation: No**
