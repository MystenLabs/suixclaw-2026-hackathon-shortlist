# sui-secure-ai-shield — Audit

## Project Info
| Field | Value |
|-------|-------|
| **DeepSurge ID** | `28264b1e-6df8-4f79-8646-ce11a12bda5a` |
| **Name** | sui-secure-ai-shield (SecureAI Shield) |
| **Track** | Safety & Security |
| **GitHub** | https://github.com/VipMason/sui-secure-ai-shield |
| **Website** | https://dbtgugu.online |
| **Demo Video** | https://youtu.be/614i3BlhlCQ (3:51, no CC) |
| **Package ID** | `0x3a22bb587ac926723a67cf6d134ab4795887639c49a61cf1aafae1a388d1a197` |
| **Network** | Testnet |
| **Listed** | True |
| **Submitted** | 2026-03-03T09:24:05.780Z |

## Description
SecureAI Shield: A decentralized, 7-layer security immune system for AI Agents. Built on OpenClaw and powered by Sui Network to protect against prompt injections, unauthorized wallet drains, and system tampering with on-chain audit attestation. Agent model: MiniMax-M2.5.

## Eligibility Checklist
- [x] Submitted to DeepSurge
- [x] Developed by AI agents (MiniMax-M2.5 stated)
- [x] Uses at least one Sui Stack component — Move contract, Walrus (simulated), Seal (simulated)
- [ ] Working demo verifiable by humans — Video is a code/doc walkthrough, no live execution
- [x] Complete DeepSurge profile with wallet address (shown in video: `0xe4f90573...`)

