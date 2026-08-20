"""Registry Agent (RA): sparse Merkle tree revocation accumulator."""

import hashlib

import numpy as np


class RegistryAgent:
    """Maintains a sparse Merkle tree (height 256) over revoked
    credential identifiers; anchors the root on-chain each epoch.

    The simulation models the RA by its SMT proof latency and by the
    residual correlation risk of ZKAuth transcripts (CorRisk), the
    theoretical design parameter discussed in Section VI-A."""

    SMT_PROOF_MS = (12.4, 1.8)   # non-membership proof latency (ms)
    CORR_RISK = (0.008, 0.003)   # residual correlation risk [0, 1]

    def __init__(self, rng: np.random.RandomState | None = None):
        self.rng = rng or np.random
        self.revoked: set[str] = set()

    def revoke(self, cred_id: str) -> None:
        self.revoked.add(hashlib.sha256(cred_id.encode()).hexdigest())

    def is_revoked(self, cred_id: str) -> bool:
        return hashlib.sha256(cred_id.encode()).hexdigest() in self.revoked

    def sample_corr_risk(self, n: int) -> np.ndarray:
        return np.clip(self.rng.normal(*self.CORR_RISK, n), 0.001, 0.99)
