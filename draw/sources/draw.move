module draw::draw {
    use sui::random::{Self, Random};
    use sui::event;

    /// Emitted when a draw is performed. Permanently recorded on-chain.
    public struct DrawResult has copy, drop {
        min: u64,
        max: u64,
        result: u64,
    }

    /// Generate a verifiable random number in [min, max].
    entry fun draw(r: &Random, min: u64, max: u64, ctx: &mut TxContext) {
        let mut generator = random::new_generator(r, ctx);
        let result = random::generate_u64_in_range(&mut generator, min, max);
        event::emit(DrawResult { min, max, result });
    }
}
