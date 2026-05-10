#!/usr/bin/env python3
"""
Create FPCH V6 animated demo video with visualizations
Uses matplotlib for charts and Pillow for text animation
"""
from PIL import Image, ImageDraw, ImageFont
import subprocess
import os
import tempfile
import shutil
import math

def create_frame(width=1920, height=1080, bg_color=(26, 26, 46)):
    """Create a blank frame"""
    return Image.new('RGB', (width, height), bg_color)

def draw_centered_text(draw, text, y_offset, font, color=(255, 255, 255), width=1920):
    """Draw centered text"""
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    x = (width - text_width) // 2
    draw.text((x, y_offset), text, fill=color, font=font)

def draw_title_card(title, subtitle=""):
    """Create a title card with gradient-like effect"""
    img = create_frame()
    draw = ImageDraw.Draw(img)
    
    try:
        font_title = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 80)
        font_sub = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 40)
    except:
        font_title = ImageFont.load_default()
        font_sub = ImageFont.load_default()
    
    # Draw decorative lines
    draw.rectangle([(100, 200), (1820, 205)], fill=(0, 102, 204))
    draw.rectangle([(100, 875), (1820, 880)], fill=(0, 102, 204))
    
    # Draw title
    draw_centered_text(draw, title, 400, font_title, (255, 255, 255))
    
    # Draw subtitle
    if subtitle:
        draw_centered_text(draw, subtitle, 500, font_sub, (102, 178, 255))
    
    return img

def draw_architecture_frame(step=0):
    """Draw animated architecture diagram"""
    img = create_frame()
    draw = ImageDraw.Draw(img)
    
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 32)
        font_small = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 24)
    except:
        font = ImageFont.load_default()
        font_small = ImageFont.load_default()
    
    # Title
    draw_centered_text(draw, "FPCH V6 Architecture", 50, font, (255, 255, 255))
    
    # Animation progress
    progress = min(step / 24, 1.0)  # 24 frames for animation
    
    # Draw boxes with animation
    box_height = 60
    box_width = 200
    
    # Input box
    if step >= 2:
        draw.rectangle([(860, 150), (1060, 210)], outline=(0, 255, 128), width=3)
        draw_centered_text(draw, "Input M", 160, font_small, (0, 255, 128))
    
    # Padding
    if step >= 4:
        draw.rectangle([(810, 250), (1110, 310)], outline=(255, 200, 0), width=3)
        draw_centered_text(draw, "Padding", 260, font_small, (255, 200, 0))
    
    # 8 Lanes
    lane_y = 350
    lane_names = ["L0", "L1", "L2", "L3", "L4", "L5", "L6", "L7"]
    colors = [(255, 100, 100), (100, 255, 100), (100, 100, 255), 
              (255, 255, 100), (255, 100, 255), (100, 255, 255),
              (255, 200, 100), (200, 100, 255)]
    
    for i, (name, color) in enumerate(zip(lane_names, colors)):
        if step >= 6 + i * 2:
            x = 160 + i * 200
            draw.rectangle([(x, lane_y), (x + 180, lane_y + 60)], outline=color, width=2)
            draw.text((x + 70, lane_y + 15), name, fill=color, font=font_small)
    
    # Permutation boxes
    for i in range(8):
        if step >= 20 + i:
            x = 160 + i * 200
            draw.rectangle([(x, lane_y + 80), (x + 180, lane_y + 140)], outline=(0, 200, 255), width=2)
            draw.text((x + 50, lane_y + 95), "P(x)", fill=(0, 200, 255), font=font_small)
    
    # Cross-lane mixing
    if step >= 30:
        draw.rectangle([(360, 530), (1560, 590)], outline=(0, 255, 0), width=3)
        draw_centered_text(draw, "Cross-Lane Mixing: xi ⊕ ROTL(xi+1, 13) ⊕ ROTL(xi+3, 29)", 540, font_small, (0, 255, 0))
    
    # XOR Mix
    if step >= 35:
        draw.rectangle([(760, 630), (1160, 690)], outline=(255, 0, 128), width=3)
        draw_centered_text(draw, "XOR Mix", 640, font_small, (255, 0, 128))
    
    # Output
    if step >= 40:
        draw.rectangle([(860, 730), (1060, 790)], outline=(0, 255, 255), width=3)
        draw_centered_text(draw, "Hash 512", 740, font_small, (0, 255, 255))
    
    # Draw arrows
    arrow_color = (128, 128, 128)
    if step >= 3:
        draw.line([(960, 210), (960, 250)], fill=arrow_color, width=2)
        draw.polygon([(955, 250), (965, 250), (960, 260)], fill=arrow_color)
    
    return img

