# ClawGuard — Audit

## Project Info
| Field | Value |
|-------|-------|
| **DeepSurge ID** | `df3c93ff-6cfd-4b97-b9c4-7f040a1a1fa2` |
| **Name** | ClawGuard |
| **Track** | Safety & Security |
| **GitHub** | N/A — no GitHub link provided |
| **Website** | N/A |
| **Demo Video** | N/A |
| **Package ID** | `0x2cefd7cf978a13c581a53df3479739cb6b8819b0c815212fb0489ee98f9a269e` |
| **Network** | Testnet (claimed) |
| **Listed** | True |
| **Submitted** | 2026-02-22T10:30:51.032Z |

## Description
Chinese-language submission: "在 OpenClaw 获得自由的同时，给它穿上不可绕过的 Move 安全外壳，让人类敢把钱包交给它。我们不阻止进化，我们只让进化可审计、可回滚、可信任。" (Translation: "While OpenClaw gains freedom, give it an unbypassable Move security shell so humans dare to hand over their wallets. We don't stop evolution — we just make evolution auditable, rollbackable, and trustworthy.")

## Eligibility Checklist
- [x] Submitted to DeepSurge
- [ ] Developed by AI agents (or mostly AI agents) — cannot verify
- [ ] Uses at least one Sui Stack component — package ID does not resolve on-chain
- [ ] Working demo verifiable by humans — no demo, no code, no video
- [ ] Complete DeepSurge profile with wallet address

## Evaluation Scores
| Criteria | Score (1-10) | Notes |
|----------|:------------:|-------|
| Technical Merit | 1 | No code available. No GitHub repo linked. No demo video. Only a single architecture diagram (PNG) showing a four-layer design. Nothing to evaluate technically. |
| Creativity | 5 | The four-layer architecture concept is interesting: SkillRegistry (risk scoring + blacklist) → ExecutionSandbox (burn-after-use contexts) → SupplyChainGuard (dependency graph risk propagation) → AgentCapability (dynamic tokens + soft isolation). Shows architectural thinking, but it's just a diagram. |
| Problem-Solution Fit | 3 | The described problem (making AI agent actions auditable and controllable) is real. But there's no implementation to evaluate whether the solution actually works. |
| Sui Integration | 1 | Package ID `0x2cefd7...` does not exist on testnet — `sui_getObject` returns null, `getNormalizedMoveModulesByPackage` returns empty. No Move code, no SDK usage, no Walrus, no on-chain activity. Zero verifiable Sui integration. |

## Demo Verification
- **Demo video:** None provided.
- **Live site:** None provided.
- **GitHub:** No repository link in submission.
- **On-chain verification:** Package `0x2cefd7cf978a13c581a53df3479739cb6b8819b0c815212fb0489ee98f9a269e` does NOT exist on testnet. Both `sui_getObject` and `sui_getNormalizedMoveModulesByPackage` return null/empty.
- **Media:** Single PNG image — architecture diagram showing four-layer security shell (SkillRegistry, ExecutionSandbox, SupplyChainGuard, AgentCapability). Diagram only, no code or demo.

## Code Review Notes
- No code to review. No GitHub repository. No source files.

## Sui Integration Analysis
- **Move contract:** Package ID doesn't resolve — never deployed or wrong ID. ✗
- **SDK/dapp-kit:** Cannot verify — no code. ✗
- **Walrus/Seal:** None. ✗
- **On-chain activity:** Zero. ✗

## Overall Assessment
**Concept-only submission.** ClawGuard presents an interesting four-layer security architecture in a single diagram, but there is no code, no repository, no demo, and the claimed package ID doesn't exist on testnet. This is essentially a design document with no implementation.

**Shortlist recommendation: No — disqualified. No code, no demo, no working on-chain deployment.**
