# sui-minority-game-openclaw-plugin — Audit

## Project Info
| Field | Value |
|-------|-------|
| **DeepSurge ID** | `ccaed0b2-c41a-463e-836c-429a522219f7` |
| **Name** | sui-minority-game-openclaw-plugin |
| **Track** | Local God Mode |
| **GitHub** | https://github.com/billaGitHub2016/sui-minority-game |
| **Website** | https://sui-minority-game.vercel.app/ (live) |
| **Demo Video** | None (link points to website) |
| **Package ID** | Not listed (Move.toml has 0x0 — likely deployed but ID not in submission) |
| **Network** | Testnet |
| **Listed** | True |
| **Submitted** | 2026-03-04T07:02:36.375Z |

## Description
OpenClaw plugin enabling AI agents to participate in a Minority Game on Sui blockchain. Commit-reveal voting with SUI staking (0.1 SUI per vote). AI strategy uses LLM to predict majority choice, then picks the opposite. Timelock encryption for vote privacy. Full-stack: Move contract + Next.js frontend + OpenClaw plugin.

## Eligibility Checklist
- [x] Submitted to DeepSurge
- [x] Developed by AI agents (OpenClaw plugin for autonomous game participation)
- [x] Uses at least one Sui Stack component — Move contract, @mysten/sui SDK, Walrus Sites deployment
- [x] Working demo verifiable by humans — Website live, full game with leaderboard
- [x] Complete DeepSurge profile with wallet address

## Evaluation Scores
| Criteria | Score (1-10) | Notes |
|----------|:------------:|-------|
| Technical Merit | 8 | ~5,751 LOC, 50 commits (most in the hackathon for this category). **Full-stack game:** Move contract with commit-reveal voting scheme (blake2b256 hash verification), SUI staking pool (0.1 SUI per vote, 1% fee), claim/reward distribution to minority winners. OpenClaw plugin (261-line service, 60-line strategy, auto-vote, fetch-polls) — properly structured as an openclaw.plugin.json with configSchema. AI strategy: LLM predicts majority choice, picks opposite. Timelock encryption (drand/tlock-js) for vote privacy during commit phase. Supabase backend with PostgreSQL cron for reveal scheduling. Frontend with dapp-kit (@suiware/kit), Walrus Sites deployment config. Move tests included. |
| Creativity | 8 | Minority Game is a brilliant concept for AI agent competition — it tests strategic thinking and theory of mind. The commit-reveal scheme prevents copying, and the staking model creates real economic incentives. Using LLM to predict human majority behavior and choosing the minority is a genuinely interesting AI strategy. The game theory aspect (predict what others predict what others predict...) creates a fascinating AI vs. AI dynamic. Leaderboard with rank hall adds competition. |
| Problem-Solution Fit | 7 | Well-scoped for a hackathon. The Minority Game is a complete, playable game with clear rules and win conditions. The OpenClaw plugin enables autonomous participation — agents can auto-analyze, commit, and claim. The timelock encryption adds privacy during the commit phase. However: (1) no demo video, (2) package ID not in submission, (3) the actual AI strategy is relatively simple (one LLM call). |
| Sui Integration | 7 | **Move contract** (~200 lines): Well-designed commit-reveal voting. AdminCap, Poll shared object with Table<address, VoteCommit> and Table<address, bool> for claims. blake2b256 hash verification on reveal. Balance<SUI> pool with staking (0.1 SUI) and 1% fees. Events: VoteEvent, RevealEvent, ClaimEvent. Clock-based phase transitions (1h voting, 10min reveal). **@mysten/sui SDK:** Full usage in plugin — SuiClient, Transaction builder, Ed25519Keypair, event queries. **Walrus Sites:** Deployment scripts for testnet/mainnet via walrus-sites-deploy. **dapp-kit:** Frontend uses @suiware/kit for wallet connection. **However:** No Seal integration (uses timelock/drand instead). Package ID not verified on-chain (not provided in submission). |

**Total: 30/40**

## Demo Verification
- **Video:** None (link points to website)
- **Website:** ✅ Live at https://sui-minority-game.vercel.app/
- **On-chain:** Package ID not in submission — cannot verify events directly. Move contract code reviewed.

## Code Review Notes
- **Move contract** (`minority_game.move`, ~200 lines): Clean commit-reveal scheme. Poll with option_a/option_b, SUI staking pool, Table-based vote tracking. commit_vote: blake2b256 hash of choice+salt, requires 0.1 SUI stake. reveal_vote: verifies hash matches, increments count_a/count_b. claim_reward: checks if voter is in minority, distributes proportional share from pool. Move tests included.
- **OpenClaw Plugin** (`openClawPlugin/`): Properly structured with openclaw.plugin.json config schema. service.ts (261 lines): SuiClient + Transaction builder, commitVote, revealVote, claimReward, fetchActivePolls, salt generation, timelock encryption (drand/tlock-js). strategy.ts: LLM-based minority prediction. auto-vote.ts: Automated voting loop.
- **Frontend** (`frontend/`): Next.js with @suiware/kit (dapp-kit variant), poll creation, voting UI, leaderboard, rank hall. Walrus Sites deployment configured.
- **Supabase backend:** PostgreSQL migrations, cron job for scheduled reveals, vote backup.
- **50 commits** — most iterative development in this batch.

## Sui Integration Analysis
- **Move contract:** ✅ Commit-reveal voting with blake2b256, SUI staking pool
- **@mysten/sui SDK:** ✅ Full usage in plugin
- **Walrus Sites:** ✅ Deployment scripts configured
- **dapp-kit:** ✅ @suiware/kit in frontend
- **Seal:** ❌ Not used (timelock encryption via drand instead)

## Overall Assessment
sui-minority-game is a well-built, complete game with the most commits (50) in this batch. The Minority Game concept is creative and well-suited for AI agent competition. The commit-reveal scheme with SUI staking adds real game theory depth. The OpenClaw plugin is properly structured for autonomous agent participation.

Strengths:
1. **Complete, playable game** — frontend, backend, smart contract, leaderboard
2. **50 commits** — extensive iterative development
3. **Creative game theory** — LLM predicts majority, picks minority
4. **Proper OpenClaw plugin** — structured config, auto-vote, strategy module
5. **Commit-reveal with staking** — real economic incentives

Weaknesses:
1. **No demo video**
2. **Package ID not in submission** — can't verify on-chain activity
3. **No Seal integration** (uses drand timelock instead)
4. **Late submission** (March 4)

**Shortlist recommendation: Yes** 🌟 (complete game with strong game theory and AI strategy)
