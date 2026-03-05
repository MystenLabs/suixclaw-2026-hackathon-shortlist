# Watchdog — Audit

## Project Info
| Field | Value |
|-------|-------|
| **DeepSurge ID** | `a3916732-25c4-4d35-ad1f-ea7873ddca70` |
| **Name** | Watchdog (formerly Noctua) |
| **Track** | Local God Mode |
| **GitHub** | https://github.com/cl-fi/noctua |
| **Website** | https://noctua-landing-page.vercel.app/ |
| **Demo Video** | https://www.loom.com/share/a58d2aa63d124cd98e88192adf9ae4c9 (not watched — browser unavailable) |
| **Package ID** | None (uses NAVI Protocol SDK directly) |
| **Network** | **Mainnet** |
| **Listed** | True |
| **Submitted** | 2026-03-04T04:44:56.019Z |

## Description
Autonomous AI agent that monitors NAVI Protocol lending positions on Sui, uses Gemini LLM for intelligent risk analysis and dynamic threshold calibration, and executes atomic flash loan deleveraging in a single PTB when health factor drops below trigger. Telegram bot for remote control. Walrus audit trail for every unwind operation.

## Eligibility Checklist
- [x] Submitted to DeepSurge
- [x] Developed by AI agents (Gemini Brain for analysis + decision making, OpenClaw skills)
- [x] Uses at least one Sui Stack component — NAVI SDK (flash loans, lending), Sui PTB, Walrus storage
- [x] Working demo verifiable by humans — **Mainnet flash loan TX verified on SuiScan**
- [x] Complete DeepSurge profile with wallet address

