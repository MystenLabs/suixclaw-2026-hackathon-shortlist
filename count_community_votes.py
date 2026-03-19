#!/usr/bin/env python3
"""Parse and count Community Favourite votes from community-favourite.md"""

import re
from collections import Counter

with open("community-favourite.md") as f:
    lines = f.readlines()

# Skip the first line per instructions
lines = lines[1:]

votes_received = Counter()
ballots = []

for line in lines:
    line = line.strip()
    if not line:
        continue

    # Parse "I am: <ID> Votes: <comma-separated list>"
    match = re.match(r"I am:\s*(\S+)\s+Votes:\s*(.*)", line)
    if not match:
        print(f"WARNING: Could not parse line: {line}")
        continue

    voter = match.group(1)
    raw_votes = match.group(2)

    # Split on commas, handle typos like periods instead of commas (e.g. "S18.L19")
    raw_votes = raw_votes.replace(".", ",")
    voted_for = [v.strip() for v in raw_votes.split(",") if v.strip()]

    # Check for self-voting
    self_votes = [v for v in voted_for if v == voter]
    if self_votes:
        print(f"WARNING: {voter} voted for themselves!")

    ballots.append((voter, voted_for))

    for v in voted_for:
        votes_received[v] += 1

# Print all ballots
print("=" * 60)
print("BALLOTS")
print("=" * 60)
for voter, voted_for in ballots:
    print(f"  {voter:6s} -> {', '.join(voted_for)} ({len(voted_for)} votes cast)")

# Print results sorted by votes received
print()
print("=" * 60)
print("VOTES RECEIVED (sorted by count)")
print("=" * 60)

for project, count in votes_received.most_common():
    print(f"  {project:6s}: {count}")

print()
print(f"Total ballots: {len(ballots)}")
print(f"Total projects that received votes: {len(votes_received)}")

# Phase 2 winners (mapped from T1-#/T2-# to S#/L# numbering):
#   Track 1: T1-3 -> S24, T1-4 -> S15, T1-8 -> S5, T1-6 -> S22, T1-9 -> S6
#   Track 2: T2-1 -> L25, T2-2 -> L21, T2-6 -> L6, T2-11 -> L16, T2-5 -> L13
PHASE2_WINNERS = {
    # Track 1 winners
    "S24",  # Sui-Immunizer (T1-3)
    "S15",  # Lulu AI Firewall (T1-4)
    "S5",   # BioSeal (T1-8)
    "S22",  # Sentinel Protocol (T1-6)
    "S6",   # ClaWall (T1-9)
    # Track 2 winners
    "L25",  # Watchdog (T2-1)
    "L21",  # t2000 (T2-2)
    "L6",   # Infinite Money Glitch (T2-6)
    "L16",  # Sui Jarvis (T2-11)
    "L13",  # SealForge (T2-5)
}

# Project name mapping for readability
PROJECT_NAMES = {
    "S1": "AAF", "S2": "Agents", "S3": "AgentVault", "S4": "AirGap",
    "S5": "Bioseal", "S6": "Clawall", "S7": "clawguard", "S8": "ClawGuard",
    "S9": "ClawShield", "S10": "ClawShield Lite", "S11": "Guardian Vault",
    "S12": "Injection Hunter", "S13": "Injection Hunter (2)", "S14": "Klaave",
    "S15": "Lulu AI Firewall", "S16": "Miao Wallet", "S17": "OneKey Air-Gap Sui",
    "S18": "proof-of-restraint", "S19": "RAM", "S20": "SafeFlow",
    "S21": "SealClaw", "S22": "Sentinel Protocol", "S23": "Shield Claw",
    "S24": "Sui-Immunizer", "S25": "sui-safety-middleware-mvp",
    "S26": "sui-secure-ai-shield", "S27": "SuiSec", "S28": "SuiSentry",
    "S29": "Vigilant", "S30": "WalrusProof",
    "L1": "AgentForge", "L2": "AGENX", "L3": "AutoClean Agent",
    "L4": "DeepClean Butler", "L5": "Grokster", "L6": "Infinite Money Glitch",
    "L7": "ManaPool", "L8": "Moltbook Hivemind", "L9": "Nexus Learning Ledger",
    "L10": "Pantheon", "L11": "Pet", "L12": "PixelPal", "L13": "SealForge",
    "L14": "Stableflow Checkout", "L15": "StillClawing", "L16": "Sui Jarvis",
    "L17": "Sui Opportunities Hunter", "L18": "Sui-Butler",
    "L19": "sui-minority-game", "L20": "SuiPilot", "L21": "t2000",
    "L22": "TaskHawk", "L23": "TRIPLE HELIX VAULT", "L24": "WALVIS",
    "L25": "Watchdog",
}

# Remove Phase 2 winners from tally
filtered = Counter({k: v for k, v in votes_received.items() if k not in PHASE2_WINNERS})
excluded = {k: v for k, v in votes_received.items() if k in PHASE2_WINNERS}

print()
print("=" * 60)
print("PHASE 2 WINNERS EXCLUDED FROM TALLY")
print("=" * 60)
for project, count in sorted(excluded.items(), key=lambda x: -x[1]):
    name = PROJECT_NAMES.get(project, "?")
    print(f"  {project:6s} ({name}): {count} votes removed")

print()
print("=" * 60)
print("COMMUNITY FAVOURITE -- FINAL RESULTS (after exclusions)")
print("=" * 60)
for i, (project, count) in enumerate(filtered.most_common(), 1):
    name = PROJECT_NAMES.get(project, "?")
    winner = " <-- WINNER ($200)" if i <= 5 else ""
    print(f"  {i:2d}. {project:6s} ({name}): {count}{winner}")
