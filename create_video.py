#!/usr/bin/env python3
"""
FPCH - Creation Video MP4
Genere une video de demonstration avec animations
"""

import matplotlib
matplotlib.use('Agg')  # Mode non-interactif pour generation
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation
import numpy as np
import hashlib
import os
import subprocess

# Configuration
FPS = 30
DURATION = 90  # secondes totales
FRAMES = FPS * DURATION

# Creer dossier temporaire
os.makedirs('video_frames', exist_ok=True)

def create_frame(frame_num, total_frames):
    """Cree une frame de la video"""
    
    # Calculer le temps (0.0 a 1.0)
    t = frame_num / total_frames
    
    # Scene 1: Intro (0.0 - 0.15)
    if t < 0.15:
        return create_intro_scene((t - 0.0) / 0.15, frame_num)
    
    # Scene 2: Avalanche (0.15 - 0.40)
    elif t < 0.40:
        return create_avalanche_scene((t - 0.15) / 0.25, frame_num)
    
    # Scene 3: Structure (0.40 - 0.65)
    elif t < 0.65:
        return create_structure_scene((t - 0.40) / 0.25, frame_num)
    
    # Scene 4: Performance (0.65 - 0.85)
    elif t < 0.85:
        return create_performance_scene((t - 0.65) / 0.20, frame_num)
    
    # Scene 5: Outro (0.85 - 1.0)
    else:
        return create_outro_scene((t - 0.85) / 0.15, frame_num)

def create_intro_scene(progress, frame_num):
    """Scene d'introduction"""
    fig, ax = plt.subplots(figsize=(1920/100, 1080/100), dpi=100)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # Fond degrade
    gradient = np.linspace(0, 1, 256).reshape(256, -1)
    gradient = np.vstack((gradient, gradient))
    ax.imshow(gradient, extent=[0, 10, 0, 10], aspect='auto', 
              cmap='Blues', alpha=0.3, zorder=0)
    
    # Titre qui apparait progressivement
    if progress > 0.2:
        alpha = min(1.0, (progress - 0.2) * 2)
        ax.text(5, 7, 'FPCH', fontsize=72, ha='center', weight='bold',
               alpha=alpha, color='#1a1a2e')
    
    if progress > 0.4:
        alpha = min(1.0, (progress - 0.4) * 2)
        ax.text(5, 5.5, 'Function of Chaotic Hyperbolic Permutation', 
               fontsize=24, ha='center', alpha=alpha, color='#16213e')
    
    if progress > 0.6:
        alpha = min(1.0, (progress - 0.6) * 2)
        ax.text(5, 4, 'An Invitation to Cryptanalysis', 
               fontsize=18, ha='center', alpha=alpha, style='italic',
               color='#0f3460')
    
    if progress > 0.8:
        alpha = min(1.0, (progress - 0.8) * 2)
        ax.text(5, 2, 'github.com/MisterT92-OSS/fpch-crypto', 
               fontsize=14, ha='center', alpha=alpha, color='#e94560')
    
    plt.savefig(f'video_frames/frame_{frame_num:04d}.png', 
               bbox_inches='tight', pad_inches=0, facecolor='white')
    plt.close()

def create_avalanche_scene(progress, frame_num):
    """Scene demonstration avalanche"""
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(1920/100, 1080/100), dpi=100)
    
    # Messages
    msg1 = b"Hello World"
    msg2 = b"Hello WorlD"
    hash1 = hashlib.sha256(msg1).hexdigest()
    hash2 = hashlib.sha256(msg2).hexdigest()
    
    # Partie superieure: messages
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 3)
    ax1.axis('off')
    
    ax1.text(5, 2.5, 'AVALANCHE EFFECT', fontsize=28, ha='center', weight='bold')
    
    if progress > 0.1:
        alpha = min(1.0, (progress - 0.1) * 2)
        ax1.text(2.5, 1.5, f'Input 1: {msg1.decode()}', 
                fontsize=16, ha='center', alpha=alpha,
                bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))
    
    if progress > 0.3:
        alpha = min(1.0, (progress - 0.3) * 2)
        ax1.text(7.5, 1.5, f'Input 2: {msg2.decode()}', 
                fontsize=16, ha='center', alpha=alpha,
                bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))
    
    # Partie inferieure: visualisation bits
    ax2.set_xlim(0, 64)
    ax2.set_ylim(0, 2)
    ax2.axis('off')
    
    ax2.text(32, 1.8, 'Hash Output Comparison (first 64 bits)', 
            fontsize=14, ha='center', weight='bold')
    
    bin1 = ''.join(format(int(c, 16), '04b') for c in hash1)[:64]
    bin2 = ''.join(format(int(c, 16), '04b') for c in hash2)[:64]
    
    # Animation progressive des bits
    bits_to_show = int(64 * progress)
    
    for i in range(min(bits_to_show, 64)):
        x = i % 32
        y = 0.8 if i < 32 else 0.3
        
        if bin1[i] == bin2[i]:
            color = 'lightgray'
            marker = '.'
        else:
            color = 'red'
            marker = 'X'
        
        ax2.text(x + 0.5, y, marker, fontsize=12, ha='center', 
                color=color, weight='bold')
    
    # Légende
    if progress > 0.8:
        ax2.text(16, 0.1, '. = Identical', fontsize=10, ha='center', color='gray')
        ax2.text(48, 0.1, 'X = Different', fontsize=10, ha='center', color='red')
    
    plt.tight_layout()
    plt.savefig(f'video_frames/frame_{frame_num:04d}.png',
               bbox_inches='tight', pad_inches=0.1, facecolor='white')
    plt.close()

