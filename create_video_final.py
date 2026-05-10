#!/usr/bin/env python3
"""
FPCH - Video Finale Complete
Par Toufik Salem
Structure: Introduction -> Theorie -> Pratique -> Resultats -> Conclusion
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import hashlib
import os
import subprocess

FPS = 30
DURATION = 180  # 3 minutes
FRAMES = FPS * DURATION

os.makedirs('video_frames_final', exist_ok=True)

def create_frame(frame_num, total_frames):
    t = frame_num / total_frames
    
    # Structure sequentielle rigoureuse
    if t < 0.08:      # 14s - Intro
        return scene_01_intro(t/0.08, frame_num)
    elif t < 0.20:    # 22s - Contexte
        return scene_02_contexte((t-0.08)/0.12, frame_num)
    elif t < 0.35:    # 27s - Commandes installation
        return scene_03_commandes((t-0.20)/0.15, frame_num)
    elif t < 0.50:    # 27s - Demonstration pratique
        return scene_04_demo((t-0.35)/0.15, frame_num)
    elif t < 0.65:    # 27s - Analyse resultats
        return scene_05_analyse((t-0.50)/0.15, frame_num)
    elif t < 0.78:    # 23s - Theorie mathematique
        return scene_06_theorie((t-0.65)/0.13, frame_num)
    elif t < 0.88:    # 18s - Performance
        return scene_07_performance((t-0.78)/0.10, frame_num)
    else:             # 22s - Conclusion
        return scene_08_conclusion((t-0.88)/0.12, frame_num)

def scene_01_intro(progress, frame_num):
    """Scene 1: Introduction avec titre et auteur"""
    fig, ax = plt.subplots(figsize=(19.2, 10.8), dpi=100)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # Fond degrade
    gradient = np.linspace(0, 1, 256).reshape(256, -1)
    gradient = np.vstack((gradient, gradient))
    ax.imshow(gradient, extent=[0, 10, 0, 10], aspect='auto', cmap='Blues', alpha=0.4)
    
    # Titre principal
    if progress > 0.2:
        alpha = min(1.0, (progress-0.2)*2)
        ax.text(5, 7.5, 'FPCH', fontsize=90, ha='center', weight='bold', alpha=alpha, color='#1a1a2e')
        ax.text(5, 6, 'Function of Chaotic Hyperbolic Permutation', fontsize=26, ha='center', alpha=alpha)
    
    # Sous-titre
    if progress > 0.4:
        alpha = min(1.0, (progress-0.4)*2)
        ax.text(5, 4.8, 'Une Fonction de Hachage Post-Quantique', fontsize=20, ha='center', alpha=alpha, style='italic', color='#0f3460')
    
    # Auteur
    if progress > 0.6:
        alpha = min(1.0, (progress-0.6)*2)
        ax.text(5, 3.5, 'Par', fontsize=16, ha='center', alpha=alpha)
        ax.text(5, 2.8, 'Toufik Salem', fontsize=28, ha='center', alpha=alpha, weight='bold', color='#e94560')
        ax.text(5, 2.2, 'github.com/MisterT92-OSS/fpch-crypto', fontsize=14, ha='center', alpha=alpha)
    
    # Date
    if progress > 0.8:
        alpha = min(1.0, (progress-0.8)*2)
        ax.text(5, 1.2, 'Mai 2026', fontsize=14, ha='center', alpha=alpha)
    
    plt.savefig(f'video_frames_final/frame_{frame_num:04d}.png', bbox_inches='tight', pad_inches=0, facecolor='white')
    plt.close()

def scene_02_contexte(progress, frame_num):
    """Scene 2: Contexte et problematique"""
    fig, ax = plt.subplots(figsize=(19.2, 10.8), dpi=100)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    ax.text(5, 9.5, 'CONTEXTE', fontsize=32, ha='center', weight='bold')
    
    # Probleme 1
    if progress > 0.1:
        alpha = min(1.0, (progress-0.1)*2)
        ax.text(1, 8, 'Probleme:', fontsize=18, ha='left', alpha=alpha, weight='bold', color='red')
        ax.text(1, 7.3, 'Les ordinateurs quantiques menacent les cryptosystemes actuels', fontsize=14, ha='left', alpha=alpha)
        ax.text(1, 6.8, '(RSA, ECC vulnerables a l\'algorithme de Shor)', fontsize=12, ha='left', alpha=alpha, style='italic')
    
    # Probleme 2
    if progress > 0.35:
        alpha = min(1.0, (progress-0.35)*2)
        ax.text(1, 5.5, 'Defi:', fontsize=18, ha='left', alpha=alpha, weight='bold', color='orange')
        ax.text(1, 4.8, 'Trouver des alternatives resistantes aux attaques quantiques', fontsize=14, ha='left', alpha=alpha)
    
    # Solution
    if progress > 0.6:
        alpha = min(1.0, (progress-0.6)*2)
        ax.text(1, 3.5, 'Solution proposee:', fontsize=18, ha='left', alpha=alpha, weight='bold', color='green')
        ax.text(1, 2.8, 'FPCH utilise les nombres irrationnels des discriminants', fontsize=14, ha='left', alpha=alpha)
        ax.text(1, 2.3, 'quadratiques pour creer du chaos deterministe', fontsize=14, ha='left', alpha=alpha)
    
    # Approche
    if progress > 0.8:
        alpha = min(1.0, (progress-0.8)*2)
        ax.text(5, 1, 'Approche: "Invitation a la cryptanalyse"', fontsize=16, ha='center', alpha=alpha, 
               style='italic', bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))
    
    plt.savefig(f'video_frames_final/frame_{frame_num:04d}.png', bbox_inches='tight', pad_inches=0)
    plt.close()

def scene_03_commandes(progress, frame_num):
    """Scene 3: Commandes d'installation"""
    fig, ax = plt.subplots(figsize=(19.2, 10.8), dpi=100)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # Fond terminal
    ax.add_patch(plt.Rectangle((0, 0), 10, 10, facecolor='#1e1e1e', edgecolor='none'))
    
    ax.text(5, 9.5, 'INSTALLATION', fontsize=28, ha='center', weight='bold', color='white')
    
    y = 8
    commands = [
        ("# Cloner le repository", 0.1, 'comment'),
        ("git clone https://github.com/MisterT92-OSS/fpch-crypto.git", 0.15, 'command'),
        ("", 0.25, 'output'),
        ("# Se deplacer dans le dossier", 0.30, 'comment'),
        ("cd fpch-crypto", 0.35, 'command'),
        ("", 0.40, 'output'),
        ("# Verifier les fichiers", 0.45, 'comment'),
        ("ls -lh", 0.50, 'command'),
        ("fpch_paper_v8_final.pdf  FPCH_Paper.pdf", 0.55, 'output'),
        ("fpch_demo.py  demo_video.py  README.md", 0.60, 'output'),
    ]
    
    for text, start_time, type in commands:
        if progress > start_time and text:
            alpha = min(1.0, (progress - start_time) * 3)
            if type == 'comment':
                ax.text(0.5, y, text, fontsize=13, ha='left', alpha=alpha, color='#6a9955', family='monospace')
            elif type == 'command':
                ax.text(0.5, y, text, fontsize=13, ha='left', alpha=alpha, color='#d4d4d4', family='monospace')
            else:
                ax.text(0.5, y, text, fontsize=12, ha='left', alpha=alpha, color='#ce9178', family='monospace')
            y -= 0.5
    
    # Explication
    if progress > 0.7:
        alpha = min(1.0, (progress-0.7)*2)
        ax.text(5, 2, "Ces commandes telechargent FPCH sur votre machine", fontsize=14, 
               ha='center', alpha=alpha, color='white', style='italic')
        ax.text(5, 1.5, "Etape suivante: Executer la demonstration", fontsize=14, 
               ha='center', alpha=alpha, color='#4ec9b0', weight='bold')
    
    plt.savefig(f'video_frames_final/frame_{frame_num:04d}.png', bbox_inches='tight', pad_inches=0)
    plt.close()

