"""Privacy-Preserving Authentication Score (PPAS).

Definition 3 of the paper:

    PPAS(e) = alpha * (1 - min(V_lat, V_max) / V_max)
            + beta  * (1 - CorRisk)
            + gamma * ZK_comp

with (alpha, beta, gamma) = (0.40, 0.35, 0.25) and V_max = 120 ms.
Range [0, 1]; higher is better.
"""

import numpy as np

ALPHA = 0.40   # latency weight
BETA = 0.35    # correlation-resistance weight
GAMMA = 0.25   # ZK-completeness weight
V_MAX_MS = 120.0


def compute_ppas(verify_ms, corr_risk, zk_comp, v_max=V_MAX_MS):
    """Compute PPAS for a single authentication event. O(1)."""
    latency_score = 1.0 - min(verify_ms, v_max) / v_max
    corr_score = 1.0 - corr_risk
    ppas = ALPHA * latency_score + BETA * corr_score + GAMMA * zk_comp
    return float(np.clip(ppas, 0.0, 1.0))
