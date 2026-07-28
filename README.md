# ZKAuth: A Zero-Knowledge Proof Framework for Privacy-Preserving Authentication in Decentralized Identity Systems

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![IEEE TIFS](https://img.shields.io/badge/Target-IEEE%20TIFS-blue)](https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=10206)
[![Simulation](https://img.shields.io/badge/Evaluation-Simulation%20Based-green)](data/results/)
[![GitHub](https://img.shields.io/badge/GitHub-ufxa%2Fzkauth-black?logo=github)](https://github.com/ufxa/zkauth)

> **Authors:** Allan Douglas Costa (UFRA/LICA/CCAD-IA)
> **Target Journal:** IEEE Transactions on Information Forensics and Security (IF 6.8)
> **Submission Status:** Preparation

---

## Abstract

ZKAuth is a three-agent framework integrating Groth16 zk-SNARKs with W3C DID infrastructure
to deliver provably privacy-preserving authentication without trusted third parties.
Evaluated against 10,000 synthetic decentralized identities across ten experimental rounds,
ZKAuth achieves a **Privacy-Preserving Authentication Score (PPAS) of 0.9924 ± 0.0001**,
surpassing ZK-STARK (0.8433), Bulletproofs (0.5875), and baseline Groth16 (0.9807),
with all improvements statistically significant (p < 0.001, paired t-test).

---

## Repository Structure

```
zkauth/
├── README.md
├── paper/
│   ├── main.tex               # Main LaTeX file (IEEEtran format)
│   ├── references.bib         # 53 bibliography entries with DOIs
│   └── figures/               # TikZ figures (embedded in main.tex)
├── src/                       # Source code for experiments
│   ├── agents/                # Prover, Verifier, Registry agent implementations
│   ├── metrics/               # PPAS metric implementation
│   └── evaluation/            # Evaluation scripts
├── data/
│   ├── processed/             # Processed synthetic DID dataset
│   └── results/               # Simulation outputs (CSV/JSON)
├── notebooks/                 # Jupyter notebooks for figure reproduction
├── scripts/
│   └── build.sh               # tectonic main.tex
├── .gitignore
└── LICENSE
```

---

## Novel Metric: Privacy-Preserving Authentication Score (PPAS)

```
PPAS(e) = 0.40 * (1 - min(V_lat, 120) / 120)
        + 0.35 * (1 - CorRisk)
        + 0.25 * ZK_comp
```

- `V_lat`: verification latency in milliseconds
- `CorRisk`: probability of identity correlation attack success ∈ [0,1]
- `ZK_comp`: zero-knowledge completeness score ∈ [0,1]
- Range: [0, 1] — higher is better

---

## Build

```bash
cd paper && tectonic main.tex
```

---

## Reproduce Simulation

```bash
pip install numpy scipy pandas
python3 src/evaluation/run_simulation.py
```

Results are written to `data/results/`.

---

## Key Results

| Scheme             | PPAS            | Verify Latency | Proof Size   | CorRisk |
|--------------------|-----------------|----------------|--------------|---------|
| **ZKAuth (Ours)**  | **0.9924±0.0001** | 1.21 ms       | 256 bytes    | 0.008   |
| ZK-SNARK (Groth16) | 0.9807±0.0001  | 0.82 ms        | 192 bytes    | 0.041   |
| ZK-STARK           | 0.8433±0.0003  | 44.72 ms       | ~87 KB       | 0.021   |
| Bulletproofs       | 0.5875±0.0003  | 118.16 ms      | ~2.5 KB      | 0.063   |

All paired t-tests: p < 10⁻⁶ (10 rounds, n=1,000 auth/scheme/round).

---

## Citation

```bibtex
@article{costa2026zkauth,
  author    = {Costa, Allan Douglas},
  title     = {ZKAuth: A Zero-Knowledge Proof Framework for Privacy-Preserving
               Authentication in Decentralized Identity Systems},
  journal   = {IEEE Transactions on Information Forensics and Security},
  year      = {2026},
  note      = {Under review}
}
```

---

## License

MIT License. See [LICENSE](LICENSE).
