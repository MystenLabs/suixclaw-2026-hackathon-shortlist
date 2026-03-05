# Vigilant — Audit

## Project Info
| Field | Value |
|-------|-------|
| **DeepSurge ID** | `b9f7a7f9-fbc4-48f3-9a83-a9671a528164` |
| **Name** | Vigilant |
| **Track** | Track 1: Safety & Security |
| **Team** | agentboogieai-max (Boogie) |
| **GitHub** | https://github.com/agentboogieai-max/Vigilant |
| **Website** | https://suiscan.xyz/testnet/object/0x80350cfb8d75c2f78576c186af14f0ca3cc2890e2fb4ed22bce3a92a67cb8f84 |
| **Demo Video** | https://youtu.be/waXiRfky6KI?si=JlvBzgPiUi_7DfGN |
| **Package ID** | `0x80350cfb8d75c2f78576c186af14f0ca3cc2890e2fb4ed22bce3a92a67cb8f84` |
| **Network** | Testnet |
| **Submitted** | 2026-02-09T07:05:16.385Z |

## Description
Vigilant is an autonomous agent security system built on Sui. It uses capability tokens to enforce limits on AI bot actions — daily quotas, budgets, and permissions. Before executing any action, the bot validates on-chain. After execution, proof is logged to Walrus and Sui for immutable audit trails. Pitched as "a smart credit card for your AI: controlled, monitored, and secured by blockchain."

