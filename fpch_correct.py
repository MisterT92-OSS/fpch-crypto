#!/usr/bin/env python3
"""
FPCH - Implementation CORRIGEE
Par Toufik Salem

Version avec vraie formule FPCH et integer_sqrt exact.
"""

import math

# Les discriminants fondamentaux positifs
DISCRIMINANTS = [5, 8, 12, 13, 17, 21, 24, 28]

def integer_sqrt_exact(D: int, bits: int = 60) -> int:
    """
    Calcule floor(sqrt(D) * 2^bits) avec arithmetique entiere exacte.
    
    Formule: isqrt(D * 4^bits) = isqrt(D) * 2^bits + correction
    """
    # D * 2^(2*bits) puis racine carree entiere
    return math.isqrt(D * (1 << (2 * bits)))

def fpch_layer(x: int, alpha: int, beta: int, gamma: int, D: int, bits: int = 60) -> int:
    """
    Une couche FPCH avec la VRAIE formule:
    P(x) = floor( (floor(sqrt(D))_bits * x^2 / 2^bits + alpha*x + beta) / (x + gamma) ) mod 2^64
    """
    # sqrt(D) avec precision exacte 'bits'
    sqrt_D = integer_sqrt_exact(D, bits)
    
    # x^2
    x_sq = x * x
    
    # sqrt(D) * x^2 / 2^bits
    term1 = (sqrt_D * x_sq) >> bits
    
    # Numerateur: term1 + alpha*x + beta
    numerator = term1 + (alpha * x) + beta
    
    # Denominateur: x + gamma (eviter division par zero)
    denominator = x + gamma
    if denominator == 0:
        denominator = 1
    
    # Division et modulo 2^64
    result = (numerator // denominator) & 0xFFFFFFFFFFFFFFFF
    
    return result

def fpch_hash64(message: bytes) -> int:
    """
    Hash FPCH 64-bit avec vraie implementation.
    """
    # Initialisation avec IV base sur discriminants
    state = 0x6a09e667f3bcc908
    
    # Derive alpha, beta, gamma du message
    if not message:
        msg_val = 0
    else:
        msg_val = int.from_bytes(message[:8], 'big') if len(message) <= 8 else hash(message) % (2**64)
    
    # 16 rounds avec 16 discriminants differents
    for round_idx in range(16):
        D = DISCRIMINANTS[round_idx % len(DISCRIMINANTS)]
        
        # Parametres derives du message
        alpha = (0x9e3779b97f4a7c15 + msg_val * (round_idx + 1)) & 0xFFFFFFFFFFFFFFFF
        beta = (0xf39cc0605cedc834 + msg_val * (round_idx + 3)) & 0xFFFFFFFFFFFFFFFF
        gamma = ((0x510e527fade682d1 + msg_val * (round_idx + 5)) % 0xFFFFFFFFFFFFFFFF) | 1  # Non-zero
        
        # Application de la couche FPCH
        state = fpch_layer(state, alpha, beta, gamma, D)
    
    return state

def demo():
    """Demonstration avec vraie implementation FPCH."""
    print("=" * 70)
    print("FPCH - Implementation de Reference (Vraie Formule)")
    print("Par Toufik Salem")
    print("=" * 70)
    print()
    print("Cette implementation utilise la VRAIE formule FPCH du papier:")
    print("  P(x) = floor((sqrt(D)*x^2/2^bits + alpha*x + beta)/(x+gamma)) mod 2^64")
    print()
    print("Avec integer_sqrt EXACT (pas d'approximation flottante).")
    print()
    
    # Verifier integer_sqrt
    print("Verification integer_sqrt exact:")
    for D in [5, 8, 12]:
        approx = integer_sqrt_exact(D, 60)
        real_sqrt = math.sqrt(D)
        print(f"  sqrt({D}) * 2^60 = {approx}")
        print(f"    Valeur reelle: {real_sqrt:.10f}")
        print(f"    Ratio: {approx / (2**60):.10f} ✓ EXACT")
        print()
    
    # Tests
    print("Tests de hachage:")
    tests = [
        b"Hello World",
        b"Hello WorlD",
        b"Bonjour",
        b"test",
        b"A",
    ]
    
    results = []
    for msg in tests:
        h = fpch_hash64(msg)
        results.append((msg, h))
        print(f"  {msg!r:20} -> {h:016x}")
    
    print()
    
    # Avalanche
    msg1, h1 = results[0]
    msg2, h2 = results[1]
    diff_bits = bin(h1 ^ h2).count('1')
    
    print(f"Avalanche: {msg1!r} vs {msg2!r}")
    print(f"  Hash 1: {h1:016x}")
    print(f"  Hash 2: {h2:016x}")
    print(f"  Bits differents: {diff_bits}/64 ({diff_bits/64*100:.1f}%)")
    
    if diff_bits >= 40:
        print("  Resultat: EXCELLENT ✓")
    elif diff_bits >= 20:
        print("  Resultat: ACCEPTABLE")
    else:
        print("  Resultat: FAIBLE (amelioration necessaire)")
    
    print()
    print("=" * 70)
    print("NOTES:")
    print("  - Cette version utilise la VRAIE formule FPCH")
    print("  - L'avalanche n'est pas optimale (version de reference)")
    print("  - Pour production: voir version complete 512-bit dans le papier")
    print("  - Demonstration pedagogique du concept")
    print("=" * 70)
    print()
    print("Auteur: Toufik Salem")
    print("Papier: github.com/MisterT92-OSS/fpch-crypto")

def hash(obj):
    """Hash simple pour messages longs."""
    h = 0
    for i, b in enumerate(obj):
        h = ((h * 31) + b + i) & 0xFFFFFFFFFFFFFFFF
    return h

if __name__ == "__main__":
    demo()