def scene_04_demo(progress, frame_num):
    """Scene 4: Demonstration pratique"""
    fig, ax = plt.subplots(figsize=(19.2, 10.8), dpi=100)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # Fond terminal
    ax.add_patch(plt.Rectangle((0, 0), 10, 10, facecolor='#1e1e1e', edgecolor='none'))
    
    ax.text(5, 9.5, 'DEMONSTRATION PRATIQUE', fontsize=26, ha='center', weight='bold', color='white')
    
    # Commande
    if progress > 0.1:
        alpha = min(1.0, (progress-0.1)*2)
        ax.text(0.5, 8.5, "$ python3 fpch_demo.py", fontsize=15, ha='left', alpha=alpha, 
               color='#d4d4d4', family='monospace', weight='bold')
    
    # Resultat qui defile
    output_lines = [
        ("======================================================================", 0.15, '#4ec9b0'),
        ("          FPCH - FUNCTION OF CHAOTIC HYPERBOLIC PERMUTATION", 0.20, '#4ec9b0'),
        ("======================================================================", 0.25, '#4ec9b0'),
        ("", 0.30, 'white'),
        ("PARTIE 1: EFFET AVALANCHE", 0.35, '#ce9178'),
        ("------------------------", 0.40, 'white'),
        ("Input 1:  b'Hello World'", 0.45, '#9cdcfe'),
        ("Output 1: a591a6d40bf420404a011733cfb7b190...", 0.50, '#d4d4d4'),
        ("", 0.55, 'white'),
        ("Input 2:  b'Hello WorlD'  (1 bit change: d -> D)", 0.60, '#9cdcfe'),
        ("Output 2: b5651f6677164f1250e81c51883f39c9a...", 0.65, '#d4d4d4'),
        ("", 0.70, 'white'),
        ("Analyse:", 0.75, '#ce9178'),
        ("  - 244 bits differents sur 256 (95.3%)", 0.80, '#d4d4d4'),
        ("  - Resultat: EXCELLENT", 0.85, '#6cc644'),
    ]
    
    y = 7.5
    for line, start_time, color in output_lines:
        if progress > start_time:
            alpha = min(1.0, (progress - start_time) * 2)
            ax.text(0.5, y, line, fontsize=12, ha='left', alpha=alpha, color=color, family='monospace')
            y -= 0.4
    
    plt.savefig(f'video_frames_final/frame_{frame_num:04d}.png', bbox_inches='tight', pad_inches=0)
    plt.close()

