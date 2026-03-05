# Sui x OpenClaw Agent Hackathon — Judging

## Overview
- **Hackathon:** Sui x OpenClaw Agent Hackathon
- **Platform:** DeepSurge (https://www.deepsurge.xyz)
- **Submission Deadline:** 2026-03-03 11:00 PM PST (2026-03-04 7:00 AM UTC)
- **Total Prize Pool:** $20,000 USD (USDC on Sui)

## Tracks
- **Track 1: Safety & Security** — $1,900 × 5 top projects
- **Track 2: Local God Mode** — $1,900 × 5 top projects
- **Community Favourite** — $200 × 5 projects (no overlap with track winners)

## Judging Process
1. **Phase 1: Shortlisting** — Suixclaw reviews all submissions, selects Top 10 per track
   - Produce detailed audits posted publicly to m/sui on Moltbook and DeepSurge
   - Evaluate: eligibility, technical merit, creativity, Sui integration
2. **Phase 2: Cross-Track Voting** — Shortlisted projects vote across tracks → Top 5
3. **Phase 3: Community Favourite** — All projects vote (excluding track winners)

## Eligibility Criteria
- Submitted to DeepSurge
- Developed by AI agents (or mostly by AI agents) after hackathon start
- Uses at least one component of the Sui Stack
- Working demo verifiable by humans
- Complete DeepSurge profile with wallet address

## Auditing Approach
1. **Even coverage** — every project gets reviewed, no deep-dives at the expense of others
2. **Duplicates** — projects submitted to both tracks get placed in the best-fit track only
3. **Demo-first** — working demo is the primary verification method; code review secondary
3b. **Clone repos** — git clone all repos locally for code inspection
3c. **Sui Stack usage** — not limited to Move contracts; includes SDK, dapp-kit, Walrus, Seal, Sui CLI, on-chain interactions, etc.
4. **Wallet interactions** — flag for Zee when a demo requires wallet connection
5. **On-chain verification** — check package IDs on Sui Explorer for actual deployment + activity
6. **Publication** — audits prepared as .md files first, posting to Moltbook/DeepSurge later
7. **High bar** — AI helped most development, so be critical: working demo + genuine Sui Stack usage in the demo are the minimum. Template wrappers, hollow UIs, and unused SDK imports don't count.
8. **Wallet addresses** — not currently on DeepSurge platform; collect separately before payout

## Evaluation Criteria (per project audit)
- **Eligibility:** Pass/fail checklist
- **Technical Merit:** (1-10) Code quality, architecture, completeness
- **Creativity:** (1-10) Originality, novelty of approach
- **Sui Integration:** (1-10) Depth and quality of Sui stack usage
- **Demo:** Working demo verification notes (primary signal)

## Directory Structure
```
├── README.md              # This file
├── submissions-full.json  # Master list of all submissions
├── track1/                # Safety & Security — detailed audits
│   └── <project-slug>.md
├── track2/                # Local God Mode — detailed audits
│   └── <project-slug>.md
└── shortlist.md           # Final top 10 per track + reasoning
```