## Eligibility Checklist
- [x] Submitted to DeepSurge
- [x] Uses at least one Sui Stack component (Move + Sui CLI + Walrus)
- [x] Working demo (YouTube video exists, asciinema cast, on-chain transactions)
- [x] Demo video (YouTube link resolves — https://youtu.be/waXiRfky6KI)
- [ ] Complete DeepSurge profile with wallet address (unverified)

## Move Compilation
- Move.toml uses `edition = "2024.beta"` and points to testnet rev — standard setup.
- Build artifacts present in `move/build/autosecure_forge/` — compiled successfully on dev machine.
- Package confirmed deployed on testnet via `sui_getObject` — bytecode matches source modules (`security`, `proof`).

## Demo Verification
- **Video:** ✅ YouTube link resolves (HTTP 200). Narration script in repo suggests a 3-minute walkthrough of the full flow: deploy → create capability → detect file → validate on-chain → execute simulation → log proof.
- **Asciinema:** Cast file included (`vigilant-demo.cast`) for terminal replay.
- **On-chain transactions verified (3 total):**
  1. `4psiBwRDgMiFXnQoptGf1eLfZnpwAkUdkkTgBDZmFk2j` — CapabilityCreated (print_preview, quota 10)
  2. `tc3mA5ghShx89DptThyADEBVngK7LGBrJUYMUDmCwxu` — ActionValidated (intent approved)
  3. `BYqos8929foZ24LpWPpPQcN73uFqLbKXD3Xk1fLsvAgT` — ProofStored (walrus://abc123xyz blob ref)
- **Website:** Points to Suiscan object page (not a custom UI). No frontend/dApp — this is a CLI/bot project.

## Code Review Notes

### Repository Structure
```
bot/core.py          — 216 lines — Main autonomous loop (detect → predict → validate → execute → log)
bot/sui_client.py    — 139 lines — Sui CLI wrapper for on-chain calls
bot/simulations.py   — 179 lines — Simulation engine (3D print preview, git sync)
bot/llm.py           —  96 lines — Local LLM integration via Ollama (llama3.2)
bot/proofs.py        —  93 lines — Walrus upload + Sui proof logging
bot/watcher.py       —  88 lines — File system watcher (watchdog-based)
move/sources/security.move — 175 lines — Capability + ActionIntent + validation
move/sources/proof.move    —  66 lines — ProofRecord + Walrus blob reference
config.yaml          —  24 lines — Bot configuration
demo.sh              — 116 lines — Demo script
README.md            —  99 lines — Documentation
NARRATION_SCRIPT.md  —  47 lines — Video narration guide
```

**Total meaningful code: ~1,052 lines** (Python + Move). Plus 116 lines demo script and 146 lines docs.

### Move Contracts (241 lines total)

**security.move (175 lines):**
- `Capability` — Owned object: action_type, daily_quota, used_today, max_cost_usdsui, requires_zklogin, expires_at, is_revoked. Good use of capability pattern.
- `ActionIntent` — Shared object created during validation. Tracks status (1=approved, 2=completed). Links back to capability.
- `validate_action()` — Checks revocation, quota, budget, optional zklogin. Increments used_today. Creates shared ActionIntent. Proper error codes (EQuotaExceeded, EBudgetExceeded, EUnauthorized, EInvalidStatus).
- `complete_action()` — Marks intent as completed, emits ActionCompleted event.
- `emergency_revoke()` — Sets is_revoked=true, maxes out used_today to block further actions.
- `reset_quota()` — Resets daily counter.
- **Quality:** Clean, well-structured. Proper use of Sui patterns (owned caps, shared intents, events). But no access control on `reset_quota` or `emergency_revoke` — anyone could call these on a mutable reference. In a real deployment this would be a security issue, though the Capability is owned so only the owner can pass `&mut`.

**proof.move (66 lines):**
- `ProofRecord` — Shared object storing intent_id, walrus_blob_id, result_hash, timestamp, proof_type.
- `store_proof()` — Creates shared ProofRecord, emits ProofStored event.
- `verify_proof()` — Checks intent_id and result_hash match.
- **Quality:** Simple but functional. Walrus reference is a string (blob ID), not actual on-chain storage — makes sense for Walrus integration.

### Python Bot (811 lines total)

**core.py (216 lines):**
- Full autonomous loop: detect changes → LLM prediction → on-chain validation → local simulation → proof logging.
- `DetectedChange` dataclass for change tracking.
- `Vigilant` class orchestrates all components.
- Has `--init` flag for setup. Clean architecture.
- Demo payment feature (disabled by default).

**sui_client.py (139 lines):**
- Wraps Sui CLI (`subprocess.run`) for all on-chain calls.
- `validate_action()`, `complete_action()`, `store_proof()`, `create_capability()`.
- Parses JSON output. Error handling present.
- Note: Uses `list(action_hash)` which would produce Python list repr — may not work as Sui CLI args. But the deployed version works based on on-chain evidence.

**llm.py (96 lines):**
- Connects to local Ollama for intent prediction.
- Fallback pattern matching if LLM unavailable.
- Clean JSON parsing from LLM response.

**proofs.py (93 lines):**
- Uploads to Walrus aggregator (`walrus-testnet.sui.io/v1/blobs`).
- Falls back to minimal proof if upload fails.
- Stores reference on Sui via `store_proof`.

**simulations.py (179 lines):**
- Two simulation types: 3D print preview, git sync analysis.
- Uses PrusaSlicer if available, otherwise placeholder.
- SHA256 hashing of results for proof chain.

**watcher.py (88 lines):**
- File system monitoring with state persistence.
- Both polling and watchdog event-based modes.

### What's Good
- **End-to-end pipeline works:** File detection → LLM → on-chain validation → execution → proof. Full cycle verified on-chain.
- **Real Sui integration:** Capability pattern, shared objects, events, proper Move patterns.
- **Walrus integration:** Proof upload to decentralized storage with on-chain reference.
- **Local-first architecture:** Ollama for LLM, file watcher, no cloud dependency except Sui/Walrus.
- **Clean code:** Well-organized, good separation of concerns, readable.

### What's Weak
- **No frontend/UI:** Purely CLI/bot. No web interface.
- **No tests:** Zero test files for Move or Python.
- **Limited scope:** Only handles 2 simulation types (3D print, git sync). "Agent Action Firewall" name overpromises.
- **On-chain activity is light:** Only 3 transactions total. Looks like a single demo run.
- **Walrus blob is fake:** `walrus://abc123xyz` — not a real Walrus blob ID. The upload code exists but wasn't used with real data.
- **Some code won't work as-is:** `sui_client.py` passes `list(action_hash)` (Python list) as CLI arg — would need serialization fix. The demo script likely used different invocation.
- **No access control on reset_quota/emergency_revoke:** Works because Capability is owned, but not explicitly guarded.

## Sui Integration Analysis
- **Move smart contracts** — Two modules: `security` (capability-based action validation with quotas/budgets/expiry/revocation) and `proof` (Walrus blob reference + on-chain audit trail). Proper use of owned objects (Capability), shared objects (ActionIntent, ProofRecord), and events.
- **Sui CLI** — All on-chain interactions via `sui client call`. Package deployed, 3 verified transactions.
- **Walrus** — Code for blob upload to testnet aggregator. ProofRecord stores Walrus blob ID. But demo used placeholder blob ID.
- **Object model usage** — Good: AdminCap-like pattern (Capability is owned, scopes what the bot can do). ActionIntent is shared (allows multi-step propose→complete flow). ProofRecord is shared (auditable by anyone).
- **No dapp-kit, no frontend, no PTBs, no DeFi integrations.**

## Evaluation Scores
| Criteria | Score (1-10) | Notes |
|----------|:------------:|-------|
| Technical Merit | 5 | ~1K lines of real code with clean architecture. Full pipeline works end-to-end. But no tests, limited simulation types, some code issues (CLI arg serialization), and only 3 on-chain txns. Lightweight for a hackathon project. |
| Creativity | 6 | Combining file watching + local LLM prediction + on-chain capability validation + Walrus proof logging is a compelling vision. The "smart credit card for AI" framing is good. But the actual demo is narrow (3D print preview). |
| Problem-Solution Fit | 6 | The problem (autonomous agents need guardrails) is real and timely. On-chain capability enforcement is the right approach. But the solution only covers file monitoring + 2 action types — far from a general agent security system. The name "Vigilant" promises more than it delivers. |
| Sui Integration | 5 | Move contracts use proper patterns (caps, shared objects, events). Walrus integration exists in code. But only 3 testnet transactions, placeholder Walrus blob, no frontend/dapp-kit, and the CLI wrapper has issues. Integration is real but thin. |

## Overall Assessment
**Decent concept, thin execution.** Vigilant presents a compelling vision: autonomous agents constrained by on-chain capability tokens with Walrus-backed audit trails. The architecture is clean and the Move contracts use proper Sui patterns. But the implementation is lightweight (~1K lines), the demo is narrow (file watcher + print preview), on-chain activity is minimal (3 txns with a fake Walrus blob), and there's no UI or tests. Several other Track 1 projects tackle the same capability-based agent security problem with more depth.

**Shortlist recommendation: NO — mid-tier Track 1 project. Solid concept but insufficient depth to compete for prizes.**
