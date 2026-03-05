# Stableflow Checkout — Audit

## Project Info
| Field | Value |
|-------|-------|
| **DeepSurge ID** | `4211f778-91e0-4b17-b92a-8f963e1181b4` |
| **Name** | Stableflow Checkout |
| **Track** | Local God Mode |
| **GitHub** | https://github.com/2658183739/vibecoding-vrm-sui |
| **Website** | https://2658183739.github.io/vibecoding-vrm-sui/#/quickstart |
| **Demo Video** | https://www.youtube.com/watch?v=jdmkCqtGSJk |
| **Package ID** | N/A — contract not deployed (Move.toml address = `0x0`) |
| **Network** | Testnet (configured, but no deployment) |
| **Submitted** | 2026-02-09T06:52:37.770Z |

## Description
Stableflow Checkout is a Web3 payment solution on Sui solving "Payment Fragmentation" — merchants want branded stablecoins (BrandUSD) while users hold USDC. It uses PTBs for "Atomic Mint+Pay": USDC collateralizes → mints BrandUSD → pays merchant in one transaction. Includes a local Node.js agent for natural language payment orchestration.

## Eligibility Checklist
- [x] Submitted to DeepSurge
- [x] Developed by AI agents (or mostly AI agents) — AI disclosure folder with 6 detailed prompt logs (Codex/GPT-5 class tooling)
- [x] Uses at least one Sui Stack component — Move contract, @mysten/sui SDK, @mysten/dapp-kit, StableLayer SDK
- [ ] Working demo verifiable by humans — Live GitHub Pages site exists but contract never deployed; demo runs in "smoke mode" with simulated data
- [ ] Complete DeepSurge profile with wallet address

## Evaluation Scores
| Criteria | Score (1-10) | Notes |
|----------|:------------:|-------|
| Technical Merit | 7 | Impressive codebase: ~12,000 lines of TypeScript + Move across a well-structured monorepo (pnpm workspace). 7 frontend pages (Merchant Dashboard, Payment, Redeem, Claim, Metrics, Automation, Local Agent), a 341-line Move contract with 2 unit tests, a rule-based + LLM-powered local agent (HTTP server on port 3777), bilingual support (EN/CN), CI pipeline, e2e test setup (Playwright), and thorough AI disclosure. Architecture is production-grade with proper separation: `packages/move`, `packages/agent` (shared engine), `apps/web` (React 19 + Tailwind + HeroUI), `apps/local-agent` (Node.js HTTP agent). Code quality is high with TypeScript throughout, proper error handling, and configurable via env vars. Deducted for no actual deployment and smoke mode reliance. |
| Creativity | 7 | The "Atomic Mint+Pay" concept — collateralizing USDC to mint branded stablecoins and paying a merchant invoice in a single PTB — is a genuinely novel payment flow. The BrandUSD concept (merchant-specific stablecoins backed 1:1 by USDC) addresses a real commerce need. The local agent with bilingual NLU (rule engine + LLM fallback, supporting Chinese and English) for payment orchestration is a creative local-first approach. The 7-page commercial loop (create → invoice → pay → claim → redeem) is well thought out. |
| Problem-Solution Fit | 6 | The payment fragmentation problem is real in crypto commerce — merchants wanting stable, branded tokens while users hold different stablecoins. The atomic swap approach is elegant. However: (1) the contract was never deployed, so the solution hasn't been validated on-chain; (2) the BrandUSD concept requires StableLayer integration which is configured but untested in production; (3) the local agent is a nice addition but the core value is the payment flow, which remains theoretical. Would need real merchant adoption testing. |
| Sui Integration | 5 | **Code-level integration is strong but undeployed.** Move contract (341 lines): Merchant, Product, Invoice, Receipt objects with proper access control, events (InvoiceCreated, InvoicePaid, ReceiptMinted), and 2 unit tests. Frontend uses `@mysten/sui` SDK extensively (SuiClient, Transaction building, coin selection, mergeCoins, splitCoins, moveCall with type arguments), `@mysten/dapp-kit-react` for wallet connection, and StableLayer SDK for mint/burn flows. PTB composability is used correctly for atomic mint+pay. **However:** Move.toml has `stableflow_checkout = "0x0"`, no package ID exists anywhere in the repo (only `0xYOUR_PACKAGE_ID` placeholder in .env.example), zero on-chain transactions, and the live site runs in smoke mode with a dummy wallet address. The Sui integration is well-architected but entirely theoretical. |

