# FPCH - Function of Chaotic Hyperbolic Permutation
## Par Toufik Salem

**Une Invitation à la Cryptanalyse**

---

## 📋 Description

FPCH est une fonction de hachage cryptographique qui utilise les **nombres irrationnels** des discriminants quadratiques pour créer du chaos mathématique déterministe. Contrairement aux constructions traditionnelles basées sur des groupes algébriques (RSA, ECC vulnérables à l'algorithme de Shor), FPCH exploite l'irrationalité des racines carrées (√5, √8, √13...) comme source d'entropie.

---

## 🚀 Démarrage Rapide

```bash
# Cloner le repository
git clone https://github.com/MisterT92-OSS/fpch-crypto.git
cd fpch-crypto

# Exécuter la démonstration (Version 4 - Recommandée)
python3 fpch_v4.py

# Ou la version 100% conforme au papier
python3 fpch_v5.py
```

---

## 📁 Versions Disponibles

| Fichier | Description | Statut |
|---------|-------------|--------|
| **`fpch_v5.py`** | **Version 5** - Implémentation complète FPCH-512 conforme au papier académique v8. Inclut HKDF, 8 lanes, IV dérivé de √D. | ✅ **Référence académique** |
| **`fpch_v4.py`** | **Version 4** - Implémentation corrigée avec tous les patches (integer_sqrt exact, formule FPCH authentique). | ✅ **Recommandée** |
| **`fpch_working.py`** | Version simplifiée fonctionnelle (64-bit) avec bonne avalanche (42%). | ✅ Démonstration |
| `fpch_paper_v8_final.pdf` | Papier académique complet (9 pages). | 📄 Publication |

---

## 🎯 Versions Vidéo

- `fpch_demo_final.mp4` - Vidéo de démonstration (Français, 3 min)
- `fpch_demo_final_en.mp4` - Vidéo de démonstration (Anglais, 3 min)

---

## 🔬 Spécifications Techniques

### Paramètres
- **Sortie** : 512 bits (8 lanes × 64 bits)
- **Discriminants** : 64 discriminants fondamentaux positifs
- **Couches** : 16 rounds FPCH par lane
- **Construction** : Merkle-Damgård

### Formule Mathématique
```
P(x) = ⌊(⌊√D⌋₁₂₈ · x² ≫ 64 + α·x + β) / (x + γ)⌋ mod 2⁶⁴
```

Où :
- D ∈ {5, 8, 12, 13, 17, 21, 24, 28, ...} (discriminants fondamentaux)
- √D est irrationnel (fraction continue infinie non-périodique)
- Tous les calculs utilisent l'**arithmétique entière exacte**

---

## 🛡️ Limitations Connues

Conformément à l'**honnêteté intellectuelle** du papier :

1. **Lane Independence** : Les 8 lanes sont traitées indépendamment, ce qui réduit la diffusion inter-lanes (Section 6.3 du papier).
2. **Aucune preuve formelle** de sécurité sous des hypothèses standard.
3. **Construction préliminaire** : Cette implémentation est une invitation à la cryptanalyse.

---

## 📧 Contact

**Toufik Salem**
- Email : toufik.salem.perso@pm.me
- GitHub : https://github.com/MisterT92-OSS/fpch-crypto
- Affiliation : Chercheur indépendant

---

## ⚠️ Avertissement

Ce travail est de la **recherche expérimentale**. Ne pas utiliser en production sans validation cryptographique approfondie par la communauté.

---

*Mai 2026*
