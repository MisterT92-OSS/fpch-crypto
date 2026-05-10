#!/usr/bin/env python3
"""
FPCH V6 - Vidéo Démo Française
Auteur: Toufik Salem
"""
import time
import os

# Couleurs ANSI
R = '\033[91m'   # Rouge
G = '\033[92m'   # Vert
B = '\033[94m'   # Bleu
Y = '\033[93m'   # Jaune
C = '\033[96m'   # Cyan
W = '\033[97m'   # Blanc
BOLD = '\033[1m'
RESET = '\033[0m'

def clear():
    os.system('clear')

def demo():
    clear()
    print(f"\n{BOLD}{C}╔══════════════════════════════════════════════════════════════╗{RESET}")
    print(f"{BOLD}{C}║      FPCH - Function of Chaotic Hyperbolic Permutation       ║{RESET}")
    print(f"{BOLD}{C}║           Invitation à la Cryptanalyse | V6                  ║{RESET}")
    print(f"{BOLD}{C}╚══════════════════════════════════════════════════════════════╝{RESET}")
    time.sleep(2)
    
    # Auteur
    print(f"\n{Y}Auteur: Toufik Salem{RESET}")
    print(f"{G}GitHub: github.com/toufiksalem/fpch-crypto{RESET}")
    time.sleep(1.5)
    
    # Introduction
    clear()
    print(f"\n{BOLD}{W}📊 OBJECTIF{RESET}")
    print(f"\nExplorer une fonction de hash basée sur:")
    print(f"  {C}•{RESET} Champs quadratiques réels (discriminants fondamentaux)")
    print(f"  {C}•{RESET} Arithmétique entière uniquement (pas de floating-point)")
    print(f"  {C}•{RESET} Structure sans groupe (résistance à Shor)")
    time.sleep(3)
    
    # Formule V5
    clear()
    print(f"\n{BOLD}{W}📐 FORMULE FPCH V5 (Papier original){RESET}")
    print(f"\n{Y}P(x) = floor( (⌊√D⌋₁₂₈ · x² >> 64 + α·x + β) / (x + γ) ) mod 2⁶⁴{RESET}")
    print(f"\n{R}⚠️  Problème: Division modulaire non-inversible{RESET}")
    print(f"{R}⚠️  Problème: 8 lanes indépendantes → sécurité 8×2⁶⁴{RESET}")
    time.sleep(3)
    
    # Améliorations V6
    clear()
    print(f"\n{BOLD}{G}🔧 AMÉLIORATIONS FPCH V6{RESET}")
    print(f"\n{G}✓ Cross-lane mixing après chaque round{RESET}")
    print(f"  {C}x[i] = x[i] ⊕ ROTL(x[(i+1)%8], 13) ⊕ ROTL(x[(i+3)%8], 29){RESET}")
    print(f"\n{G}✓ Division remplacée par multiplication + XOR{RESET}")
    print(f"  {C}y = numerator × rotl(denom, 17) ⊕ denom{RESET}")
    print(f"\n{G}✓ Non-linéarité renforcée (MurmurHash-style){RESET}")
    print(f"\n{G}✓ Constante golden ratio (0x9e3779b97f4a7c15){RESET}")
    time.sleep(4)
    
    # Avalanche comparison
    clear()
    print(f"\n{BOLD}{W}📈 COMPARAISON AVALANCHE{RESET}")
    print(f"\n{R}V5:  24/512 bits (4.7%){RESET}")
    print(f"{G}V6: 245/512 bits (47.9%){RESET}")
    print(f"\n{BOLD}{Y}→ Amélioration: 10× meilleure diffusion{RESET}")
    time.sleep(3)
    
    # Architecture
    clear()
    print(f"\n{BOLD}{W}🏗️  ARCHITECTURE FPCH V6{RESET}")
    print(f"""
{C}     ┌──────────────────────────────────────────┐{RESET}
{C}     │         Input Message M (512 bits)        │{RESET}
{C}     └─────────────────┬──────────────────────────┘{RESET}
{C}                       ▼{RESET}
{C}     ┌──────────────────────────────────────────┐{RESET}
{C}     │     Merkle-Damgård Padding (512-bit)      │{RESET}
{C}     └─────────────────┬──────────────────────────┘{RESET}
{C}                       ▼{RESET}
{Y}     ┌─────────────────────────────────────────────────────────────┐{RESET}
{Y}     │  L0  │  L1  │  L2  │  L3  │  L4  │  L5  │  L6  │  L7  │{RESET}
{Y}     │      │      │      │      │      │      │      │      │{RESET}
{Y}     │  P(x)│  P(x)│  P(x)│  P(x)│  P(x)│  P(x)│  P(x)│  P(x)│{RESET}
{Y}     │      │      │      │      │      │      │      │      │{RESET}
{Y}     └──┬───┴──┬───┴──┬───┴──┬───┴──┬───┴──┬───┴──┬───┴──┬───┘{RESET}
{G}        │      │      │      │      │      │      │      │{RESET}
{G}        ▼      ▼      ▼      ▼      ▼      ▼      ▼      ▼{RESET}
{G}     ┌─────────────────────────────────────────────────────┐{RESET}
{G}     │           CROSS-LANE MIXING (après chaque round)     │{RESET}
{G}     └─────────────────────┬───────────────────────────────┘{RESET}
{G}                           ▼{RESET}
{B}     ┌──────────────────────────────────────────┐{RESET}
{B}     │         Final XOR Mix (512 bits)          │{RESET}
{B}     └─────────────────────┬────────────────────┘{RESET}
{B}                           ▼{RESET}
{B}     ┌──────────────────────────────────────────┐{RESET}
{B}     │         Hash Output (512 bits)            │{RESET}
{B}     └──────────────────────────────────────────┘{RESET}
""")
    time.sleep(5)
    
    # Test rapide
    clear()
    print(f"\n{BOLD}{W}🧪 TEST FPCH V6{RESET}\n")
    
    try:
        from fpch_v6 import fpch_hash512_v6
        
        test_cases = [
            (b"Hello World", "Message simple"),
            (b"Hello WorlD", "1 bit différent"),
            (b"", "Message vide"),
        ]
        
        for msg, desc in test_cases:
            h = fpch_hash512_v6(msg)
            print(f"{C}{desc}:{RESET}")
            print(f"  {G}{msg!r:20}{RESET} → {Y}{h.hex()[:32]}...{RESET}\n")
            time.sleep(1)
        
        # Avalanche
        h1 = fpch_hash512_v6(b"Hello World")
        h2 = fpch_hash512_v6(b"Hello WorlD")
        xor = int.from_bytes(h1, 'big') ^ int.from_bytes(h2, 'big')
        diff = bin(xor).count('1')
        
        print(f"{BOLD}{W}📊 AVALANCHE{RESET}")
        print(f"  Bits différents: {G}{diff}/512{RESET} ({diff/512*100:.1f}%)")
        time.sleep(2)
        
    except ImportError:
        print(f"{R}⚠️  fpch_v6.py non trouvé{RESET}")
        time.sleep(2)
    
    # Invitation cryptanalyse
    clear()
    print(f"\n{BOLD}{Y}🔬 INVITATION À LA CRYPTANALYSE{RESET}")
    print(f"\n{W}Vecteurs d'attaque suggérés:{RESET}")
    print(f"  {R}•{RESET} Attaques algébriques (base de Gröbner)")
    print(f"  {R}•{RESET} Cryptanalyse différentielle")
    print(f"  {R}•{RESET} Attaques lane-wise (réduction 2⁵¹² → 8×2⁶⁴)")
    print(f"  {R}•{RESET} Clés faibles (semences produisant un comportement linéaire)")
    print(f"  {R}•{RESET} Attaques préimage")
    time.sleep(4)
    
    # Conclusion
    clear()
    print(f"\n{BOLD}{G}✅ FPCH V6{RESET}")
    print(f"\n{W}• Cross-lane diffusion ✓{RESET}")
    print(f"{W}• Division-free ✓{RESET}")
    print(f"{W}• Avalanche 47.9% ✓{RESET}")
    print(f"{W}• Arithmétique entière pure ✓{RESET}")
    print(f"\n{Y}⚠️  Toujours en recherche de validation communautaire{RESET}")
    time.sleep(3)
    
    # Contact
    clear()
    print(f"\n{BOLD}{C}╔══════════════════════════════════════════════════════════════╗{RESET}")
    print(f"{BOLD}{C}║                    CONTACT & RESSOURCES                       ║{RESET}")
    print(f"{BOLD}{C}╚══════════════════════════════════════════════════════════════╝{RESET}")
    print(f"\n{G}GitHub:   github.com/toufiksalem/fpch-crypto{RESET}")
    print(f"{G}Email:    toufik.salem.perso@pm.me{RESET}")
    print(f"{G}Papier:   FPCH_Paper.pdf (12 pages){RESET}")
    print(f"\n{Y}Venez casser FPCH ! 🛠️{RESET}\n")

if __name__ == "__main__":
    demo()