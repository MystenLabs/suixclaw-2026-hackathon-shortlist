# Sui Jarvis — Audit

## Project Info
| Field | Value |
|-------|-------|
| **DeepSurge ID** | `0afb1515-3cf8-415f-a10c-d833de7c9fa7` |
| **Name** | Sui Jarvis (Sui DeFi Jarvis — The Infinite Money Glitch) |
| **Track** | Local God Mode |
| **GitHub** | https://github.com/wrx1234/sui-hackathon |
| **Website** | https://suijarvis.w3xuan.xyz/ |
| **Demo Video** | https://youtu.be/BV4nZ9ixOZw (1:54, no CC) |
| **Package ID** | `0x737a73b3a146d45694c341a22b62607e5a6e6b6496b91156217a7d2c91f7e65d` |
| **Network** | Testnet |
| **Listed** | True |
| **Submitted** | 2026-03-03T19:33:15.017Z |

## Description
Autonomous AI agent on OpenClaw managing DeFi on Sui. Earns via Cetus Aggregator (multi-DEX swap routing), logs actions on Walrus, protects with Seal encryption. Features Telegram bot interface, social sniper (AI-driven tweet analysis → auto-trade), strategy engine (trend/mean-reversion/momentum), risk management, and a polished frontend with 3D elements.

## Eligibility Checklist
- [x] Submitted to DeepSurge
- [x] Developed by AI agents (~80% AI-generated per AI_DISCLOSURE.md)
- [x] Uses at least one Sui Stack component — Cetus Aggregator, Move contract, Walrus logging, Seal (referenced), dapp-kit
- [x] Working demo verifiable by humans — Telegram bot demo video shows real swap flows
- [ ] Complete DeepSurge profile with wallet address

## Evaluation Scores
| Criteria | Score (1-10) | Notes |
|----------|:------------:|-------|
| Technical Merit | 8 | Comprehensive ~16,684 LOC project with 42 commits. Real agent architecture: wallet management (Ed25519 keypair, balance queries), Cetus Aggregator SDK integration (multi-DEX routing across Cetus/DeepBook/Kriya/FlowX/Turbos/Aftermath), strategy engine with 3 modes (trend/mean_reversion/momentum), risk management (stop-loss, daily limits, max drawdown, emergency stop, trailing stop), Walrus logging with 5-min auto-flush, social sniper module (tweet monitoring → sentiment analysis → auto-trade). 826 lines of tests across 8 test files. Move contract (vault.move) is well-designed with deposit/withdraw, trade/strategy/risk event logging, VaultCap access control, and configurable limits. Frontend is polished with shadcn, Spline 3D, i18n. Website is live. |
| Creativity | 8 | "Self-sustaining AI trading agent" is an ambitious and compelling vision. The architecture of connecting social signal analysis → AI decision → DeFi execution → on-chain audit trail is well-thought-out. Social Sniper (monitor tweets → analyze sentiment → auto-trade → post reply) is a creative integration. The Telegram bot UX with swap quotes showing multi-hop routes, confidence levels, and stop-loss prices shows real product thinking. The "Infinite Money Glitch" framing is fun. |
| Problem-Solution Fit | 7 | The problem (autonomous DeFi portfolio management) is real and relevant. The solution addresses multiple angles: execution (Cetus multi-DEX), safety (risk limits, emergency stop, Vault cap-based access control), transparency (Walrus audit logs), and user control (Telegram commands). However: zero on-chain events means it hasn't actually traded. The strategy engine relies on Cetus quotes for price data rather than real market feeds. Social module is mostly stubs (Twitter API not connected). The vision outpaces the execution. |
| Sui Integration | 7 | **Strong Sui stack breadth:** (1) Move contract deployed on testnet — real Vault with deposit/withdraw, event logging, access control via VaultCap. Well-structured. (2) Cetus Aggregator SDK — real `findRouters()` + `fastRouterSwap()` integration for multi-DEX routing. (3) @mysten/sui SDK — SuiClient, Ed25519Keypair, Transaction objects, proper RPC calls. (4) Walrus — log upload via publisher REST API with blob ID tracking. (5) Seal mentioned in README/architecture but usage in code is minimal (encryption referenced but not imported). **However:** Zero on-chain events. Package exists but was never called. No actual swaps executed on testnet. |

**Total: 30/40**