## Demo Verification
- **YouTube video:** Link provided (https://www.youtube.com/watch?v=jdmkCqtGSJk) — would need manual verification.
- **Live site:** GitHub Pages deployment is live (HTTP 200). Loads a React SPA with Sui SDK and StableLayer vendor bundles. The site appears to run in "smoke mode" since no real package ID is configured — uses placeholder `0x1111...1111` address and simulated data.
- **On-chain verification:** **None.** Move contract address is `0x0` in Move.toml. The `.env.example` has `0xYOUR_PACKAGE_ID` placeholder. No real package ID found anywhere in the codebase. Zero on-chain activity.

## Code Review Notes
- **Move contract (checkout.move, 341 lines):** Clean commerce module with 4 object types (Merchant, Product, Invoice, Receipt), 3 event types, proper access control (`assert_merchant_owner`), generic payment type `<T>` allowing any coin type, and 2 `#[test]` functions with proper test cleanup. Well-structured but never deployed.
- **Frontend (apps/web, ~4,600 lines across pages + components):** React 19 + Tailwind + HeroUI. 7 pages covering the full merchant-buyer flow. `sui.ts` (590 lines) has comprehensive Sui SDK usage — object fetching, transaction building, coin selection with merge/split, event querying, chain proof fetching. `buildMintAndPayTx.ts` (112 lines) orchestrates the atomic flow: select USDC coins → StableLayer mint → Move pay_invoice, all in one Transaction. `buildBurnTx.ts` (73 lines) handles BrandUSD → USDC redemption. dapp-kit properly configured with GraphQL client.
- **Agent package (packages/agent, ~1,560 lines):** Rule-based intent engine with keyword matching for PAY/REDEEM/CLAIM/STATUS/HELP intents. Bilingual keyword support (EN + CN). 289 lines of tests.
- **Local Agent (apps/local-agent, ~1,645 lines):** HTTP server (port 3777) with LLM integration for NLU, rule engine fallback, audit logging, configurable domain allowlist, OpenClaw browser adapter for UI automation, and security module. Well-architected local-first agent.
- **AI Disclosure (6 prompt logs):** Transparent about AI-assisted development. Each prompt documented with tool, date, and human review notes. Good practice.
- **CI/CD:** GitHub Actions with lint, build, test. Playwright e2e test config present.
- **Smoke mode:** The app has a `?smoke=1` query parameter mode for demo purposes with a fake wallet address, which is what the deployed site uses.

## Sui Integration Analysis
- **Move contract:** Well-written with generics, events, access control. Never deployed. ✗ (deployed) ✓ (code quality)
- **@mysten/sui SDK:** Extensively used — SuiClient, Transaction, moveCall, coin operations, event queries. ✓
- **@mysten/dapp-kit:** Properly integrated with GraphQL client. ✓
- **StableLayer SDK:** Integrated for mint/burn flows (buildMintTx, buildBurnTx). ✓
- **PTB composability:** Atomic mint+pay in a single transaction — this is idiomatic Sui. ✓
- **On-chain activity:** Zero. ✗
- **Walrus/Seal:** Not used. N/A

## Overall Assessment
**Strong architecture, zero deployment.** Stableflow Checkout is one of the most well-engineered submissions in terms of code quality, structure, and Sui SDK usage. The monorepo is clean, the Move contract is properly designed with generics, the frontend demonstrates deep Sui SDK knowledge (coin selection, PTB composition, event querying), and the local agent is a thoughtful addition. The "Atomic Mint+Pay" concept using PTBs is genuinely creative and leverages Sui's unique capabilities. The AI disclosure is exemplary — 6 detailed prompt logs showing the AI-assisted development process.

**However, the critical gap is that nothing is deployed.** The Move contract has `0x0` addresses, no package ID exists in the codebase, and the live site runs in smoke mode with fake data. For a hackathon submission, this means the working demo requirement is not fully met — the architecture works in theory but hasn't been validated on-chain.

**Shortlist recommendation: Borderline — exceptional code quality and architecture, but undeployed contract and smoke-mode demo significantly limit verifiability. Would be a strong 8+ across the board if deployed with real transactions.**
