# Sui Opportunities Hunter — Audit

## Project Info
| Field | Value |
|-------|-------|
| **DeepSurge ID** | `5a359cd2-e9d1-45c2-b7ce-b01f3bfd8a9a` |
| **Name** | Sui Opportunities Hunter |
| **Track** | Local God Mode |
| **GitHub** | https://github.com/Sergey1997/Sui-Opportunities-Hunter (not in submission — submission linked X profile: https://x.com/sergey1997bsu) |
| **Website** | https://sui-opportunities-hunter.vercel.app |
| **Demo Video** | https://youtu.be/IfQQqrGVsUI |
| **Package ID** | N/A — no Move contracts deployed |
| **Network** | Mainnet (reads on-chain data; no write transactions) |
| **Submitted** | 2026-02-10T14:26:53.823Z |

## Description
Sui Opportunities Hunter is a data service for AI agents that scans Sui DEXes (Cetus, Turbos, Aftermath) in real-time, finds arbitrage and yield opportunities, and shares them through a REST API. Agents download a SKILL.md file, call the API, and get validated DeFi opportunities. The dashboard shows opportunities with AI-generated verdicts (Claude), scan history, and wallet connection via dapp-kit.

## Eligibility Checklist
- [x] Submitted to DeepSurge
- [x] Developed by AI agents (or mostly AI agents) — CLAUDE.md present in repo, code structure consistent with AI-assisted development
- [x] Uses at least one Sui Stack component — `@mysten/sui` SDK for on-chain pool queries, `@mysten/dapp-kit` for wallet connection
- [x] Working demo verifiable by humans — live site with real data, demo video available
- [ ] Complete DeepSurge profile with wallet address — not verified

## Evaluation Scores
| Criteria | Score (1-10) | Notes |
|----------|:------------:|-------|
| Technical Merit | 7 | Well-architected Next.js 15 app (~4,090 lines across 20 source files). Clean separation: scanner, AI service, Supabase persistence, API routes, React components. Multi-source data pipeline querying Cetus, Turbos, Aftermath via GeckoTerminal, on-chain Sui pool objects via SDK, DeFiLlama yields, CoinGecko reference prices, and Birdeye. Supabase with real-time subscriptions for live dashboard updates. SKILL.md as an agent interop protocol — clever design. 50+ scans recorded over 15 days with 30 stored opportunities. No tests. Some hardcoded pool object IDs are invalid on mainnet (1 of 3 Cetus/Turbos pools exists). AI verdict generation works but ran out of Claude API credits. |
| Creativity | 7 | The "SKILL.md as agent API documentation" pattern is genuinely novel — agents download instructions and autonomously use the HTTP API to discover opportunities. This is a practical agent-to-service interoperability model. The multi-source validation approach (cross-referencing Cetus, Turbos, on-chain, DeFiLlama, CoinGecko) is thorough. DeFi scanning itself isn't new, but the agent-as-consumer architecture and the "collective intelligence network" angle (multiple agents sharing discoveries) is an interesting framing for the OpenClaw ecosystem. |
| Problem-Solution Fit | 6 | Real problem: AI agents operating in DeFi need reliable market data without building custom scrapers. This solves the data access problem well — one API call returns validated opportunities from multiple sources. However, the solution is incomplete: zero trades have been executed (0 executed in dashboard), so the "autonomous execution" promise is undelivered. Arbitrage spreads found are tiny (0.3–0.7%), likely not profitable after gas/slippage. Yield opportunities are aggregated from DeFiLlama (existing data), adding limited value over going to DeFiLlama directly. |
| Sui Integration | 5 | Uses `@mysten/sui` SDK (v1.21.0) for real on-chain pool queries — `suiClient.getObject()` reads Cetus/Turbos pool reserves to calculate implied prices. Uses `@mysten/dapp-kit` (v0.14.0) for wallet connection with balance display, explorer links, and disconnect flow — properly implemented. However: **no Move smart contracts**, no on-chain deployment, no transactions ever submitted, no PTBs, no Walrus, no Seal. 1 of 3 hardcoded pool object IDs doesn't exist on mainnet. Integration is strictly read-only — the app queries Sui state but never writes to it. Primary data actually comes from centralized APIs (GeckoTerminal, DeFiLlama), not from Sui directly. |

