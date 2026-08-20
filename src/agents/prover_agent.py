"""Prover Agent (PA): proof generation envelope."""

import hashlib
import secrets

import numpy as np


class ProverAgent:
    """User-side wallet component: witness generation + Groth16 proving.

    Performance envelope (mean, std) used by the simulation; values are
    calibrated against published Groth16 benchmarks plus the overhead of
    the 256 Poseidon constraints added for Merkle revocation checking.
    """

    GEN_MS = (1840.0, 95.0)      # proof generation latency (ms)
    PROOF_BYTES = (256, 0)       # proof + nullifier payload (bytes)

    def __init__(self, rng: np.random.RandomState | None = None):
        self.rng = rng or np.random

    def nullifier(self, sk_h: bytes, nonce: bytes) -> str:
        """eta = H(sk_H || nonce || r) with fresh per-event randomness r."""
        r = secrets.token_bytes(32)
        return hashlib.sha256(sk_h + nonce + r).hexdigest()

    def sample_generation_ms(self, n: int) -> np.ndarray:
        return np.clip(self.rng.normal(*self.GEN_MS, n), 10, None)