def draw_avalanche_chart(v5_val=4.7, v6_val=47.9, step=0):
    """Draw avalanche comparison chart"""
    img = create_frame()
    draw = ImageDraw.Draw(img)
    
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 48)
        font_small = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 32)
    except:
        font = ImageFont.load_default()
        font_small = ImageFont.load_default()
    
    # Title
    draw_centered_text(draw, "Avalanche Effect Comparison", 50, font, (255, 255, 255))
    
    # Chart area
    chart_x = 300
    chart_y = 200
    chart_width = 1320
    chart_height = 500
    
    # Draw chart background
    draw.rectangle([(chart_x, chart_y), (chart_x + chart_width, chart_y + chart_height)], 
                   outline=(100, 100, 100), width=2)
    
    # Draw grid lines
    for i in range(6):
        y = chart_y + chart_height - i * chart_height // 5
        draw.line([(chart_x, y), (chart_x + chart_width, y)], fill=(60, 60, 80), width=1)
        # Labels
        draw.text((chart_x - 50, y - 15), f"{i * 20}%", fill=(150, 150, 150), font=font_small)
    
    # Animate bars
    bar_width = 200
    v5_height = int(v5_val / 100 * chart_height * min(step / 30, 1.0))
    v6_height = int(v6_val / 100 * chart_height * min(step / 30, 1.0))
    
    # V5 bar
    v5_x = chart_x + 200
    v5_color = (255, 100, 100)
    if v5_height > 0:
        draw.rectangle([(v5_x, chart_y + chart_height - v5_height), 
                        (v5_x + bar_width, chart_y + chart_height)], 
                       fill=v5_color, outline=(255, 150, 150), width=2)
    draw_centered_text(draw, "V5", chart_y + chart_height + 30, font_small, v5_color, 1920)
    draw.text((v5_x + 50, chart_y + chart_height - v5_height - 50), f"{v5_val}%", fill=v5_color, font=font)
    
    # V6 bar
    v6_x = chart_x + 700
    v6_color = (0, 255, 128)
    if v6_height > 0:
        draw.rectangle([(v6_x, chart_y + chart_height - v6_height), 
                        (v6_x + bar_width, chart_y + chart_height)], 
                       fill=v6_color, outline=(100, 255, 180), width=2)
    draw_centered_text(draw, "V6", chart_y + chart_height + 30, font_small, v6_color, 1920)
    if v6_height > 30:
        draw.text((v6_x + 50, chart_y + chart_height - v6_height - 50), f"{v6_val}%", fill=v6_color, font=font)
    
    # Improvement text
    if step >= 35:
        draw_centered_text(draw, "10× Improvement!", 850, font, (255, 255, 0))
    
    return img

def draw_formula_frame(formula_text, explanation=""):
    """Draw a formula with explanation"""
    img = create_frame()
    draw = ImageDraw.Draw(img)
    
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 40)
        font_formula = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 36)
    except:
        font = ImageFont.load_default()
        font_formula = ImageFont.load_default()
    
    # Draw formula box
    draw.rectangle([(100, 350), (1820, 550)], outline=(0, 102, 204), width=3)
    draw_centered_text(draw, formula_text, 420, font_formula, (102, 178, 255))
    
    if explanation:
        draw_centered_text(draw, explanation, 600, font, (200, 200, 200))
    
    return img