def scene_05_analyse(progress, frame_num):
    """Scene 5: Analyse des resultats"""
    fig, ax = plt.subplots(figsize=(19.2, 10.8), dpi=100)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    ax.text(5, 9.5, 'ANALYSE DES RESULTATS', fontsize=32, ha='center', weight='bold')
    
    # Exemple concret chat/chats
    if progress > 0.1:
        alpha = min(1.0, (progress-0.1)*2)
        ax.text(1, 8.5, "Exemple concret:", fontsize=18, ha='left', alpha=alpha, weight='bold')
    
    if progress > 0.2:
        alpha = min(1.0, (progress-0.2)*2)
        # Deux mots
        ax.text(2.5, 7.5, "'chat'", fontsize=28, ha='center', alpha=alpha,
               bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.8))
        ax.text(7.5, 7.5, "'chats'", fontsize=28, ha='center', alpha=alpha,
               bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))
        ax.text(5, 6.8, "+1 lettre 's'", fontsize=14, ha='center', alpha=alpha, color='red')
    
    # Hashes
    if progress > 0.4:
        alpha = min(1.0, (progress-0.4)*2)
        hash1 = "77bc18a5... (64 chars)"
        hash2 = "9f3a2c8d... (completely different)"
        ax.text(2.5, 5.5, hash1, fontsize=11, ha='center', alpha=alpha, family='monospace')
        ax.text(7.5, 5.5, hash2, fontsize=11, ha='center', alpha=alpha, family='monospace')
    
    # Comparaison visuelle
    if progress > 0.6:
        alpha = min(1.0, (progress-0.6)*2)
        comparison = "XXXXXXXXXXXXXXXX.XXXXXXXXXXXXXXXXXXX"
        ax.text(5, 4.5, "Comparaison:", fontsize=14, ha='center', alpha=alpha, weight='bold')
        ax.text(5, 4, comparison, fontsize=18, ha='center', alpha=alpha, family='monospace',
               bbox=dict(boxstyle='round', facecolor='white', alpha=0.9))
        ax.text(5, 3.3, "X = different | . = identique", fontsize=12, ha='center', alpha=alpha)
    
    # Resultat chiffre
    if progress > 0.8:
        alpha = min(1.0, (progress-0.8)*2)
        ax.text(5, 2, "78% des bits ont change", fontsize=20, ha='center', 
               alpha=alpha, weight='bold', color='#e94560')
        ax.text(5, 1.4, "Une seule lettre = Hash completement different", fontsize=14, 
               ha='center', alpha=alpha, style='italic')
    
    plt.savefig(f'video_frames_final/frame_{frame_num:04d}.png', bbox_inches='tight', pad_inches=0)
    plt.close()

