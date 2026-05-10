#!/bin/bash
# Script de nettoyage du repository FPCH
# Garde uniquement l'essentiel

echo "Nettoyage du repository FPCH..."

# Supprimer les fichiers Python obsolètes
rm -f fpch_hash.py fpch_correct.py fpch512.py fpch512_v2.py fpch_demo.py 
rm -f fpch_demo_concept.py fpch_reference.py fpch_minimal.py

# Supprimer les scripts de video intermédiaires
rm -f create_video.py create_video_v2.py create_video_v3.py create_video_real.py
rm -f demo_video.py demo_visual.py

# Supprimer les videos intermédiaires
rm -f fpch_demo.mp4 fpch_demo_v2.mp4

# Supprimer les scripts de test non-essentiels
rm -f fpch_test_suite.py

echo "Nettoyage termine."
echo ""
echo "Fichiers conserves:"
echo "  - fpch_main.py (version principale recommandee)"
echo "  - fpch_v5.py (version 100% conforme au papier)"
echo "  - fpch_v4.py (version avec correctifs)"
echo "  - fpch_working.py (version simplifiee)"
echo "  - FPCH_Paper.pdf (papier academique)"
echo "  - README.md, README_FR.md, README_EN.md (documentation)"
echo "  - COMMANDS.md (guide des commandes)"
echo "  - fpch_demo_final.mp4, fpch_demo_final_en.mp4 (videos)"
echo "  - create_video_final.py, create_video_final_en.py (scripts video)"
echo "  - cuda/fpch_cuda_advanced.cu (implementation GPU)"
echo "  - source.tex (source LaTeX du papier)"
echo "  - tests/fpch_test_suite.py (tests NIST)"
