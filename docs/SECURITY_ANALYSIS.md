# FPCH Security Analysis

**Version:** V6 (2026-05-14)
**Author:** Toufik Salem
**Status:** Invitation to Cryptanalysis

---

## 1. Threat Model

We consider three attacker profiles:

| Profile | Capability | Goal |
|---|---|---|
| **Classical** | Black-box oracle, adaptive queries, CPU clusters | Collision, preimage, or distinguisher from random oracle |
| **GPU** | Parallel exploitation of 8 lanes | Reduce effective security from $2^{512}$ to $8 \times 2^{64}$ if lanes can be attacked independently |
| **Quantum (limited)** | Grover-capable, **not** Shor-capable | Quantum preimage search; structural resistance to Shor is a design feature, not a proof |

---

## 2. Structural Properties

### 2.1 Parameter Sensitivity (Theorem)
For fixed $D$ and $(\alpha, \beta) \neq (\alpha', \beta')$:
$$\Pr_{x}[P_{\alpha,\beta}(x) = P_{\alpha',\beta'}(x)] \leq 2^{-32}$$

**Implication:** Distinct HKDF-derived parameter sets produce functions that differ on at least $2^{64} - 2^{32}$ inputs.

### 2.2 Algebraic Resistance (Theorem)
For any polynomial $q(x) \in \mathbb{F}_2[x]$ of degree $d < 2^{48}$:
$$\Pr_{x}[P(x) = q(x)] \leq \frac{d + 2^{32}}{2^{64}}$$

**Implication:** FPCH resists low-degree polynomial approximation (including certain Gröbner basis attacks). High-degree approximations remain possible and are explicitly invited.

### 2.3 Continued-Fraction Non-Periodicity (Lemma)
For $D \in \mathcal{D}^+$, the partial quotients of $\sqrt{D}$ are unbounded for infinitely many $D$.

**Implication:** The irrationality-based seeding does not collapse to short periodic sequences with high probability.

---

## 3. Known Weaknesses

### 3.1 V5 Weaknesses (Legacy)
- **Lane independence:** 8 lanes processed independently until final XOR.
- **Non-invertible division:** Division modulo $2^{64}$ fails for even denominators.
- **Weak avalanche:** $4.7\%$ bit change on 1-bit input perturbation.

### 3.2 V6 Residual Risks
- **No formal proof of collision resistance** beyond birthday bound.
- **No reduction to standard hard problems** (LWE, SIS, etc.).
- **No memory-hardness:** Vulnerable to ASIC/FPGA acceleration.
- **No side-channel analysis:** Timing, power, and cache attacks not evaluated.
- **Quantum resistance is structural only:** Grover still applies ($O(2^{n/2})$ preimage).

---

## 4. Attack Surface We Invite

### 4.1 Algebraic Attacks
- Express FPCH as a system of polynomial equations over $\mathbb{Z}_{2^{64}}$ or $\mathbb{F}_2$.
- Compute Gröbner basis complexity for 1-round and 16-round instances.

### 4.2 Differential Cryptanalysis
- Compute expected differential probability for $P(x) \oplus P(x \oplus \Delta)$.
- Search for high-probability differentials over multiple rounds.

### 4.3 Lane-Wise Attacks
- Exploit the 8-lane architecture before final global mixing.
- Meet-in-the-middle on intermediate states.

### 4.4 Weak Key / Weak Parameter Search
- Are there parameter sets $(\alpha, \beta, \gamma, D)$ that produce linear or near-linear behavior?
- Does HKDF derivation ever output weak parameters with high probability?

### 4.5 Preimage and Second-Preimage
- Is finding $x$ such that $\text{FPCH}(x) = y$ easier than exhaustive search?
- Is the division-free V6 layer easier to invert algebraically than V5?

---

## 5. Responsible Disclosure

If you discover a practical attack (collision, preimage, or distinguisher significantly better than generic bounds), please:

1. Open a private security advisory on GitHub, **or**
2. Email **toufik.salem.perso@pm.me** with subject `[FPCH] Security Finding`.

We commit to acknowledging receipt within 72 hours and publishing a credited analysis within 30 days.

---

## 6. References

- Alvarez & Li, "Some basic cryptographic requirements for chaos-based cryptosystems," IJBC 2006.
- Courtois & Meier, "Algebraic attacks on stream ciphers with linear feedback," EUROCRYPT 2003.
- Biham & Shamir, "Differential cryptanalysis of DES-like cryptosystems," Journal of Cryptology 1991.
- NIST SP 800-22 Rev. 1a, "A Statistical Test Suite for Random and Pseudorandom Number Generators."
