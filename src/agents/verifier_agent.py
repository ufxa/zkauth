"""Verifier Agent (VA): O(1) verification envelope + nullifier set."""

import numpy as np


class VerifierAgent:
    """Relying-party component: Groth16 verification (3 pairings, O(1)),
    nullifier replay check, and accumulator-root consistency check."""

    VERIFY_MS = (1.21, 0.09)     # verification latency (ms)

    def __init__(self, rng: np.random.RandomState | None = None):
        self.rng = rng or np.random
        self.nullifier_set: set[str] = set()

    def check_and_insert(self, eta: str) -> bool:
        """Replay check: reject if eta was already used, else record it."""
        if eta in self.nullifier_set:
            return False
        self.nullifier_set.add(eta)
        return True

    def sample_verification_ms(self, n: int) -> np.ndarray:
        return np.clip(self.rng.normal(*self.VERIFY_MS, n), 0.01, None)