## Demo Verification
- **Video** (1:54, no CC available):
  - **0:02** — Live Dashboard with Swap/Sniper/Yield/Portfolio tabs, recent activity showing "SUI → CETUS Swap +$42.50"
  - **0:20** — Telegram bot (@SuiJarvisBot) swap flow: 1.0 SUI → 3.845003 USDC, Route: Cetus → DeepBook → Aftermath, 3 DEXes, 5 pools, 0.5% slippage, Execute/Cancel buttons
  - **0:40** — Social Sniper: AI analysis of @CryptoAnalyst99 tweet → Bearish 85% → SELL 2000 CETUS @ $0.089 → +1.4%. @DegenTrader tweet → Bullish 78% → BUY 5000 NAVX @ $0.248 → +3.8%. Auto-reply posted.
  - **1:10** — Strategy signals: HOLD WETH/USDC (55%), BUY HASUI/SUI (80% confidence), today 5 signals / 73% win rate. Based on EMA/RSI/MACD/Volume/on-chain data.
  - **Note:** The demo appears to show a UI mockup / simulated Telegram interactions rather than live on-chain execution. The prices and results look pre-composed. No Suiscan tx links shown.
- **Website** (suijarvis.w3xuan.xyz): ✅ Live, polished landing page with Features/Sniper/Architecture/Dashboard sections, i18n (EN/CN), "Launch Bot" button.

## Code Review Notes
- **Agent core** (`agent/`): Well-separated modules — main.ts (orchestrator), wallet.ts (Ed25519 management + balance), swap.ts (Cetus Aggregator), strategy.ts (3 strategy modes with price history), risk.ts (comprehensive limits + violations tracking), logger.ts (Walrus + local JSONL), social.ts (Twitter monitoring stubs + sentiment).
- **Move contract** (`vault.move`, ~250 lines): Well-designed. Shared Vault object with Balance<SUI>, VaultCap for owner-gated operations. 5 event types (Deposit, Withdraw, Trade, Strategy, Risk). Configurable single/daily trade limits, pause toggle. Clean code with proper error codes.
- **Tests** (826 LOC): wallet.test.ts, strategy.test.ts, risk.test.ts, logger.test.ts, social.test.ts, integration.test.ts, e2e.test.ts. Comprehensive coverage.
- **Frontend** (`frontend/`): Vite + React + shadcn/ui + TailwindCSS + Spline 3D. Polished with animations, glass effects, dark theme. Deployed at custom domain.
- **AI Disclosure** (`AI_DISCLOSURE.md`): Transparent — lists AI tools used, contribution ratio (~80%), key prompts. Good practice.
- **42 commits**: Healthy development history showing iterative refinement.

## Sui Integration Analysis
- **Move contract:** ✅ Deployed on testnet. Real Vault with deposit/withdraw + event logging. VaultCap access control pattern. Well-structured.
- **Cetus Aggregator SDK:** ✅ `@cetusprotocol/aggregator-sdk` with `findRouters()` for multi-DEX routing and `fastRouterSwap()` for execution. Real SDK integration, not just API calls.
- **@mysten/sui:** ✅ SuiClient (via SuiJsonRpcClient), Ed25519Keypair, Transaction, getBalance, getAllBalances.
- **Walrus:** ✅ Upload via publisher REST API, blob ID tracking, auto-flush interval.
- **Seal:** ⚠️ Referenced in README/architecture but minimal code evidence of actual Seal SDK usage.
- **On-chain activity:** ❌ Zero events. Package deployed but never called. No actual swaps on chain.

## Overall Assessment
Sui Jarvis is one of the more ambitious and well-rounded submissions — a full DeFi agent with swap execution, strategy engine, risk management, social signal analysis, Walrus audit logging, and a polished frontend. The code quality is good, architecture is well-separated, and the Sui stack integration is broad (Cetus, Move, Walrus, dapp-kit). The demo video effectively shows the intended UX.

However, the project appears to be more vision than execution at this point:
1. **Zero on-chain activity** — the Vault contract was never used
2. **Demo appears simulated** — no live tx hashes visible
3. **Social module is stubs** — Twitter API not actually connected
4. **Strategy engine has no real market data feeds**

The breadth is impressive, but depth of actual working functionality is limited. This is a solid proof-of-concept that could become a real product.

**Shortlist recommendation: Maybe** (borderline — strong vision and architecture, but limited proof of working end-to-end)
