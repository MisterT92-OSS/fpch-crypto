# FPCH — Function of Chaotic Hyperbolic Permutation

**A cryptographic hash function based on real quadratic fields**

**Author:** Toufik Salem (Independent Researcher)  
**Paper:** [`arxiv/fpch_arxiv.tex`](arxiv/fpch_arxiv.pdf) (arXiv-ready, 12 pages)  
**Status:** Invitation to Cryptanalysis — Experimental  
**Version:** V6 (cross-lane diffusion, division-free)

---

## Overview

FPCH explores whether the irrationality of quadratic surds can provide a foundation for chaos-based hashing when implemented with exact integer arithmetic.

While chaos-based hash functions and quadratic-field cryptography have been studied separately, their combination in an integer-only construction appears unexplored. FPCH proposes this novel combination.

---

## Research Status

This is an **invitation to cryptanalysis**. We make no claims of provable security. We explicitly invite:
- Algebraic attacks (Gröbner basis)
- Differential cryptanalysis
- Lane-wise attacks
- Weak key analysis
- Preimage attacks

See [`docs/SECURITY_ANALYSIS.md`](docs/SECURITY_ANALYSIS.md) for the full threat model and known weaknesses.

---

## Quick Start

```bash
git clone https://github.com/MisterT92-OSS/fpch-crypto.git
cd fpch-crypto
python3 fpch_v6.py        # Demo + cross-lane verification
python3 tests/test_fpch_v6.py   # Reproducible test suite
```

---

## Versions

| File | Avalanche | Description |
|---|---|---|
| `fpch_v6.py` | **49.98%** | Cross-lane diffusion, division-free (**recommended**) |
| `fpch_v5.py` | 4.7% | 100% paper-compliant (academic reference) |
| `fpch_v4.py` | 55.5% | Intermediate version |
| `fpch_working.py` | 42% | Simplified working version |
| `fpch_main.py` | 54.7% | Legacy (not paper-compliant) |

---

## Core Formula (V5)

```
P(x) = floor( (⌊√D⌋₁₂₈ · x² >> 64 + α·x + β) / (x + γ) ) mod 2⁶⁴
```

## V6 Improvements

- **Cross-lane mixing** after each round (`x[i] ^= ROTL(x[i+1],13) ^ ROTL(x[i+3],29)`)
- **Division-free permutation** (multiplication by odd rotated value + XOR)
- **MurmurHash-style non-linearity** (`0xff51afd7ed558ccd` mix)
- **Golden ratio constant** (`0x9e3779b97f4a7c15`)
- **Final global mixing** to eliminate lane independence

---

## Test Results (V6)

| Test | Result | Detail |
|---|---|---|
| NIST Frequency (Monobit) | PASS | p = 0.4133 |
| NIST Runs | PASS | p = 0.6403 |
| NIST Serial (m=4) | PASS | p = 0.0156 |
| Strict Avalanche Criterion | PASS | 49.98% bit change |
| Complete Diffusion | PASS | 50.00% bit change |
| Cross-Lane Mixing | PASS | 8/8 lanes affected |
| Weak Inputs | PASS | All distinct outputs |
| Collision (32-bit trunc.) | PASS | 1 collision / 50K (theoretical 25.3%) |

Run the suite yourself:
```bash
python3 tests/test_fpch_v6.py
```
Results are saved to `tests/fpch_v6_test_results.json`.

---

## Paper

`arxiv/fpch_arxiv.pdf` (12 pages) includes:
- Definitions of real quadratic fields and continued fractions
- FPCH V5 and V6 specifications
- Theorems on parameter sensitivity and algebraic resistance
- Reproducible experimental results
- 5 explicit open problems
- Full responsible disclosure policy

---

## Documentation

| Document | Purpose |
|---|---|
| [`docs/SECURITY_ANALYSIS.md`](docs/SECURITY_ANALYSIS.md) | Threat model, known weaknesses, invited attacks |
| [`docs/ARXIV_PREP.md`](docs/ARXIV_PREP.md) | How to submit the paper to arXiv |
| [`docs/BENCHMARKS.md`](docs/BENCHMARKS.md) | Reproducible benchmarks and performance notes |

---

## Contributing

We welcome cryptanalytic contributions. If you break FPCH, please open an issue or email **toufik.salem.perso@pm.me**.

For responsible disclosure of security findings, see [`docs/SECURITY_ANALYSIS.md`](docs/SECURITY_ANALYSIS.md).

---

## License

MIT License — See LICENSE file.

---

## Contact

**Toufik Salem** — toufik.salem.perso@pm.me

*May 2026*
