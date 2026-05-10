#!/usr/bin/env python3
"""
FPCH V6 - Demo Video English
Author: Toufik Salem
"""
import time
import os

# ANSI Colors
R = '\033[91m'   # Red
G = '\033[92m'   # Green
B = '\033[94m'   # Blue
Y = '\033[93m'   # Yellow
C = '\033[96m'   # Cyan
W = '\033[97m'   # White
BOLD = '\033[1m'
RESET = '\033[0m'

def clear():
    os.system('clear')

def demo():
    clear()
    print(f"\n{BOLD}{C}╔══════════════════════════════════════════════════════════════╗{RESET}")
    print(f"{BOLD}{C}║      FPCH - Function of Chaotic Hyperbolic Permutation       ║{RESET}")
    print(f"{BOLD}{C}║              Invitation to Cryptanalysis | V6                ║{RESET}")
    print(f"{BOLD}{C}╚══════════════════════════════════════════════════════════════╝{RESET}")
    time.sleep(2)
    
    # Author
    print(f"\n{Y}Author: Toufik Salem{RESET}")
    print(f"{G}GitHub: github.com/MisterT92-OSS/fpch-crypto{RESET}")
    time.sleep(1.5)
    
    # Introduction
    clear()
    print(f"\n{BOLD}{W}📊 OBJECTIVE{RESET}")
    print(f"\nExploring a hash function based on:")
    print(f"  {C}•{RESET} Real quadratic fields (fundamental discriminants)")
    print(f"  {C}•{RESET} Integer-only arithmetic (no floating-point)")
    print(f"  {C}•{RESET} Non-group structure (Shor resistance)")
    time.sleep(3)
    
    # V5 Formula
    clear()
    print(f"\n{BOLD}{W}📐 FPCH V5 FORMULA (Original Paper){RESET}")
    print(f"\n{Y}P(x) = floor( (⌊√D⌋₁₂₈ · x² >> 64 + α·x + β) / (x + γ) ) mod 2⁶⁴{RESET}")
    print(f"\n{R}⚠️  Issue: Modular division is non-invertible{RESET}")
    print(f"{R}⚠️  Issue: 8 independent lanes → security 8×2⁶⁴{RESET}")
    time.sleep(3)
    
    # V6 Improvements
    clear()
    print(f"\n{BOLD}{G}🔧 FPCH V6 IMPROVEMENTS{RESET}")
    print(f"\n{G}✓ Cross-lane mixing after each round{RESET}")
    print(f"  {C}x[i] = x[i] ⊕ ROTL(x[(i+1)%8], 13) ⊕ ROTL(x[(i+3)%8], 29){RESET}")
    print(f"\n{G}✓ Division replaced by multiplication + XOR{RESET}")
    print(f"  {C}y = numerator × rotl(denom, 17) ⊕ denom{RESET}")
    print(f"\n{G}✓ Enhanced non-linearity (MurmurHash-style){RESET}")
    print(f"\n{G}✓ Golden ratio constant (0x9e3779b97f4a7c15){RESET}")
    time.sleep(4)
    
    # Avalanche comparison
    clear()
    print(f"\n{BOLD}{W}📈 AVALANCHE COMPARISON{RESET}")
    print(f"\n{R}V5:  24/512 bits (4.7%){RESET}")
    print(f"{G}V6: 245/512 bits (47.9%){RESET}")
    print(f"\n{BOLD}{Y}→ Improvement: 10× better diffusion{RESET}")
    time.sleep(3)
    
    # Architecture
    clear()
    print(f"\n{BOLD}{W}🏗️  FPCH V6 ARCHITECTURE{RESET}")
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
{G}     │           CROSS-LANE MIXING (after each round)      │{RESET}
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
    
    # Quick test
    clear()
    print(f"\n{BOLD}{W}🧪 FPCH V6 TEST{RESET}\n")
    
    try:
        from fpch_v6 import fpch_hash512_v6
        
        test_cases = [
            (b"Hello World", "Simple message"),
            (b"Hello WorlD", "1 bit different"),
            (b"", "Empty message"),
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
        print(f"  Different bits: {G}{diff}/512{RESET} ({diff/512*100:.1f}%)")
        time.sleep(2)
        
    except ImportError:
        print(f"{R}⚠️  fpch_v6.py not found{RESET}")
        time.sleep(2)
    
    # Cryptanalysis invitation
    clear()
    print(f"\n{BOLD}{Y}🔬 INVITATION TO CRYPTANALYSIS{RESET}")
    print(f"\n{W}Suggested attack vectors:{RESET}")
    print(f"  {R}•{RESET} Algebraic attacks (Gröbner basis)")
    print(f"  {R}•{RESET} Differential cryptanalysis")
    print(f"  {R}•{RESET} Lane-wise attacks (reduction 2⁵¹² → 8×2⁶⁴)")
    print(f"  {R}•{RESET} Weak keys (seeds producing linear behavior)")
    print(f"  {R}•{RESET} Preimage attacks")
    time.sleep(4)
    
    # Conclusion
    clear()
    print(f"\n{BOLD}{G}✅ FPCH V6{RESET}")
    print(f"\n{W}• Cross-lane diffusion ✓{RESET}")
    print(f"{W}• Division-free ✓{RESET}")
    print(f"{W}• Avalanche 47.9% ✓{RESET}")
    print(f"{W}• Pure integer arithmetic ✓{RESET}")
    print(f"\n{Y}⚠️  Still seeking community validation{RESET}")
    time.sleep(3)
    
    # Contact
    clear()
    print(f"\n{BOLD}{C}╔══════════════════════════════════════════════════════════════╗{RESET}")
    print(f"{BOLD}{C}║                    CONTACT & RESOURCES                        ║{RESET}")
    print(f"{BOLD}{C}╚══════════════════════════════════════════════════════════════╝{RESET}")
    print(f"\n{G}GitHub:   github.com/MisterT92-OSS/fpch-crypto{RESET}")
    print(f"{G}Email:    toufik.salem.perso@pm.me{RESET}")
    print(f"{G}Paper:    FPCH_Paper.pdf (12 pages){RESET}")
    print(f"\n{Y}Come break FPCH! 🛠️{RESET}\n")

if __name__ == "__main__":
    demo()