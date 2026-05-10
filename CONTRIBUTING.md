# Contributing to FPCH

## How to Submit a Cryptanalytic Attack

1. **Open an Issue** with label `cryptanalysis`
2. Describe the attack vector (algebraic, differential, lane-wise, etc.)
3. Provide reproducible code or proof-of-concept
4. We will acknowledge all valid findings in the paper

## Attack Vectors We Explicitly Invite

- **Algebraic attacks**: Can FPCH be expressed as low-degree polynomials over Z/2⁶⁴?
- **Differential cryptanalysis**: Expected differential probabilities for P(x) ⊕ P(x⊕Δ)?
- **Lane-wise attacks**: Exploit 8 independent lanes to reduce complexity from 2⁵¹² to 8×2⁶⁴
- **Weak keys**: Are there master seeds producing linear or degenerate behavior?
- **Preimage attacks**: Finding x such that FPCH(x) = y faster than O(2ⁿ)?

## Reference Implementation

Always use `fpch_v5.py` — it is the only paper-compliant implementation.

## Contact

toufik.salem.perso@pm.me
