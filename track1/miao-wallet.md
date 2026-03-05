# Miao Wallet — Audit

## Project Info
| Field | Value |
|-------|-------|
| **DeepSurge ID** | `29abb9e2-ea63-4a05-961e-ed7f686230c9` |
| **Name** | Miao Wallet |
| **Track** | Safety & Security |
| **GitHub** | `https://github.com/CryptoMiaobug/MiaoWallet` |
| **Website** | `https://cryptomiao.wal.app/` (Walrus Sites!) |
| **Demo Video** | `https://youtu.be/ULemqtnVZiE` |
| **Package ID** | N/A |
| **Network** | Mainnet |
| **Listed** | True |
| **Submitted** | 2026-03-02T18:18:58.948Z |

## Description
MiaoWallet is a security middleware for AI agents on Sui. Separates key custody (macOS Keychain) from transaction logic. Two modes: API (MCP tools for programmatic control) and Browser (Chrome extension for DApp interactions). Session-based signing with time + count limits. Walrus attestation for audit trails.

## Eligibility Checklist
- [x] Submitted to DeepSurge
- [x] Developed by AI agents (or mostly AI agents) — includes OpenClaw SKILL.md
- [x] Uses at least one Sui Stack component — Sui SDK (mainnet), Walrus Sites hosting
- [x] Working demo verifiable by humans — YouTube demo, live Walrus site, screenshots
- [x] Complete DeepSurge profile with wallet address

## Evaluation Scores
| Criteria | Score (1-10) | Notes |
|----------|:------------:|-------|
| Technical Merit | 8 | ~11,000 LOC across Python + JS. Full-featured wallet: `wallet_mcp_server.py` (584 LOC MCP server with 10+ tools), `wallet_panel.py` (779 LOC desktop GUI with tkinter), `mnemonic_manager_bip44.py` (447 LOC BIP44 key derivation for SUI/Solana/ETH), Chrome extension (background.js + content.js + inject.js for DApp signing), `ws_bridge.py` (WebSocket bridge between extension and local wallet), `sui_transfer.py`, `solana_transfer.py`, `evm_transfer.py`, `sui_bridge.py`, `sui_name_service.js`, `cetus_swap.js` + `cetus-swap/swap.mjs` (Cetus DEX integration), `build_tx.mjs`, `sui_dry_run.js`. Includes `.bak` version showing iterative development. SKILL.md for OpenClaw integration. |
| Creativity | 8 | The key insight — separating key custody from transaction logic for AI agents — is both practical and important. The dual-mode approach (MCP for programmatic + Chrome extension for DApps) covers both agent interaction patterns elegantly. Session-based signing with count + time limits is a smart security/usability balance. Multi-chain support (SUI, Solana, ETH) with BIP44 derivation adds real utility. macOS Keychain for key storage is a production-grade choice. Deployed on Walrus Sites! |
| Problem-Solution Fit | 8 | Addresses one of the most critical problems in agent security: how agents transact without exposing private keys. The MCP server design means any OpenClaw agent can use it as a tool. The whitelist system (origin + contract address) provides defense-in-depth. The Chrome extension bridges the gap for DApp interactions. Practical, immediately useful solution. |
| Sui Integration | 7 | Sui SDK used throughout (`@mysten/sui` in JS, `sui_transfer.py`, `sui_dry_run.js`). SUI Name Service integration (`sui_name_service.js`). Cetus DEX swap integration. Sui bridge support. Real mainnet wallet with balance shown (0.942 SUI + 11.625 WAL). **Hosted on Walrus Sites** (`cryptomiao.wal.app`) — one of the few submissions using Walrus Sites. No Move contract (appropriate for wallet middleware). YouTube demo exists. |

## Demo Verification
- **GitHub:** Public repo with 9419 files (mostly node_modules), real source in `MiaoWallet-SecureWallet-4Openclaw/`.
- **Demo video:** YouTube at `https://youtu.be/ULemqtnVZiE`.
- **Website:** Live on Walrus Sites at `cryptomiao.wal.app` — proves Walrus ecosystem usage.
- **Screenshots:** Polished desktop app showing multi-chain wallet tree, dual signing modes (API authorized + Browser connected), session counters (0/10, 29:31 remaining), whitelist configuration panel.
- **Iterative development:** `.bak-20260220` backup directory shows real development history.

## Code Review Notes
- **MCP Server (584 LOC Python):** 10+ tools including `get_address`, balance checks, transfers. Communicates with local bridge at `localhost:3847`. Uses `httpx` for HTTP, `mcp.server.fastmcp` for MCP protocol. Clean error handling with Chinese+English messages.
- **Desktop GUI (779 LOC Python):** tkinter-based wallet panel with hierarchical wallet tree, session management, balance display.
- **Key Management (447 LOC Python):** BIP44 derivation for SUI (ed25519), Solana (ed25519), ETH (secp256k1). macOS Keychain integration for encrypted storage.
- **Chrome Extension:** Background service worker communicates with local bridge via HTTP. Content script + injector pattern for DApp signing interception. Origin whitelisting enforced.
- **DApp Integrations:** Cetus DEX swap, SUI Name Service, SUI Bridge, dry-run simulation — real ecosystem tool usage.
- **OpenClaw SKILL.md:** Proper skill definition for OpenClaw integration.

## Sui Integration Analysis
- **Sui SDK:** Used in transfers, dry-run, name service, bridge ✓✓
- **Walrus Sites:** Live deployment at `cryptomiao.wal.app` ✓✓
- **DApp ecosystem:** Cetus DEX, SUI Name Service, SUI Bridge integrations ✓✓
- **MCP/Agent integration:** MCP server with full wallet tool suite ✓✓
- **Move contract:** None (appropriate for wallet middleware) —
- **On-chain activity:** Mainnet wallet with real balance, but no verifiable transaction history ✓

## Overall Assessment
**Impressive full-stack wallet middleware with real ecosystem integration.** MiaoWallet is one of the most complete submissions — a functional desktop wallet with MCP server for AI agents, Chrome extension for DApps, multi-chain support, session-based rate limiting, and defense-in-depth whitelisting. The code is substantial (~11K LOC), well-organized, and shows real Sui ecosystem integration (Cetus, SUI Name Service, Bridge, Walrus Sites hosting). The dual-mode design (API + Browser) is exactly what agent builders need. This solves a real, important problem.

**Shortlist recommendation: YES — comprehensive wallet middleware with deep ecosystem integration, MCP agent support, and production-grade security design.**