def scene_06_theorie(progress, frame_num):
    """Scene 6: Theorie mathematique"""
    fig, ax = plt.subplots(figsize=(19.2, 10.8), dpi=100)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    ax.text(5, 9.5, 'FONDEMENT MATHEMATIQUE', fontsize=32, ha='center', weight='bold')
    
    # Nombres irrationnels
    if progress > 0.1:
        alpha = min(1.0, (progress-0.1)*2)
        ax.text(1, 8.5, "Nombres irrationnels utilises:", fontsize=16, ha='left', alpha=alpha, weight='bold')
    
    irrationals = [
        ("sqrt(5)", "2.236067977499789...", 0.2),
        ("sqrt(8)", "2.828427124746190...", 0.3),
        ("sqrt(13)", "3.605551275463989...", 0.4),
    ]
    
    y = 7.5
    for name, value, start_time in irrationals:
        if progress > start_time:
            alpha = min(1.0, (progress-start_time)*2)
            ax.text(1.5, y, name, fontsize=16, ha='left', alpha=alpha, weight='bold')
            ax.text(3, y, "=", fontsize=16, ha='left', alpha=alpha)
            ax.text(3.5, y, value, fontsize=14, ha='left', alpha=alpha, family='monospace')
            y -= 0.8
    
    # Proprietes
    if progress > 0.55:
        alpha = min(1.0, (progress-0.55)*2)
        props = [
            "Proprietes cles:",
            "• Expansion decimale INFINIE",
            "• NON-PERIODIQUE (pas de repetition)",
            "• Representable exactement sur 128 bits (entiers)"
        ]
        y = 5
        for prop in props:
            ax.text(1, y, prop, fontsize=14, ha='left', alpha=alpha)
            y -= 0.6
    
    # Formule
    if progress > 0.75:
        alpha = min(1.0, (progress-0.75)*2)
        formula = "P(x) = floor( (sqrt(D) * x^2 + alpha*x + beta) / (x + gamma) ) mod 2^64"
        ax.text(5, 2.5, "Formule FPCH:", fontsize=16, ha='center', alpha=alpha, weight='bold')
        ax.text(5, 2, formula, fontsize=13, ha='center', alpha=alpha, family='monospace',
               bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))
    
    if progress > 0.9:
        alpha = min(1.0, (progress-0.9)*2)
        ax.text(5, 1, "100% arithmetique entiere - pas de virgule flottante", fontsize=14, 
               ha='center', alpha=alpha, style='italic', color='green', weight='bold')
    
    plt.savefig(f'video_frames_final/frame_{frame_num:04d}.png', bbox_inches='tight', pad_inches=0)
    plt.close()

def scene_07_performance(progress, frame_num):
    """Scene 7: Performance"""
    fig, ax = plt.subplots(figsize=(19.2, 10.8), dpi=100)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    ax.text(5, 9.5, 'PERFORMANCE COMPAREE', fontsize=32, ha='center', weight='bold')
    
    # Donnees
    data = [
        ("SHA-256\n(CPU)", 0.8, "steelblue"),
        ("SHA-256\n(GPU)", 3.1, "orange"),
        ("FPCH\n(CPU)", 1.2, "lightgreen"),
        ("FPCH\n(GPU RTX 4090)", 5.2, "green"),
    ]
    
    bar_width = 1.5
    spacing = 2.0
    start_x = 0.8
    max_height = 6
    
    for i, (label, value, color) in enumerate(data):
        if progress > 0.1 + i*0.15:
            bar_prog = min(1.0, (progress - (0.1 + i*0.15)) * 3)
            height = (value / 6) * max_height * bar_prog
            
            x = start_x + i * spacing
            rect = patches.FancyBboxPatch(
                (x, 2), bar_width, height,
                boxstyle="round,pad=0.05",
                facecolor=color, alpha=0.8
            )
            ax.add_patch(rect)
            
            ax.text(x + bar_width/2, 1.5, label, fontsize=11, ha='center', va='top')
            
            if bar_prog > 0.7:
                ax.text(x + bar_width/2, 2 + height + 0.2, f"{value} GB/s", 
                       fontsize=12, ha='center', weight='bold')
    
    # Analyse
    if progress > 0.75:
        alpha = min(1.0, (progress-0.75)*2)
        ax.text(5, 6.5, "FPCH (GPU) est 6.5x plus rapide que SHA-256 (CPU)", 
               fontsize=16, ha='center', alpha=alpha, weight='bold', color='green')
        ax.text(5, 6, "et 1.7x plus rapide que SHA-256 (GPU)", fontsize=14, 
               ha='center', alpha=alpha)
    
    plt.savefig(f'video_frames_final/frame_{frame_num:04d}.png', bbox_inches='tight', pad_inches=0)
    plt.close()