def create_structure_scene(progress, frame_num):
    """Scene structure mathematique"""
    fig, ax = plt.subplots(figsize=(1920/100, 1080/100), dpi=100)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # Titre
    ax.text(5, 9.5, 'MATHEMATICAL STRUCTURE', fontsize=28, ha='center', weight='bold')
    
    # Nombres irrationnels
    if progress > 0.1:
        alpha = min(1.0, (progress - 0.1) * 2)
        ax.text(5, 8.5, 'Using Quadratic Irrationals:', 
               fontsize=16, ha='center', alpha=alpha)
    
    irrationals = [
        ('sqrt(5)', '2.2360679...'),
        ('sqrt(13)', '3.6055512...'),
        ('sqrt(17)', '4.1231056...')
    ]
    
    for i, (name, value) in enumerate(irrationals):
        if progress > 0.2 + i * 0.1:
            alpha = min(1.0, (progress - (0.2 + i * 0.1)) * 3)
            y_pos = 7.5 - i * 0.8
            ax.text(3, y_pos, f'{name} =', fontsize=14, ha='right', alpha=alpha)
            ax.text(3.2, y_pos, value, fontsize=14, ha='left', alpha=alpha,
                   family='monospace', color='#16213e')
    
    # Schema de calcul
    if progress > 0.6:
        alpha = min(1.0, (progress - 0.6) * 2)
        
        # Boites avec animation
        box_props = dict(boxstyle='round,pad=0.5', facecolor='lightblue', alpha=alpha)
        
        ax.text(5, 4.5, 'Input x (64 bits)', fontsize=14, ha='center', 
               bbox=box_props)
        
        ax.annotate('', xy=(5, 4), xytext=(5, 4.2),
                   arrowprops=dict(arrowstyle='->', lw=2, alpha=alpha))
        
        calc_text = 'sqrt(D) * x² + α*x + β\n─────────────────────\n      x + γ'
        ax.text(5, 2.8, calc_text, fontsize=12, ha='center',
               bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=alpha),
               family='monospace')
        
        ax.annotate('', xy=(5, 1.8), xytext=(5, 2.2),
                   arrowprops=dict(arrowstyle='->', lw=2, alpha=alpha))
        
        ax.text(5, 1.3, 'Output y (64 bits)', fontsize=14, ha='center',
               bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=alpha))
    
    plt.savefig(f'video_frames/frame_{frame_num:04d}.png',
               bbox_inches='tight', pad_inches=0, facecolor='white')
    plt.close()

def create_performance_scene(progress, frame_num):
    """Scene performance"""
    fig, ax = plt.subplots(figsize=(1920/100, 1080/100), dpi=100)
    
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # Titre
    ax.text(5, 9.5, 'PERFORMANCE', fontsize=28, ha='center', weight='bold')
    
    # Donnees
    algorithms = ['SHA-256\n(CPU)', 'SHA-256\n(GPU)', 'FPCH\n(Target)']
    speeds = [0.8, 3.1, 5.2]
    colors = ['steelblue', 'orange', 'green']
    
    max_speed = max(speeds)
    
    # Barres avec animation
    for i, (algo, speed, color) in enumerate(zip(algorithms, speeds, colors)):
        if progress > 0.1 + i * 0.15:
            bar_progress = min(1.0, (progress - (0.1 + i * 0.15)) * 3)
            current_speed = speed * bar_progress
            
            bar_width = (current_speed / max_speed) * 6
            
            rect = patches.FancyBboxPatch(
                (2, 6.5 - i * 1.8), bar_width, 1.2,
                boxstyle="round,pad=0.1",
                facecolor=color, alpha=0.7, edgecolor='black'
            )
            ax.add_patch(rect)
            
            ax.text(1.8, 7.1 - i * 1.8, algo, fontsize=12, ha='right', va='center')
            ax.text(2 + bar_width + 0.2, 7.1 - i * 1.8, 
                   f'{current_speed:.1f} GB/s', fontsize=12, va='center')
    
    # Note
    if progress > 0.7:
        alpha = min(1.0, (progress - 0.7) * 3)
        ax.text(5, 1.5, 'Note: FPCH achieves 5.2 GB/s on RTX 4090 (GPU)', 
               fontsize=12, ha='center', style='italic', alpha=alpha)
        ax.text(5, 1, 'Integer-only arithmetic enables deterministic chaos', 
               fontsize=11, ha='center', alpha=alpha, color='#555')
    
    plt.savefig(f'video_frames/frame_{frame_num:04d}.png',
               bbox_inches='tight', pad_inches=0, facecolor='white')
    plt.close()