def create_video():
    """Create animated video"""
    tmpdir = tempfile.mkdtemp()
    fps = 24
    
    frame_idx = 0
    
    # Scene 1: Title
    for i in range(96):  # 4 seconds
        img = draw_title_card("FPCH V6", "Fonction de Permutation Hyperbolique Chaotique")
        img.save(os.path.join(tmpdir, f"frame_{frame_idx:05d}.png"))
        frame_idx += 1
    
    # Scene 2: Architecture animation (60 frames = 2.5 sec)
    for i in range(60):
        img = draw_architecture_frame(i)
        img.save(os.path.join(tmpdir, f"frame_{frame_idx:05d}.png"))
        frame_idx += 1
    
    # Scene 3: V5 Formula
    for i in range(72):  # 3 seconds
        img = draw_formula_frame(
            "P(x) = floor( (√D · x² + αx + β) / (x + γ) ) mod 2⁶⁴",
            "V5: Permutation basee sur la division"
        )
        img.save(os.path.join(tmpdir, f"frame_{frame_idx:05d}.png"))
        frame_idx += 1
    
    # Scene 4: V6 Improvements
    improvements = [
        ("Cross-Lane Mixing", "x[i] ⊕ ROTL(x[i+1], 13) ⊕ ROTL(x[i+3], 29)"),
        ("Sans Division", "y = numerator × rotl(denom, 17) ⊕ denom"),
        ("Non-linearite", "Mix style MurmurHash"),
    ]
    for title, formula in improvements:
        for i in range(60):  # 2.5 sec each
            img = draw_formula_frame(formula, title)
            img.save(os.path.join(tmpdir, f"frame_{frame_idx:05d}.png"))
            frame_idx += 1
    
    # Scene 5: Avalanche chart animation
    for i in range(48):  # 2 seconds
        img = draw_avalanche_chart(step=i)
        img.save(os.path.join(tmpdir, f"frame_{frame_idx:05d}.png"))
        frame_idx += 1
    
    # Hold final avalanche
    for i in range(48):
        img = draw_avalanche_chart(step=50)
        img.save(os.path.join(tmpdir, f"frame_{frame_idx:05d}.png"))
        frame_idx += 1
    
    # Scene 6: Cryptanalysis invitation
    attacks = [
        "Attaques Algebriques (base de Groebner)",
        "Cryptanalyse Differentielle",
        "Attaques Lane-wise",
        "Analyse des Cles Faibles",
        "Attaques Preimage"
    ]
    for attack in attacks:
        for i in range(36):  # 1.5 sec each
            img = create_frame()
            draw = ImageDraw.Draw(img)
            try:
                font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 48)
            except:
                font = ImageFont.load_default()
            draw_centered_text(draw, "Invitation a la Cryptanalyse", 200, font, (255, 200, 0))
            draw_centered_text(draw, attack, 400, font, (102, 178, 255))
            img.save(os.path.join(tmpdir, f"frame_{frame_idx:05d}.png"))
            frame_idx += 1
    
    # Scene 7: Contact
    for i in range(96):  # 4 seconds
        img = draw_title_card("github.com/MisterT92-OSS/fpch-crypto", "toufik.salem.perso@pm.me")
        img.save(os.path.join(tmpdir, f"frame_{frame_idx:05d}.png"))
        frame_idx += 1
    
    # Create video
    output = "fpch_v6_animated_fr.mp4"
    cmd = [
        'ffmpeg', '-y', '-framerate', str(fps),
        '-i', os.path.join(tmpdir, 'frame_%05d.png'),
        '-c:v', 'libx264', '-pix_fmt', 'yuv420p',
        '-crf', '20',
        output
    ]
    subprocess.run(cmd, capture_output=True)
    
    print(f"✅ Animated video created: {output}")
    
    # Cleanup
    shutil.rmtree(tmpdir, ignore_errors=True)

if __name__ == "__main__":
    create_video()