# Audit Template

## Process (per project)

### Step 0: Understand the Project
- **What is this project trying to do?** (one sentence)
- **What problem does it solve?** (who has this problem? how painful is it?)
- **Does the solution actually address that problem?** (or is it a solution looking for a problem?)
- **Would someone actually use this?** (practical utility check)

### Step 1: Repo Scan
- Check repo structure, file count, languages
- Estimate lines of code
- Look for Move contracts, Sui SDK usage, Walrus/Seal integration
- Note: is this real code or boilerplate/template?

### Step 1b: Move Contract Compilation (if Move contracts exist)
- Run `sui move build` in the contract directory
- Does it compile cleanly? Any errors or warnings?
- If it fails, note the errors — this is a minus but not disqualifying if a deployed version exists on-chain with real transactions (code worked at some point)
- Check `Move.toml` for correct dependencies and edition

### Step 2: Demo Video Analysis
If a demo video exists (YouTube, Loom, etc.):
- **Watch the full video** (2x speed is fine) and note timestamps of key moments
- **Content analysis:**
  - What does the video actually show? (live app, terminal, slides, talking head, etc.)
  - Does it demonstrate the core claimed functionality end-to-end?
  - Are there real on-chain transactions visible (tx hashes, Suiscan/Suivision links)?
  - Is it a screencast of real usage or just a slideshow/UI mockup?
  - Does the demo match what the code actually does? (flag mismatches)
- **Quality signals:**
  - Video length and production effort
  - Does the presenter explain the architecture or just click through?
  - Are there visible errors, placeholder data, or simulated outputs?
  - Is it clear the person understands the project or just reading a script?
- **Note specific operations demonstrated** (e.g., "mints NFT at 1:23", "wallet connects at 0:45")
- If video link is placeholder (just youtube.com) or broken, flag as ❌ No demo video

### Step 3: Live Site / On-Chain Verification
- Test website if available (flag Zee if wallet connection needed)
- Verify package ID on Sui Explorer — does the contract exist? Any transactions?
- Check npm packages if claimed

### Step 4: Sui Stack Usage Assessment
Look for genuine usage of:
- `@mysten/sui` SDK (SuiClient, transaction building)
- `@mysten/dapp-kit` (wallet connection, hooks)
- Move smart contracts (custom modules, not just hello-world)
- Walrus (decentralized storage — blob uploads, reads)
- Seal (encryption, threshold decryption)
- Sui CLI / PTBs (programmable transaction blocks)
- DeFi protocols on Sui (NAVI, Cetus, Turbos, etc.)
- Gas Station / sponsored transactions

**Critical question:** Is Sui actually used in the demo, or just mentioned in the description?

### Step 5: Score & Write Audit

## Scoring Rubric

### Technical Merit (1-10)
- 1-3: Minimal code, mostly boilerplate/scaffolding, doesn't compile or run
- 4-5: Basic working code but shallow implementation, limited functionality
- 6-7: Solid implementation, good architecture, multiple features working
- 8-9: Production-quality code, comprehensive features, tests, infra
- 10: Exceptional engineering — novel architecture, deep integrations, polished

### Creativity (1-10)
- 1-3: Direct clone of existing project or generic template
- 4-5: Minor twist on a common idea
- 6-7: Interesting approach, solves a real problem in a novel way
- 8-9: Highly original concept, compelling framing, clear vision
- 10: Category-defining — creates a new paradigm or combines ideas nobody else did

### Problem-Solution Fit (1-10)
- 1-3: No clear problem identified, or solution doesn't address the stated problem
- 4-5: Problem exists but solution is superficial or already well-solved elsewhere
- 6-7: Real problem with a reasonable solution, but gaps in how well they connect
- 8-9: Clear, well-articulated problem with a solution that directly and effectively addresses it
- 10: Nail-on-the-head — identifies a critical underserved problem and the solution is the obvious right answer

### Sui Integration (1-10)
- 1-3: Sui mentioned but barely used (just SDK import, no real on-chain activity)
- 4-5: Basic Sui usage (simple contract or SDK calls, single component)
- 6-7: Meaningful integration of 2-3 Sui stack components with real on-chain activity
- 8-9: Deep integration across multiple Sui components, real transactions, thoughtful use of Sui's unique features (object model, PTBs, etc.)
- 10: Pushes the boundaries of what's possible on Sui — novel protocol usage, deep Move contracts, multiple ecosystem integrations

## Red Flags
- Placeholder YouTube links (just youtube.com with no video)
- GitHub link points to non-repo (X profile, generic user page)
- Website is just localhost or 127.0.0.1
- Description claims features that aren't in the code
- Package ID doesn't exist on the claimed network
- Repo is mostly README with minimal actual code
- Deployed on non-Sui chain (Base, Ethereum, etc.)
- Duplicate submission (same project, both tracks)