## Evaluation Scores
| Criteria | Score (1-10) | Notes |
|----------|:------------:|-------|
| Technical Merit | 10 | Exceptional engineering. ~2,156 LOC TypeScript, 19 commits showing iterative optimization (progressive backoff, position caching, token filter reducing 102 RPC calls → ~6, slippage fixes). **The flash loan unwind is a single atomic PTB**: flash loan → repay debt → withdraw collateral → oracle update → swap → repay flash loan. Uses NAVI SDK's `flashloan()`, `repayDebt()`, `withdrawCoin()`, `swapPTB()`, `repayFlashLoan()` all in one transaction. Gemini Brain with function-calling tools (get_position, execute_unwind, get_history, get_walrus_trace, update_rule). SUI price volatility analysis via CoinGecko for dynamic threshold calibration. Telegram bot with natural language → LLM routing. Health factor calculation with proper LTV math. Three strategies (collateral_swap, wallet_repay, full_exit). Retry logic with progressive backoff. Position caching. Token filter optimization. |
| Creativity | 10 | This is the most practical and immediately useful project in the entire hackathon. DeFi liquidation protection is a real, urgent problem — people lose 35% of their collateral because they were asleep. An AI agent that monitors positions, dynamically adjusts risk thresholds using LLM analysis of market volatility, and autonomously executes flash loan unwinding is genuinely novel. The atomic flash loan PTB (5 operations in one transaction) is elegant. Using LLM for risk calibration rather than static thresholds shows sophisticated thinking. OpenClaw skills for different operations (monitor, protect, history). |
| Problem-Solution Fit | 10 | **Perfect problem-solution alignment.** The problem (DeFi liquidation losses from unmonitored positions) is real, measurable, and affects every DeFi user. The solution is comprehensive: (1) 60-second monitoring cycle, (2) LLM-driven analysis with market volatility context, (3) Atomic flash loan execution — no partial state risk, (4) Three strategies for different scenarios, (5) Telegram alerts with SuiVision TX links, (6) Walrus audit trail. And crucially — **it actually works on mainnet with real money.** TX `9VqeBU...` is a real flash loan unwind verified on SuiScan with 48 events. |
| Sui Integration | 8 | **Deep Sui protocol integration:** (1) **NAVI Protocol SDK** — full usage: flashloan, repayDebt, withdrawCoin, swapPTB, repayFlashLoan, oracle updates, position queries, health factor calculation. (2) **Sui PTB** — single atomic transaction with 5+ operations. Uses `@mysten/sui/transactions` Transaction builder. (3) **Walrus** — real audit trail uploads. Unwind traces stored on Walrus with full details (trigger HF, restored HF, strategy, amounts, TX digest, gas). Verified: `ERhJKNU1lrxXdaZ5utsS1CGFfIJc92aKFnl9VQCVET8` contains actual execution data. (4) **Mainnet execution** — not testnet play money, real SUI and real USDC. **However:** No custom Move contracts (uses NAVI's existing contracts). No Seal usage. No dapp-kit (Telegram-only interface). |

**Total: 38/40**

## Demo Verification
- **Loom video** (not watched — browser unavailable during review).
- **On-chain verification (compensates for missed video):**
  - **Mainnet TX verified**: `9VqeBUPdBCjwLD4LxqcP7gdDxoL4djUNxFZKz7k2MLQe` — success, 48 events, real gas costs
  - **Walrus audit trail verified**: `ERhJKNU1lrxXdaZ5utsS1CGFfIJc92aKFnl9VQCVET8` contains:
    - triggerHF: 1.424
    - strategy: collateral_swap
    - collateralSold: 0.271916 SUI
    - debtRepaid: 0.241525 nUSDC
    - swapRoute: Sui → nUSDC (NAVI Aggregator)
    - txDigest matches the on-chain TX
  - **SuiScan link**: https://suiscan.xyz/mainnet/tx/9VqeBUPdBCjwLD4LxqcP7gdDxoL4djUNxFZKz7k2MLQe

## Code Review Notes
- **flashloan-unwind.ts** (~150 lines): Core engine. Single PTB with 6 steps: register structs → flash loan → oracle update → repay debt → withdraw collateral → swap → repay flash loan. Handles ESM/CJS dual-package issues with `createRequire`. Proper error handling with try/catch.
- **navi-client.ts** (~200 lines): NAVI SDK wrapper. Position queries, health factor calculation, price caching (15 min), position caching (30s), active token filter (reduces 102 RPC calls to ~6 after first fetch). Supports all 20+ NAVI token types.
- **gemini-brain.ts** (~200 lines): Gemini 3 Flash Preview model. Two modes: (1) Monitor — structured JSON analysis for shouldAct/shouldWarn decisions, (2) Chat — function-calling with 5 tools for Telegram interaction. Custom system prompt with DeFi risk context.
- **unwind-engine.ts** (~150 lines): Calculates optimal repay amounts using HF math: `newDebt = totalCollateral * avgLTV / targetHF`. Handles flash loan fee (0.5%). Picks largest debt and collateral positions. Records traces to Walrus.
- **walrus-logger.ts** (~50 lines): Clean Walrus upload/download. Stores UnwindTrace as JSON blob. Handles newlyCreated and alreadyCertified responses.
- **price-volatility.ts** (~100 lines): CoinGecko API for SUI 3-day hourly prices. Calculates 24h/72h change, max drawdown, volatility (std/mean). Human-readable kline summary for LLM consumption.
- **telegram-bot.ts** (~100 lines): Grammy framework. /start, /status, /history commands. Natural language messages routed to Gemini Brain. Push alerts with clickable SuiVision links.
- **tools.ts** (~80 lines): Gemini function declarations + ToolHandler class. 5 tools: get_position, execute_unwind, get_history, get_walrus_trace, update_rule.
- **OpenClaw skills** (3): noctua-monitor (position monitoring), noctua-protect (rule config + manual unwind), noctua-history (audit trail queries).

## Sui Integration Analysis
- **NAVI Protocol SDK:** ✅ Deep integration — flash loans, debt repayment, collateral withdrawal, oracle updates, aggregator swaps, position queries, health factor.
- **Sui PTB:** ✅ Single atomic transaction with 5+ moveCall operations. Real mainnet execution.
- **Walrus:** ✅ Real upload and verification. Unwind traces stored with full execution details.
- **Mainnet:** ✅ Not testnet — real money, real flash loans, real debt repayment.
- **Move contracts:** ❌ No custom contracts (uses NAVI's existing contracts directly).
- **Seal/dapp-kit:** ❌ Not used.

## Overall Assessment
Watchdog is the standout project of the hackathon. While other submissions demonstrate concepts on testnet with play money, Watchdog has **actually executed a flash loan deleveraging on Sui mainnet** to protect a real lending position. The Walrus audit trail is intact and verifiable.

The technical execution is exceptional:
1. **Mainnet flash loan atomic unwind** — real money, real protection
2. **LLM-driven risk analysis** — Gemini with function-calling tools, dynamic threshold calibration
3. **Production-quality code** — 19 commits of iterative optimization (caching, retry logic, RPC call reduction)
4. **Complete agent** — monitoring, analysis, execution, Telegram control, audit trail
5. **Real utility** — this is a product someone would actually use

The only weakness is the lack of custom Move contracts (it leverages NAVI's existing contracts), which slightly limits the Sui integration score. But the depth of protocol interaction (flash loans, oracle updates, aggregator swaps in a single PTB) more than compensates.

**Shortlist recommendation: Yes — Strong candidate for top prize** 🌟🌟
