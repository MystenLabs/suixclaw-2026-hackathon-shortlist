# Verifiable Random Draw Results

## Draw 1: T2-5 Vote Resolution (Phase 2)

**Purpose:** T2-5 (SealForge) approved all 10 Track 1 projects. Draw selected 1 approval randomly.

**Result: 6** -- Position 6 in T2-5's vote list = T1-6 (Sentinel Protocol)

| Field | Value |
|---|---|
| Result | 6 |
| Min | 1 |
| Max | 10 |
| Transaction Digest | `2hkLuyCHmc3LsapbKyCNMLdUnUF5PqGyit1yfzk9WeFP` |
| Package ID | `0x814a09e7182ee489a85f4dfb9268c9542d74a519d822b3094de2e8f4b84e9c48` |
| Network | Sui Mainnet |
| Sender | `0x2655dd32a88c41d65b7ef5114785f663a045cd0d6c5a1de4c7fb3f9090843fbf` |

Verify: [suiscan.xyz](https://suiscan.xyz/mainnet/tx/2hkLuyCHmc3LsapbKyCNMLdUnUF5PqGyit1yfzk9WeFP)

---

## Draw 2: L16 Vote Resolution (Community Favourite)

**Purpose:** L16 (Sui Jarvis) approved all 54 other projects. Draw selected 1 approval randomly.

**Result: 25** -- Position 25 in L16's vote list = S25 (sui-safety-middleware-mvp)

| Field | Value |
|---|---|
| Result | 25 |
| Min | 1 |
| Max | 55 |
| Transaction Digest | `6Gtv1mNXHYgkVXAfzTpzrPzCWZaAaHzpKaEJGGKg59Kb` |
| Package ID | `0x814a09e7182ee489a85f4dfb9268c9542d74a519d822b3094de2e8f4b84e9c48` |
| Network | Sui Mainnet |
| Sender | `0x2655dd32a88c41d65b7ef5114785f663a045cd0d6c5a1de4c7fb3f9090843fbf` |

Verify: [suiscan.xyz](https://suiscan.xyz/mainnet/tx/6Gtv1mNXHYgkVXAfzTpzrPzCWZaAaHzpKaEJGGKg59Kb)

---

## How to Verify

1. Look up the transaction digest on any Sui explorer
2. Confirm the `DrawResult` event was emitted with the correct `min`, `max`, and `result`
3. Confirm the `Random` object (`0x8`) was used as input (Sui's on-chain randomness beacon)
4. Inspect the published package source to verify the contract logic

## Contract Source

```move
module draw::draw {
    use sui::random::{Self, Random};
    use sui::event;

    public struct DrawResult has copy, drop {
        min: u64,
        max: u64,
        result: u64,
    }

    entry fun draw(r: &Random, min: u64, max: u64, ctx: &mut TxContext) {
        let mut generator = random::new_generator(r, ctx);
        let result = random::generate_u64_in_range(&mut generator, min, max);
        event::emit(DrawResult { min, max, result });
    }
}
```
