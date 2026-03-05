# DUPLICATES.md — Duplicate & Related Submission Analysis

Generated: 2026-03-04 16:40 GMT+8

## Confirmed Duplicates (same project, both tracks)

### 1. Vigilant — ⚠️ EXACT DUPLICATE
- **Same:** creator, GitHub repo, package ID, demo video — identical submission in both tracks
- **A:** Vigilant [Local God Mode] (`709b194a`) — listed ✅
- **B:** Vigilant [Safety & Security] (`b9f7a7f9`) — listed ✅
- GitHub: https://github.com/agentboogieai-max/Vigilant
- Package: `0x80350cfb8d75c2f78576c186af14f0ca3cc2890e2fb4ed22bce3a92a67cb8f84`
- Video: https://youtu.be/waXiRfky6KI
- **Verdict:** Cross-track duplicate. Both listed. Already audited under `b9f7a7f9` (track1/vigilant.md). Skeleton exists for `709b194a` (track2/vigilant-709b194a.md).

### 2. Guardian Vault — ⚠️ EXACT DUPLICATE
- **Same:** creator, project name, demo video, GitHub org
- **A:** Guardian Vault [Safety & Security] (`fa823b0c`) — listed ✅
  - GitHub: https://github.com/kiprotich-langat/guardian-vault
  - Skeleton audit exists (track1/guardian-vault-fa823b0c.md)
- **B:** Guardian Vault [Safety & Security] (`8859dd0b`) — listed ✅
  - GitHub: https://github.com/kiprotich-langat (profile, not repo)
  - Audited (track1/guardian-vault-8859dd0b.md)
- Video (both): https://youtu.be/CNoNs_p3UKY
- Package: None (both)
- **Verdict:** Same track duplicate. Same creator, same video. `8859dd0b` already has full audit.

## Same Name, Different Projects

### 3. Injection Hunter — DIFFERENT PROJECTS
- **A:** Injection Hunter [Safety & Security] (`728ce007`) — listed ✅
  - GitHub: https://github.com/bytesloop/injection_hunter
  - Package: `0x2fbbd7e553561aceed6001316e679b3a2dd9ad3d4e760cdbd9cc10bbd6f7fea8`
  - Video: ❌ (link points to GitHub)
- **B:** Injection Hunter [Safety & Security] (`9aaf1a99`) — listed ✅
  - GitHub: https://github.com/pipi333/hackathon-injection-hunter
  - Package: None
  - Video: https://youtu.be/RpPpsJwOLgI
- **Verdict:** Different creators, different repos, different code. Same name is coincidence. Both should be audited separately. `9aaf1a99` already audited (track1/injection-hunter.md).

### 4. ClawGuard — DIFFERENT PROJECTS
- **A:** clawguard [Safety & Security] (`b861f6d4`) — listed ✅
  - GitHub: https://github.com/jayjoshix/clawdefender
  - Package: `0x5379bf93b2b4733478e126f377d43b4cdc69ef6de7d7d163412fd3a0007c3fb2`
  - Audited (track1/clawguard-b861f6d4.md)
- **B:** ClawGuard [Safety & Security] (`df3c93ff`) — listed ✅
  - GitHub: https://github.com/goawtdg/SUI/tree/master
  - Package: `0x2cefd7cf978a13c581a53df3479739cb6b8819b0c815212fb0489ee98f9a269e`
  - Audited (track1/clawguard-df3c93ff.md)
- **Verdict:** Different creators, different repos, different packages. Both already audited separately.

## Same Creator, Different Projects (allowed)

### 5. TRIPLE HELIX VAULT + SealClaw — Same creator, both unlisted
- **Creator:** `991245b7`
- **A:** TRIPLE HELIX VAULT [Local God Mode] (`d4bf1de4`) — unlisted ❌
  - GitHub: https://github.com/Olympusxvn/triple_helix_demo (404)
- **B:** SealClaw [Safety & Security] (`92268d8a`) — unlisted ❌
  - GitHub: https://github.com/Olympusxvn/seal_claw (404)
- **Verdict:** Different projects, different tracks. Both unlisted, both repos 404. Legitimate multi-submission (different ideas).

### 6. AgentForge + Bioseal — Same creator
- **Creator:** `a9e3b4c9`
- **A:** AgentForge [Local God Mode] (`48d68d8d`) — unlisted ❌
  - GitHub: https://github.com/Hemal-047/AgentForge
- **B:** Bioseal [Safety & Security] (`a61a1414`) — listed ✅
  - GitHub: https://github.com/Hemal-047/Bioseal
- **Verdict:** Different projects, different tracks. Legitimate multi-submission.

### 7. Shield Claw + TaskHawk — Same creator
- **Creator:** `e7856440`
- **A:** Shield Claw [Safety & Security] (`c82a8620`) — listed ✅
  - GitHub: https://github.com/mememan-anon/ShieldClaw
- **B:** TaskHawk [Local God Mode] (`e3aafb3d`) — listed ✅
  - GitHub: https://github.com/mememan-anon/TaskHawk
- **Verdict:** Different projects, different tracks. Legitimate multi-submission.

## Summary

| Type | Count | Action |
|------|-------|--------|
| **Exact duplicates** | 2 (Vigilant, Guardian Vault) | Audit once, note duplicate in both files |
| **Same name, different projects** | 2 (Injection Hunter, ClawGuard) | Audit separately (already done) |
| **Same creator, different projects** | 3 (legitimate) | Audit separately |
| **Total unique projects** | **55** (57 - 2 duplicates) |