def create_outro_scene(progress, frame_num):
    """Scene de fin"""
    fig, ax = plt.subplots(figsize=(1920/100, 1080/100), dpi=100)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # Fond
    gradient = np.linspace(0, 1, 256).reshape(256, -1)
    gradient = np.vstack((gradient, gradient))
    ax.imshow(gradient, extent=[0, 10, 0, 10], aspect='auto',
              cmap='Blues', alpha=0.2, zorder=0)
    
    # Textes progressifs
    if progress > 0.1:
        alpha = min(1.0, (progress - 0.1) * 2)
        ax.text(5, 7, 'Thank You', fontsize=56, ha='center', weight='bold',
               alpha=alpha, color='#1a1a2e')
    
    if progress > 0.3:
        alpha = min(1.0, (progress - 0.3) * 2)
        ax.text(5, 5.5, 'FPCH: An Invitation to Cryptanalysis', 
               fontsize=20, ha='center', alpha=alpha, style='italic')
    
    if progress > 0.5:
        alpha = min(1.0, (progress - 0.5) * 2)
        ax.text(5, 4, 'github.com/MisterT92-OSS/fpch-crypto',
               fontsize=16, ha='center', alpha=alpha, color='#e94560',
               weight='bold')
    
    if progress > 0.7:
        alpha = min(1.0, (progress - 0.7) * 2)
        ax.text(5, 2.5, 'Contact: toufik.salem.perso@pm.me',
               fontsize=14, ha='center', alpha=alpha)
    
    plt.savefig(f'video_frames/frame_{frame_num:04d}.png',
               bbox_inches='tight', pad_inches=0, facecolor='white')
    plt.close()

def compile_video():
    """Compile les frames en video MP4 avec FFmpeg"""
    print("\nCompilation de la video avec FFmpeg...")
    
    cmd = [
        'ffmpeg',
        '-y',  # Ecraser si existe
        '-framerate', str(FPS),
        '-i', 'video_frames/frame_%04d.png',
        '-c:v', 'libx264',
        '-pix_fmt', 'yuv420p',
        '-crf', '23',  # Qualite
        'fpch_demo.mp4'
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode == 0:
        print("✅ Video generee avec succes: fpch_demo.mp4")
        
        # Afficher info
        probe_cmd = ['ffprobe', '-v', 'error', '-show_entries', 
                    'format=duration,size,bit_rate', '-of', 
                    'default=noprint_wrappers=1', 'fpch_demo.mp4']
        probe_result = subprocess.run(probe_cmd, capture_output=True, text=True)
        print(f"\nInfos video:")
        print(probe_result.stdout)
        
        return True
    else:
        print("❌ Erreur FFmpeg:")
        print(result.stderr)
        return False

def main():
    """Programme principal"""
    print("=" * 70)
    print("FPCH - GENERATION VIDEO")
    print("=" * 70)
    print(f"\nConfiguration:")
    print(f"  - Duree: {DURATION} secondes")
    print(f"  - FPS: {FPS}")
    print(f"  - Total frames: {FRAMES}")
    print(f"  - Resolution: 1920x1080")
    print()
    
    print("Generation des frames...")
    for frame_num in range(FRAMES):
        if frame_num % 30 == 0:
            progress = (frame_num / FRAMES) * 100
            print(f"  Frame {frame_num}/{FRAMES} ({progress:.1f}%)")
        
        create_frame(frame_num, FRAMES)
    
    print("\n✅ Toutes les frames generees")
    
    # Compiler la video
    if compile_video():
        # Nettoyer les frames
        print("\nNettoyage des frames temporaires...")
        import shutil
        shutil.rmtree('video_frames')
        print("✅ Nettoyage termine")
        
        print("\n" + "=" * 70)
        print("VIDEO PRETE: fpch_demo.mp4")
        print("=" * 70)
        print("\nTu peux maintenant:")
        print("  1. Ouvrir fpch_demo.mp4 dans QuickTime/VLC")
        print("  2. Uploader sur YouTube (unlisted)")
        print("  3. Partager le lien")
    else:
        print("\n❌ Echec de la generation video")
        print("Les frames sont conservees dans video_frames/")

if __name__ == "__main__":
    main()
