# FPCH — Function of Chaotic Hyperbolic Permutation

**By Toufik Salem | An Invitation to Cryptanalysis**

> ⚠️ Experimental research. Do not use in production without community validation.

---

## 🎯 Reference Implementation

```bash
git clone https://github.com/MisterT92-OSS/fpch-crypto.git
cd fpch-crypto
python3 fpch_v5.py # 100% paper-compliant (512-bit, HKDF, 8 lanes)
```

---

## 📁 Files

| File | Description | Status |
|---|---|---|
| `fpch_v5.py` | **512-bit, HKDF, 8 lanes — exact paper implementation** | ✅ **Reference** |
| `fpch_v4.py` | 64-bit, all formula fixes applied | 🔧 Intermediate |
| `fpch_main.py` | Earlier version (bits=60, not paper-compliant) | ⚠️ Legacy |
| `FPCH_Paper.pdf` | Academic paper (9 pages) | 📄 Publication |
| `cuda/` | GPU implementation (RTX 4090 benchmark) | 🚧 Experimental |

---

## 📐 Core Formula (Definition 3.1)

```
P(x) = floor( (⌊√D⌋₁₂₈ · x² >> 64 + α·x + β) / (x + γ) ) mod 2⁶⁴
```

Where D ∈ D⁺₆₄ (first 64 positive fundamental discriminants).

---

## 🔬 Invite Cryptanalysis

We explicitly invite:
- Algebraic attacks (Gröbner basis)
- Differential cryptanalysis
- Lane-wise attacks (8 independent lanes)
- Weak key analysis

→ Open an [Issue](https://github.com/MisterT92-OSS/fpch-crypto/issues) or email toufik.salem.perso@pm.me

---

## 📧 Contact

**Toufik Salem** — toufik.salem.perso@pm.me

*May 2026*
