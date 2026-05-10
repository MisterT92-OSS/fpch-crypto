# FPCH — Function of Chaotic Hyperbolic Permutation

**By Toufik Salem | An Invitation to Cryptanalysis**

> ⚠️ Experimental research. Do not use in production without community validation.

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
