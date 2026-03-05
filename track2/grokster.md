# Grokster — Audit

## Project Info
| Field | Value |
|-------|-------|
| **DeepSurge ID** | `cc618fac-91e0-449d-9bbc-4d15ca8d4747` |
| **Name** | Grokster |
| **Track** | Local God Mode |
| **GitHub** | https://github.com/Sergey1997/grokster |
| **Website** | https://grokster-nine.vercel.app/ |
| **Demo Video** | None (YouTube link points to GitHub repo) |
| **Package ID** | None |
| **Network** | None |
| **Listed** | True |
| **Submitted** | 2026-02-21T08:08:01.126Z |

## Description
AI agent prediction market platform where agents compete by betting on real-world events (crypto, stocks, sports, politics). Agents start with $2,500 simulated funds. Leaderboard-based competition. Claims to be "Built on the SUI blockchain" with Polymarket integration planned.

## Eligibility Checklist
- [x] Submitted to DeepSurge
- [ ] Developed by AI agents — unclear, appears to be a standard web app
- [ ] Uses at least one Sui Stack component — **NO SUI INTEGRATION WHATSOEVER**
- [ ] Working demo verifiable by humans — Website returns 200 but demo video is missing (link points to GitHub)
- [x] Complete DeepSurge profile with wallet address

## Evaluation Scores
| Criteria | Score (1-10) | Notes |
|----------|:------------:|-------|
| Technical Merit | 5 | ~7,583 LOC TypeScript, 12 commits. Full-stack Next.js app with Supabase backend. Admin dashboard, agent API (auth with math challenges, betting, portfolio, events), leaderboard, event resolution. Well-structured with proper API routes, Zod validation, components. However: no blockchain code, no Move contracts, no SDK integration. It's a centralized web2 app with simulated balances in a SQL database. |
| Creativity | 5 | AI agent prediction markets is an interesting concept — agents competing on forecasting accuracy with public leaderboards. The idea of using prediction markets to evaluate AI capabilities has real potential. However: (1) no actual AI agent integration beyond API endpoints, (2) Polymarket integration is "planned" not built, (3) simulated funds only (no real economics). |
| Problem-Solution Fit | 4 | The platform could be interesting as a benchmark for AI prediction capabilities, but: (1) no actual Sui integration despite claiming to be "built on SUI blockchain", (2) balances are simulated SQL records, not tokens, (3) no smart contracts for trustless resolution, (4) centralized admin resolves events manually. The SQL database approach defeats the purpose of a prediction market. |
| Sui Integration | 1 | **Zero Sui integration.** No Move contracts. No @mysten/sui SDK. No Walrus. No Seal. No dapp-kit. No package ID. No network deployment. The description claims "Built on the SUI blockchain" but the entire app runs on Supabase with centralized SQL databases. Agents have simulated $2,500 balances stored in PostgreSQL. This does not meet the hackathon requirement of using at least one Sui Stack component. |

**Total: 15/40**

## Demo Verification
- **Video:** None (YouTube link points to GitHub repo — broken submission)
- **Website:** Returns HTTP 200, assumed live
- **On-chain:** Nothing to verify — no package, no transactions

## Code Review Notes
- **Next.js app** with Supabase backend, Tailwind CSS, TypeScript
- **Agent API** (`/api/v1/agent/`): Auth (init/verify with math challenges), bets, portfolio, events, API keys, comments
- **Admin API** (`/api/admin/`): Event management, agent management, simulation, resolution
- **Database:** PostgreSQL via Supabase — agents, auth_sessions, api_keys, events, bets, comments
- **Frontend:** Events listing, agent profiles, leaderboard, admin dashboard
- **12 commits** — mostly initialization and updates

## Sui Integration Analysis
- **Move contracts:** ❌ None
- **@mysten/sui SDK:** ❌ Not in dependencies
- **Walrus:** ❌ Not used
- **Seal:** ❌ Not used
- **dapp-kit:** ❌ Not used
- **On-chain activity:** ❌ None

## Overall Assessment
Grokster is a well-built web2 prediction market platform, but it has **zero Sui blockchain integration** despite claiming to be "Built on the SUI blockchain." The entire system runs on centralized Supabase with SQL databases. There are no Move contracts, no SDK usage, no Walrus, no Seal — none of the required Sui stack components.

The concept (AI agents competing in prediction markets) has potential, but in its current state it's a standard Next.js/Supabase app that doesn't meet the hackathon's core requirement of Sui integration.

**Shortlist recommendation: No** — fails core eligibility (no Sui integration)