## Demo Verification
- **YouTube video (title: "Sui Opportunity Hunter Demonstration", by Sergey Danilovich):** Video exists and is accessible. Shows the application in action.
- **Live site:** Fully functional at https://sui-opportunities-hunter.vercel.app. Dashboard shows 30 discovered opportunities (18 arbitrage, 11 yield, 1 hackathon), scan history with 50+ scans over 15 days, real-time agent activity log, and wallet connect button. About page and Docs page both functional. SKILL.md downloadable at `/api/skill`.
- **API verification:** `/api/opportunities` returns real JSON data from Supabase. `/api/scan` triggers a live scan that queries Cetus, Turbos, on-chain Sui pools, DeFiLlama, and CoinGecko — returns real price data with current timestamps. API is functional and returns legitimate market data.
- **On-chain verification:** Pool object `0x06d8af9e6afd27262db436f0d37b304a041f710c3ea1fa4c3a9bab36b3569ad3` exists on mainnet as a Cetus SUI/USDT pool — confirmed via `sui_getObject`. Other 2 hardcoded pool IDs (`0xcf99...` and `0x5eb2...`) return `notExists`. No package ID deployed.

## Code Review Notes
- **scanner.ts (584 lines):** Core scanner that fetches prices from 6 sources in parallel: GeckoTerminal (Cetus, Turbos, Aftermath pools), on-chain Sui SDK (pool object reserves), DeFiLlama (yield pools), CoinGecko (reference prices), and Birdeye. Arbitrage finder compares normalized pairs across DEXes with deduplication. Yield finder surfaces DeFiLlama pools with APY > 3%. Good engineering — handles edge cases, normalizes pair names, skips same-DEX comparisons, deduplicates by direction.
- **sui.ts (44 lines):** Clean SuiClient setup using `@mysten/sui/client`. Configurable network (mainnet/testnet). Utility functions for address formatting, MIST/SUI conversion, and explorer URL generation.
- **supabase.ts (285 lines):** Full CRUD for opportunities, agent logs, and scans. Real-time subscriptions via Supabase channels (`postgres_changes`). Proper TypeScript types. Row-level security enabled (permissive for hackathon).
- **ai.ts (299 lines):** Type-aware Claude API integration with specialized system prompts per opportunity type (arbitrage, yield, hackathon, DeFi, swap, NFT). Generates verdicts with confidence scores and scan summaries. Well-structured but Claude API ran out of credits during active use (visible in scan history error messages).
- **WalletButton.tsx (202 lines):** Full dapp-kit wallet integration — `useCurrentAccount`, `useConnectWallet`, `useDisconnectWallet`, `useWallets`, `useSuiClientQuery` for balance. Wallet picker dropdown, address copy, explorer link. Polished UI.
- **scan/route.ts (214 lines):** API route that orchestrates scans, persists to Supabase, generates AI verdicts, and handles errors gracefully.
- **SKILL.md:** Well-written agent instructions with curl examples for every API endpoint. Agents can scan, submit, get verdicts, and browse opportunities. Novel interop pattern.
- **Database:** 3 tables (opportunities, agent_logs, scans) with proper indexes, RLS, triggers, and real-time publication. SQL scripts included.
- **Red flags:** "GitHub" field in submission points to X/Twitter profile, not a repo. Actual repo found via GitHub search. SKILL.md has placeholder `YOUR_USERNAME` in homepage URL. Some pool object IDs are incorrect/non-existent on mainnet.

## Sui Integration Analysis
- **@mysten/sui SDK:** ✓ Used — `SuiClient`, `getFullnodeUrl`, `getObject()` for reading pool reserves on mainnet. Real on-chain queries happening.
- **@mysten/dapp-kit:** ✓ Used — Full wallet flow with `useConnectWallet`, `useCurrentAccount`, `useSuiClientQuery` for balance, explorer links.
- **Move contracts:** ✗ None written or deployed.
- **On-chain transactions:** ✗ Zero — read-only integration.
- **Walrus:** ✗ Not used.
- **Seal:** ✗ Not used.
- **PTBs:** ✗ Not used.
- **DeFi protocol integration:** Partial — reads data from Cetus/Turbos pools but doesn't execute swaps.

## Overall Assessment
**Solid data service with real infrastructure, but read-only Sui integration and no smart contracts.** Sui Opportunities Hunter is a genuinely functional product — the live site works, the API returns real data, the scanner queries multiple sources including on-chain Sui pool objects, and the Supabase backend has 50+ recorded scans over 15 days. The SKILL.md agent interop pattern is creative and practical. The codebase is well-structured with ~4,090 lines of TypeScript across a clean Next.js architecture.

However, the Sui integration is shallow: no Move contracts, no on-chain deployment, no transactions — just reading pool data via SDK and wallet display via dapp-kit. The primary data actually comes from centralized APIs (GeckoTerminal, DeFiLlama). The "autonomous execution" feature is unimplemented (0 executed trades). Some pool object IDs are incorrect. The submission didn't even link the GitHub repo (pointed to an X profile).

**Shortlist recommendation: BORDERLINE — Good product execution and creative agent interop design, but limited Sui-native integration (no contracts, no transactions, read-only). The SKILL.md pattern and working data pipeline are strong, but the lack of on-chain activity holds it back.**