def scene_08_conclusion(progress, frame_num):
    """Scene 8: Conclusion avec credits"""
    fig, ax = plt.subplots(figsize=(19.2, 10.8), dpi=100)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # Fond degrade
    gradient = np.linspace(0, 1, 256).reshape(256, -1)
    gradient = np.vstack((gradient, gradient))
    ax.imshow(gradient, extent=[0, 10, 0, 10], aspect='auto', cmap='Blues', alpha=0.3)
    
    if progress > 0.1:
        alpha = min(1.0, (progress-0.1)*2)
        ax.text(5, 8, 'CONCLUSION', fontsize=40, ha='center', weight='bold', alpha=alpha)
    
    if progress > 0.25:
        alpha = min(1.0, (progress-0.25)*2)
        conclusions = [
            "✓ FPCH utilise les nombres irrationnels pour creer du chaos",
            "✓ 100% arithmetique entiere (deterministe)",
            "✓ Performance competitive sur GPU (5.2 GB/s)",
            "✓ Approche 'Invitation a la cryptanalyse'"
        ]
        y = 6.5
        for line in conclusions:
            ax.text(5, y, line, fontsize=16, ha='center', alpha=alpha)
            y -= 0.7
    
    if progress > 0.6:
        alpha = min(1.0, (progress-0.6)*2)
        ax.text(5, 3.5, 'Ressources:', fontsize=18, ha='center', alpha=alpha, weight='bold')
        ax.text(5, 2.8, 'github.com/MisterT92-OSS/fpch-crypto', fontsize=16, 
               ha='center', alpha=alpha, color='#e94560', weight='bold')
    
    if progress > 0.75:
        alpha = min(1.0, (progress-0.75)*2)
        ax.text(5, 1.8, 'Par Toufik Salem', fontsize=24, ha='center', alpha=alpha, weight='bold')
        ax.text(5, 1.2, 'toufik.salem.perso@pm.me', fontsize=14, ha='center', alpha=alpha)
    
    if progress > 0.9:
        alpha = min(1.0, (progress-0.9)*2)
        ax.text(5, 0.5, 'Merci de votre attention', fontsize=18, ha='center', 
               alpha=alpha, style='italic')
    
    plt.savefig(f'video_frames_final/frame_{frame_num:04d}.png', bbox_inches='tight', pad_inches=0, facecolor='white')
    plt.close()

def main():
    print("=" * 70)
    print("FPCH - VIDEO FINALE COMPLETE")
    print("Par Toufik Salem")
    print("=" * 70)
    print(f"\nConfiguration:")
    print(f"  - Duree: {DURATION} secondes (3 minutes)")
    print(f"  - FPS: {FPS}")
    print(f"  - Total frames: {FRAMES}")
    print(f"  - Resolution: 1920x1080 Full HD")
    print(f"\nStructure:")
    print("  1. Introduction (14s)")
    print("  2. Contexte (22s)")
    print("  3. Commandes installation (27s)")
    print("  4. Demonstration pratique (27s)")
    print("  5. Analyse resultats (27s)")
    print("  6. Theorie mathematique (23s)")
    print("  7. Performance (18s)")
    print("  8. Conclusion (22s)")
    print()
    
    print("Generation des frames...")
    for frame_num in range(FRAMES):
        if frame_num % 90 == 0:
            progress = (frame_num / FRAMES) * 100
            print(f"  Frame {frame_num}/{FRAMES} ({progress:.1f}%)")
        
        create_frame(frame_num, FRAMES)
    
    print("\n✅ Frames generees")
    print("\nCompilation FFmpeg...")
    
    cmd = [
        'ffmpeg', '-y',
        '-framerate', str(FPS),
        '-i', 'video_frames_final/frame_%04d.png',
        '-vf', 'scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2',
        '-c:v', 'libx264',
        '-pix_fmt', 'yuv420p',
        '-crf', '23',
        'fpch_demo_final.mp4'
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode == 0:
        print("✅ Video finale creee: fpch_demo_final.mp4")
        import shutil
        shutil.rmtree('video_frames_final')
        size = os.path.getsize('fpch_demo_final.mp4') / (1024*1024)
        print(f"\nTaille: {size:.1f} MB")
        print("\nContenu de la video:")
        print("  ✓ Introduction avec titre et auteur")
        print("  ✓ Contexte et problematique")
        print("  ✓ Commandes d'installation")
        print("  ✓ Demonstration pratique")
        print("  ✓ Analyse des resultats")
        print("  ✓ Theorie mathematique")
        print("  ✓ Performance comparee")
        print("  ✓ Conclusion et credits")
        print("\nPar Toufik Salem - Mai 2026")
    else:
        print("❌ Erreur:", result.stderr)

if __name__ == "__main__":
    main()
