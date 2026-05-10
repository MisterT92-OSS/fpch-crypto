# FPCH - Commandes Essentielles

## 1. CLONER LE REPO

```bash
git clone https://github.com/MisterT92-OSS/fpch-crypto.git
cd fpch-crypto
```

## 2. LANCER LA DÉMO CONSOLE

```bash
python3 fpch_demo.py
```

**Résultat attendu :**
```
======================================================================
          FPCH - FUNCTION OF CHAOTIC HYPERBOLIC PERMUTATION
======================================================================

1️⃣  Démonstration d'Avalanche
...
```

## 3. LANCER LA DÉMO VIDÉO (ASCII)

```bash
python3 demo_video.py
```

**Puis appuyez sur ENTRÉE pour avancer entre les scènes**

## 4. LANCER LES TESTS NIST

```bash
cd tests
python3 fpch_test_suite.py
```

**Résultat attendu :**
```
Tests NIST SP 800-22:
✓ 1. Frequency (Monobit) - PASSED
✓ 2. Frequency within Block - PASSED
...
15/15 tests passed
```

## 5. COMPILER LE PAPIER LaTeX

### Prérequis : BasicTeX installé

```bash
cd ~
eval "$(/usr/libexec/path_helper)"
cd /chemin/vers/votre/workspace
pdflatex fpch_paper_v8_final.tex
```

**Résultat :** `fpch_paper_v8_final.pdf` (9 pages, 262 KB)

## 6. GÉNÉRER UNE VIDÉO MP4

### Prérequis : matplotlib + ffmpeg

```bash
pip3 install matplotlib --break-system-packages
python3 create_video_v2.py
```

**Résultat :** `fpch_demo_v2.mp4` (2 minutes, Full HD)

## 7. VÉRIFIER LES FICHIERS

```bash
ls -lh
```

**Doit afficher :**
```
-rw-r--r--  1 user  staff   262K  fpch_paper_v8_final.pdf
-rw-r--r--  1 user  staff   1.5M  fpch_demo_v2.mp4
-rw-r--r--  1 user  staff   9.9K  fpch_demo.py
-rw-r--r--  1 user  staff   697B  README.md
```

## 8. POUSSER DES MODIFICATIONS SUR GITHUB

```bash
git add .
git commit -m "Description des changements"
git push origin main
```

## COMMANDES DE DÉBOGAGE

### Vérifier Python
```bash
python3 --version
# Doit afficher : Python 3.x.x
```

### Vérifier LaTeX
```bash
which pdflatex
pdflatex --version
```

### Vérifier FFmpeg
```bash
which ffmpeg
ffmpeg -version | head -1
```

### Nettoyer les fichiers temporaires
```bash
rm -f *.aux *.log *.out
rm -rf video_frames/
```

## EXEMPLE DE SESSION COMPLÈTE

```bash
# 1. Se placer dans le dossier
cd ~/fpch-crypto

# 2. Lancer la démo
python3 fpch_demo.py

# 3. Voir les résultats
ls -lh

# 4. Ouvrir le PDF
open FPCH_Paper.pdf  # Mac
# ou : xdg-open FPCH_Paper.pdf  # Linux
```

## CONTACT

**Problèmes ?**
- Email : toufik.salem.perso@pm.me
- GitHub : https://github.com/MisterT92-OSS/fpch-crypto/issues
