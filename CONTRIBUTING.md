# Contributing to FPCH / Contribuer à FPCH

## 🎯 Invitation to Cryptanalysis / Invitation à la Cryptanalyse

This repository is explicitly positioned as an **"invitation to cryptanalysis"**. 
Ce repository est explicitement positionné comme une **"invitation à la cryptanalyse"**.

---

## How to Submit an Attack / Comment Soumettre une Attaque

### 1. Found a Vulnerability? / Vous avez trouvé une vulnérabilité?

**Open an issue** with label `cryptanalysis` / **Ouvrez une issue** avec le label `cryptanalysis`:
- Describe the attack / Décrivez l'attaque
- Provide proof-of-concept code / Fournissez un code de preuve de concept
- Include complexity analysis / Incluez l'analyse de complexité

### 2. Types of Attacks We Welcome / Types d'attaques bienvenues

| Attack Type | Description | Status |
|-------------|-------------|--------|
| **Algebraic attacks** | Express FPCH as low-degree polynomial equations / Exprimer FPCH comme équations polynomiales de bas degré | 🟡 Open |
| **Differential cryptanalysis** | Find differential probabilities / Trouver des probabilités différentielles | 🟡 Open |
| **Lane-wise attacks** | Exploit independent lane processing / Exploiter le traitement indépendant des lanes | 🟡 Open |
| **Weak keys** | Find parameter sets with weak behavior / Trouver des jeux de paramètres faibles | 🟡 Open |
| **Preimage attacks** | Find x such that FPCH(x) = y faster than O(2^n) / Trouver x tel que FPCH(x) = y plus vite que O(2^n) | 🟡 Open |

### 3. Submission Guidelines / Lignes directrices

```markdown
## Attack: [Name]

### Target
- Version: fpch_v5.py
- Component: [hash function / compression / parameter derivation]

### Description
[Brief description]

### Complexity
- Time: O(2^n)
- Memory: O(2^m)

### PoC Code
```python
# Proof of concept
```

### Impact
[What can an attacker do?]
```

---

## Bug Reports / Rapports de bugs

For non-security bugs: use label `bug` / Pour les bugs non-sécurité: utilisez le label `bug`

---

## Questions?

Contact: toufik.salem.perso@pm.me

---

**By Toufik Salem** - May 2026
