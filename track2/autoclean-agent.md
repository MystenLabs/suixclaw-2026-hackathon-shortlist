# AutoClean Agent — Audit

## Project Info
| Field | Value |
|-------|-------|
| **DeepSurge ID** | `e0cbc19c-153d-43f3-9bf2-c1b7d5ef9a08` |
| **Name** | AutoClean Agent (Deepurge) |
| **Track** | Local God Mode |
| **GitHub** | https://github.com/samuelcampozano/deepurge-autoclean-agent |
| **Website** | https://github.com/samuelcampozano/deepurge-autoclean-agent |
| **Demo Video** | https://youtu.be/6JnrVI59Hbc |
| **Package ID** | `0x9347b087370be9ddda2caad8dfcef4db4500a62c3505691925b5890f9830ee9a` |
| **Network** | Testnet |

## Eligibility Checklist
- [x] Submitted to DeepSurge
- [x] Developed by AI agents (or mostly AI agents)
- [x] Uses at least one Sui Stack component
- [x] Working demo verifiable by humans
- [x] Complete DeepSurge profile with wallet address

## Demo Verification
- YouTube video exists: **Yes** — titled "SUI X OPENCLAW AGENT HACKATHON - Autonomous Ai agent"
- Real demo: Shows the agent monitoring a Downloads folder, classifying files, moving them to organized folders, and logging to Walrus. Dashboard visible with live agent stats, blob explorer, and blockchain verification panel.
- On-chain verification: Package ID verified on Sui Testnet — **exists as `package` type** ✅

## Code Review Notes
- **Repo structure:** Python-based agent with 10 source files, Move contract, Flask dashboard, Docker deployment
- **Lines of code:** ~3,636 lines of Python + ~90 lines of Move + ~400 lines dashboard
- **Move contract:** `deepurge_anchor.move` — a Registry shared object mapping date → SHA-256 root hash. Uses Table, events, ownership checks. Simple but well-structured and purpose-built.
- **Agent code (agent.py):** Full-featured file monitoring agent using Watchdog. File classification, duplicate detection via SHA-256, timestamped renaming, retry logic, workflow engine, vault encrypted backups.
- **Walrus integration (walrus_logger.py):** Real HTTP REST API calls to Walrus Publisher (`PUT /v1/blobs?epochs=N`). Handles `newlyCreated` and `alreadyCertified` responses correctly. Batch uploads, session summaries, daily reports.
- **Sui anchor (sui_anchor.py):** Uses Sui JSON-RPC directly (no pysui). Computes root hash from daily reports, calls `unsafe_moveCall` to anchor on-chain. Falls back to local ledger when contract not configured.
- **Vault (vault.py):** AES-256-GCM encryption before uploading to Walrus. Complete encrypt → upload → manifest flow.
- **Dashboard:** Flask web UI with agent control, blob explorer, category editor, statistics.
- **Docker:** docker-compose.yml, Dockerfiles for both agent and dashboard. Production-ready deployment.
- **Quality:** Good error handling, logging, configuration system. Code reads like it was written with care.

## Sui Integration Analysis
**Meaningful integration of multiple Sui stack components:**
- **Move smart contract** — Registry for daily report root hashes. Deployed on testnet. Uses Table, events, ownership assertions. Purpose-built for the use case.
- **Walrus** — Real REST API integration for blob uploads. Action logs, daily reports, session summaries all uploaded to Walrus testnet. Correct endpoint usage (`/v1/blobs`).
- **Sui JSON-RPC** — Direct RPC calls for anchoring root hashes on-chain. Falls back gracefully to local ledger.
- **On-chain integrity proof** — Daily SHA-256 root hashes anchored on Sui, providing tamper-evident audit trail for file management actions.

**Missing:** No `@mysten/sui` SDK usage (Python project), no dapp-kit, no Seal integration (uses custom AES-256-GCM instead).

## Evaluation Scores
| Criteria | Score (1-10) | Notes |
|----------|:------------:|-------|
| Technical Merit | 7 | Solid, complete implementation. ~4K lines with Move contract, Walrus integration, encrypted vault, Docker deployment, dashboard. Well-architected with good error handling. |
| Creativity | 6 | File organizer is a well-known concept but the Walrus logging + on-chain integrity anchoring adds a novel decentralized audit trail angle. The "black box for file management" framing works. |
| Problem-Solution Fit | 6 | The core problem (messy Downloads folder) is real but low-stakes. The blockchain anchoring is interesting for compliance/audit use cases but feels like a stretch for personal file management. |
| Sui Integration | 6 | Genuine Walrus usage (REST API) and Move contract for root hash anchoring. Package deployed and verified. Not the deepest integration but it's real and purposeful. |

## Red Flags
- None significant. The project is honest about what it does.
- Package ID in submission has `/tx-blocks` suffix which is odd but the base ID verifies.

## Overall Assessment
**Solid mid-tier project.** AutoClean Agent is a well-executed local-first agent that genuinely uses Walrus for decentralized logging and Sui for integrity anchoring. The codebase is substantial and functional — not boilerplate. The Docker deployment and dashboard show polish.

The main limitation is the problem space: file organization is useful but not high-impact, and the blockchain components (while real) feel somewhat bolted onto a problem that doesn't inherently need them. Still, it's a complete, working project with verified on-chain activity.

**Shortlist recommendation: Maybe — middle of the pack for Track 2. Solid execution but limited ambition.**