## Evaluation Scores
| Criteria | Score (1-10) | Notes |
|----------|:------------:|-------|
| Technical Merit | 5 | Four OpenClaw skills (injection-hunter, self-hardening, wallet-airgap, core) with ~2,947 LOC. Modular skill-based design. Injection Hunter has regex-based pattern detection for prompt injection, jailbreak, credential harvesting, and Sui CLI command abuse. Self-hardening script handles firewall/UFW, git version control, secrets encryption, command blacklist, audit logging, Docker security. Wallet Air-Gap concept for hardware wallet middleware. However: only 4 commits, Walrus and Seal integrations are **fully simulated** (generate local hashes, don't actually upload to Walrus or call Seal), Move contract is minimal. |
| Creativity | 6 | The "7-layer security immune system" concept is well-framed and the layering model (Input Detection → Permission Manager → Runtime Sandbox → Network Firewall → Behavior Monitor → Auto-Responder → Audit Logger) is thoughtful. Multi-skill architecture maps well to OpenClaw's skill system. The permission levels (L0-L4) with cooldowns and confirmation requirements show real security thinking. However, the concept is similar to several other security-focused submissions. |
| Problem-Solution Fit | 5 | The problem (securing AI agents against injection, unauthorized access, wallet drains) is the core problem of Track 1. The 7-layer approach is comprehensive on paper. However: (1) Most layers are conceptual rather than implemented — the "Runtime Sandbox", "Network Firewall", and "Behavior Monitor" are described but not coded. (2) Walrus and Seal integrations are simulated (local hash generation, not actual uploads). (3) The injection hunter uses basic regex patterns rather than ML-based detection. (4) No live demo of the system actually blocking an attack. |
| Sui Integration | 3 | **Move contract** (`secure_audit.move`, ~100 lines): Deployed on testnet. Creates SecurityEvent objects with event_type, risk_score, description, blocked flag. AuditStore tracks event count. Specialized log functions for injections, unauthorized access, and wallet transfers. However: (1) **Walrus integration is fully simulated** — `WalrusStore` class generates local SHA-256 hashes and stores in memory/files, never actually calls the Walrus publisher API. Comments say "实际需要通过SDK上传" (needs SDK upload in actual deployment). (2) **Seal integration is fully simulated** — `SealEncryption` class uses Node.js `crypto` module for AES-256-GCM, not Sui's Seal SDK. Comments say "实际部署时需要调用 Sui 合约" (needs Sui contract call in actual deployment). (3) No @mysten/sui SDK imported. (4) No on-chain events verified. |

**Total: 19/40**

## Demo Verification
- **Video** (3:51, no CC, 4 views):
  - **0:00-0:15** — GitHub repo overview showing file structure
  - **0:15-1:00** — Self-Hardening SKILL.md walkthrough: features list (Firewall, Git Version Control, Secrets Encryption, Command Blacklist, Audit Logging, CLI Hardening, Docker Security), usage commands
  - **1:00-1:40** — Browsing through skills directories (injection-hunter, wallet-airgap, core)
  - **1:40-2:20** — README showing 7 Security Layers table
  - **2:20-3:00** — Architecture diagram, project structure
  - **3:00-3:51** — Sui Smart Contract section: `secure_audit` package ID, DeepSurge Hackathon info, wallet address
  - **Assessment:** The video is entirely a GitHub repo walkthrough — scrolling through code files and documentation. **No live demonstration** of the security system detecting an attack, blocking a prompt injection, or logging an event on-chain. This is documentation review, not a product demo.

## Code Review Notes
- **injection-hunter** (`scripts/filter.js`): Regex-based prompt injection detection. Checks for system prompt overrides, role-play attacks, credential harvesting, instruction ignoring, base64/encoding abuse, Sui CLI dangerous commands (`sui keytool export`, `sui client transfer`, etc.). Returns risk score, blocked status, and detection details. `scripts/walrus-store.js` stores detection reports to simulated Walrus.
- **self-hardening** (`scripts/harden.sh`): Shell script for system hardening — UFW firewall, fail2ban, SSH config, audit logging, Docker security, git auto-commit. Practical but not Sui-specific.
- **wallet-airgap** (`wallet-airgap.js`): Middleware concept for hardware wallet approval of transactions. Queues transactions for manual approval. No actual hardware wallet integration.
- **core** (`index.js`): Permission management system with L0-L4 levels, operation categorization, cooldowns, and multi-confirmation for high-risk ops. Integrates WalrusStore and SealEncryption.
- **Walrus** (`src/audit/walrus.js`): ⚠️ **Simulated.** `WalrusStore` class has config for testnet/mainnet URLs but never makes HTTP calls. Uses `crypto.createHash('sha256')` to generate "blob IDs" locally. `storeAuditLog()` stores to an in-memory Map. `readFromWalrus()` reads from the same Map.
- **Seal** (`src/audit/seal.js`): ⚠️ **Simulated.** `SealEncryption` class uses Node.js `crypto` (AES-256-GCM) for encryption. Has `SEAL_CONFIG` with `packageId: '0x2::seal::'` (incorrect — Seal is not at `0x2`). `createAccessPolicy()` returns a mock object. `verifyAccess()` always returns `access: 'granted'`.
- **Move contract** (`secure_audit.move`): Real but minimal. SecurityEvent struct, AuditStore counter, log functions. Deployed on testnet.
- **4 commits total** — 1 initial + 3 fixes for GitHub links.

## Sui Integration Analysis
- **Move contract:** ✅ Deployed on testnet. Real but minimal — event creation and counting.
- **Walrus:** ❌ **Simulated only.** Never calls Walrus API. Local hash generation pretending to be blob IDs.
- **Seal:** ❌ **Simulated only.** Standard Node.js crypto, not Sui Seal SDK. Incorrect package ID reference.
- **@mysten/sui:** ❌ Not imported or used anywhere.
- **On-chain activity:** ❌ Not verified (no events queried).

## Overall Assessment
SecureAI Shield has a well-thought-out conceptual framework (7-layer security model) and decent OpenClaw skill organization. The injection-hunter with regex-based detection for Sui CLI commands is practical. The permission system with cooldowns is a reasonable approach.

However, the project significantly overpromises and underdelivers on Sui integration:
1. **Walrus is completely simulated** — generates local hashes, never uploads to Walrus
2. **Seal is completely simulated** — uses Node.js crypto, not Sui's Seal
3. **Demo is a code walkthrough** — no live demonstration of security in action
4. **Only 4 commits** — appears quickly assembled
5. **Move contract is minimal** — basic event logging

The gap between the impressive README/architecture claims and the actual implementation is significant.

**Shortlist recommendation: No**
