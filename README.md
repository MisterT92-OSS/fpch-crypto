# FPCH — Function of Chaotic Hyperbolic Permutation

**A cryptographic hash function based on real quadratic fields**

**Author:** Toufik Salem (Independent Researcher)
**Paper:** FPCH_Paper.pdf (12 pages)
**Status:** Invitation to Cryptanalysis — Experimental

---

## Overview

FPCH explores whether the irrationality of quadratic surds can provide a foundation for chaos-based hashing when implemented with exact integer arithmetic.

While chaos-based hash functions and quadratic-field cryptography have been studied separately, their combination in an integer-only construction appears unexplored. FPCH proposes this novel combination.

---

## 🔬 Research Status

This is an **invitation to cryptanalysis**. We make no claims of provable security. We explicitly invite:
- Algebraic attacks (Gröbner basis)
- Differential cryptanalysis
- Lane-wise attacks (reducing 2⁵¹² to 8×2⁶⁴)
- Weak key analysis
- Preimage attacks

---

## 🎯 Quick Start

```bash
git clone https://github.com/MisterT92-OSS/fpch-crypto.git
cd fpch-crypto
python3 fpch_v6.py  # Recommended (47.9% avalanche)
python3 fpch_v5.py  # Paper reference (4.7% avalanche)
```

---

## 📁 Versions

| File | Avalanche | Description |
|---|---|---|
| `fpch_v6.py` | **47.9%** | Cross-lane diffusion, division-free (recommended) |
| `fpch_v5.py` | 4.7% | 100% paper-compliant (academic reference) |
| `fpch_v4.py` | 55.5% | Intermediate version |
| `fpch_working.py` | 42% | Simplified working version |
| `fpch_main.py` | 54.7% | Legacy (not paper-compliant) |

---

## 📐 Core Formula (V5)

```
P(x) = floor( (⌊√D⌋₁₂₈ · x² >> 64 + α·x + β) / (x + γ) ) mod 2⁶⁴
```

## 📐 V6 Improvements

- Cross-lane mixing after each round
- Division-free permutation (multiplication + XOR)
- MurmurHash-style non-linearity
- Golden ratio constant

---

## 🔬 Invite Cryptanalysis

We explicitly invite:
- Algebraic attacks (Gröbner basis)
- Differential cryptanalysis
- Lane-wise attacks (8 independent lanes)
- Weak key analysis

→ Open an [Issue](https://github.com/MisterT92-OSS/fpch-crypto/issues) or email toufik.salem.perso@pm.me

---

## 📄 Paper

`FPCH_Paper.pdf` (12 pages) includes:
- Sections 1-6: FPCH V5 specification
- Section 7: FPCH V6 proposed improvements
- Threat model, security analysis, open problems

---

## 📧 Contact

**Toufik Salem** — toufik.salem.perso@pm.me

*May 2026*
