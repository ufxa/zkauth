"""ZKAuth three-agent architecture (Section IV of the paper).

- ProverAgent (PA): witness generation and Groth16 proof construction
  over Poseidon-hashed credential attributes; emits nullifier
  eta = H(sk_H || nonce || r).
- VerifierAgent (VA): O(1) pairing-based proof verification, nullifier
  replay check, on-chain accumulator-root consistency check.
- RegistryAgent (RA): sparse Merkle tree accumulator for credential
  revocation; issues (non-)membership proofs and anchors the root
  on-chain each epoch.

The simulation models each agent by its measured performance envelope
(see src/evaluation/run_simulation.py and Table IV of the paper).
"""

from .prover_agent import ProverAgent
from .verifier_agent import VerifierAgent
from .registry_agent import RegistryAgent

__all__ = ["ProverAgent", "VerifierAgent", "RegistryAgent"]
