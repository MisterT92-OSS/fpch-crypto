# FPCH - Function of Chaotic Hyperbolic Permutation
## By Toufik Salem

**An Invitation to Cryptanalysis**

---

## 📋 Description

FPCH is a cryptographic hash function that uses **irrational numbers** from quadratic field discriminants to create deterministic mathematical chaos. Unlike traditional constructions based on algebraic groups (RSA, ECC vulnerable to Shor's algorithm), FPCH exploits the irrationality of square roots (√5, √8, √13...) as an entropy source.

---

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/MisterT92-OSS/fpch-crypto.git
cd fpch-crypto

# Run the demonstration (Version 4 - Recommended)
python3 fpch_v4.py

# Or the version 100% compliant with the paper
python3 fpch_v5.py
```

---

## 📁 Available Versions

| File | Description | Status |
|---------|-------------|--------|
| **`fpch_v5.py`** | **Version 5** - Complete FPCH-512 implementation compliant with academic paper v8. Includes HKDF, 8 lanes, IV derived from √D. | ✅ **Academic Reference** |
| **`fpch_v4.py`** | **Version 4** - Patched implementation with all fixes (exact integer_sqrt, authentic FPCH formula). | ✅ **Recommended** |
| **`fpch_working.py`** | Simplified working version (64-bit) with good avalanche (42%). | ✅ Demonstration |
| `fpch_paper_v8_final.pdf` | Complete academic paper (9 pages). | 📄 Publication |

---

## 🎯 Video Versions

- `fpch_demo_final.mp4` - Demonstration video (French, 3 min)
- `fpch_demo_final_en.mp4` - Demonstration video (English, 3 min)

---

## 🔬 Technical Specifications

### Parameters
- **Output** : 512 bits (8 lanes × 64 bits)
- **Discriminants** : 64 positive fundamental discriminants
- **Layers** : 16 FPCH rounds per lane
- **Construction** : Merkle-Damgård

### Mathematical Formula
```
P(x) = ⌊(⌊√D⌋₁₂₈ · x² ≫ 64 + α·x + β) / (x + γ)⌋ mod 2⁶⁴
```

Where :
- D ∈ {5, 8, 12, 13, 17, 21, 24, 28, ...} (fundamental discriminants)
- √D is irrational (infinite non-periodic continued fraction)
- All calculations use **exact integer arithmetic**

---

## 🛡️ Known Limitations

In accordance with **intellectual honesty** from the paper:

1. **Lane Independence** : The 8 lanes are processed independently, which reduces inter-lane diffusion (Section 6.3 of the paper).
2. **No formal proof** of security under standard assumptions.
3. **Preliminary construction** : This implementation is an invitation to cryptanalysis.

---

## 📧 Contact

**Toufik Salem**
- Email : toufik.salem.perso@pm.me
- GitHub : https://github.com/MisterT92-OSS/fpch-crypto
- Affiliation : Independent Researcher

---

## ⚠️ Disclaimer

This work is **experimental research**. Do not use in production without thorough cryptographic validation by the community.

---

*May 2026*
