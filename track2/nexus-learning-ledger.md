# Nexus Learning Ledger — Audit

## Project Info
| Field | Value |
|-------|-------|
| **DeepSurge ID** | `7525b635-0daa-4dcd-9b9d-9d9f57ce70db` |
| **Name** | Nexus Learning Ledger |
| **Track** | Local God Mode |
| **GitHub** | https://github.com/Zackmendel/nexus-learning-ledger |
| **Website** | N/A (points to GitHub) |
| **Demo Video** | https://youtu.be/p7RmilkvTwM (3:42, no CC) |
| **Package ID** | None listed |
| **Network** | Testnet |
| **Listed** | True |
| **Submitted** | 2026-03-04T06:50:58.698Z |

## Description
Autonomous AI agent that extracts trading strategies from YouTube educational content, stores them on Walrus decentralized storage, and anchors "Proof-of-Learning" on the Sui blockchain. Creates verifiable, permanent memory layer for AI agents.

## Eligibility Checklist
- [x] Submitted to DeepSurge
- [x] Developed by AI agents (agent extracts content autonomously)
- [x] Uses at least one Sui Stack component — Move contract for LearningEntry/Registry, Walrus (described)
- [x] Working demo verifiable by humans — Video shows terminal + YouTube extraction flow
- [ ] Complete DeepSurge profile with wallet address
- [ ] ⚠️ **GitHub repo is severely incomplete** — only Move contracts + README pushed (6 files), but video shows 408 files locally

## Evaluation Scores
| Criteria | Score (1-10) | Notes |
|----------|:------------:|-------|
| Technical Merit | 5 | **Major issue: GitHub repo only has 6 files** (2 Move contracts, README, .gitignore, Move.toml, Move.lock). The demo video shows 408 files locally including `memory_flash.py`, `nexus_daemon.sh`, `registration.sh`, `extraction_suite.ts`, `trading.ts`. None of this code was pushed to GitHub. The Move contracts themselves are well-designed: LearningEntry (key object with title, content_id, walrus_blob_id, extracted_at, agent, category), LearningRegistry (per-agent with entry count, capability pattern via RegistryCap), proper events (LearningRecorded). `learning_ledger.move` is ~100 lines of clean, well-structured code. But we can't evaluate 95% of the project because it wasn't pushed. |
| Creativity | 7 | "Proof-of-Learning" is a compelling and original concept — AI agents that create verifiable trails of what they've learned, when, and from where. The architecture of YouTube extraction → Walrus storage → Sui anchoring is a natural pipeline. The agent economy angle (portable, auditable knowledge) is forward-thinking. The specific focus on trading strategies from YouTube is practical and differentiated. Good README that clearly explains the vision. |
| Problem-Solution Fit | 5 | The problem (AI agents lack verifiable memory trails) is real and relevant for an agent economy. The solution (decentralized storage + blockchain anchoring) is appropriate. However: (1) We can't verify the extraction/storage pipeline works because the code isn't on GitHub. (2) No package ID means the contract wasn't deployed. (3) The video shows it partially working but doesn't show Walrus upload or Sui transactions. (4) The concept is strong but execution proof is missing. |
| Sui Integration | 4 | **Move contract** (`learning_ledger.move`): Well-designed with LearningEntry (stores walrus_blob_id), LearningRegistry (per-agent state), RegistryCap (authorization). Proper use of shared objects, events, Clock for timestamps. However: (1) **No package ID** — contract was NOT deployed to testnet. (2) **No on-chain activity** verifiable. (3) The main `nexus.move` module is empty (boilerplate). (4) Walrus integration is described but code isn't in repo. (5) No @mysten/sui SDK usage visible (the TypeScript files that presumably use it aren't in the repo). |

**Total: 21/40**

## Demo Verification
- **Video** (3:42, no CC, 1 view, by "Isaac Samuel"):
  - **0:00-0:15** — Terminal showing project directory listing, scrolling through file names
  - **0:15-0:40** — Shows 408 files in 41 directories — significantly more than what's on GitHub (6 files)
  - **0:40-1:30** — Terminal commands, navigation through extraction scripts
  - **1:30-2:30** — YouTube browser view showing TradingLab channel content. Video extraction happening — "Price action. Probably one of the most important aspects of trading with technical analysis." Multiple trading videos visible with analysis panel.
  - **2:30-3:42** — Continued extraction process, file listing
  - **Assessment:** The demo shows the agent autonomously browsing YouTube and extracting content. The local project appears to be a substantial codebase (408 files). **However, the critical issue is that this codebase was not pushed to GitHub.** No Walrus uploads or Sui transactions are shown in the video.

## Code Review Notes
- **Move contract** (`learning_ledger.move`, ~100 lines): Clean and well-designed.
  - `LearningEntry` (key object): title, content_id, walrus_blob_id, extracted_at (Clock timestamp), agent address, category
  - `LearningRegistry` (key object): per-agent state with total_entries counter
  - `RegistryCap`: Capability-based authorization for recording entries
  - `init_registry()`: Creates registry + cap, transfers both to sender
  - `record_learning()`: Creates entry, emits LearningRecorded event, increments counter, transfers to owner
  - Uses Clock for timestamps, proper event emission, shared object patterns
- **Main module** (`nexus.move`): Empty — only boilerplate comment
- **README**: Excellent documentation. Clear architecture diagrams, tech stack table, Getting Started guide. Describes full pipeline: YouTube → Extraction Engine → Walrus Blob Storage → Sui Chain Anchor → Daily Report.
- **Missing from repo**: All agent code (extraction_suite.ts, trading.ts, memory_flash.py, nexus_daemon.sh, registration.sh), Walrus client, Sui client, browser automation, configuration files. These exist locally per the video but weren't committed.
- **1 commit**: "Initial commit: Nexus Learning Ledger smart contracts"

## Sui Integration Analysis
- **Move contract:** ✅ Well-designed but NOT deployed. No package ID.
- **On-chain activity:** ❌ Nothing deployed or executed.
- **Walrus:** ❌ Referenced in architecture and Move contract (walrus_blob_id field) but no Walrus code in repo.
- **@mysten/sui SDK:** ❌ Not in repo (likely in the unpushed code).
- **Seal/dapp-kit:** ❌ Not used.

## Overall Assessment
Nexus Learning Ledger has an excellent concept (Proof-of-Learning with verifiable agent memory) and a well-designed Move contract. The README is thorough and the architecture is compelling. The demo video shows a real project with 408 files running locally.

However, the fatal flaw is that **the codebase wasn't pushed to GitHub**. Only the Move contracts and README are in the repo. We cannot evaluate:
- The extraction engine
- The Walrus integration
- The Sui client / transaction building
- The browser automation
- The agent orchestration

Additionally, no package was deployed to testnet, so there's no on-chain proof of anything working. The project likely works locally but fails the submission requirement of having reviewable code.

**Shortlist recommendation: No** (would reconsider if code were pushed and contract deployed)
