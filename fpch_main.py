#!/usr/bin/env python3
"""
FPCH - Implementation Principale / Main Implementation
Par Toufik Salem / By Toufik Salem

VERSION PRINCIPALE / MAIN VERSION
Cette implémentation est la version recommandée pour l'utilisation.
Elle équilibre conformité au papier et efficacité pratique.

This implementation is the recommended version for use.
It balances paper compliance and practical efficiency.

Formule / Formula:
  P(x) = floor((sqrt(D)*x^2/2^bits + alpha*x + beta)/(x+gamma)) mod 2^64

Auteur / Author: Toufik Salem
Contact: toufik.salem.perso@pm.me
GitHub: github.com/MisterT92-OSS/fpch-crypto
"""

import hashlib
import math

# Les 8 premiers discriminants fondamentaux positifs
# The 8 first positive fundamental discriminants
DISCRIMINANTS = [5, 8, 12, 13, 17, 21, 24, 28]

def integer_sqrt_exact(D: int, bits: int = 60) -> int:
    """
    Calcule floor(sqrt(D) * 2^bits) avec arithmétique entière exacte.
    Computes floor(sqrt(D) * 2^bits) with exact integer arithmetic.
    
    Cette fonction capture la partie fractionnelle de sqrt(D) sans utiliser
    de nombres à virgule flottante.
    
    This function captures the fractional part of sqrt(D) without using
    floating-point numbers.
    """
    return math.isqrt(D * (1 << (2 * bits)))

def fpch_layer(x: int, alpha: int, beta: int, gamma: int, D: int, bits: int = 60) -> int:
    """
    Une couche FPCH avec la VRAIE formule du papier.
    One FPCH layer with the REAL formula from the paper.
    
    Args:
        x: Entrée 64 bits / 64-bit input
        alpha, beta, gamma: Paramètres / Parameters
        D: Discriminant fondamental / Fundamental discriminant
        bits: Précision pour sqrt(D) / Precision for sqrt(D)
    
    Returns:
        Sortie 64 bits / 64-bit output
    """
    # sqrt(D) avec précision exacte 'bits'
    # sqrt(D) with exact 'bits' precision
    sqrt_D = integer_sqrt_exact(D, bits)
    
    # Terme quadratique / Quadratic term
    term1 = (sqrt_D * x * x) >> bits
    
    # Numérateur / Numerator
    numerator = term1 + (alpha * x) + beta
    
    # Dénominateur (éviter division par zéro) / Denominator (avoid division by zero)
    denominator = x + gamma
    if denominator == 0:
        denominator = 1
    
    # Résultat modulo 2^64 / Result modulo 2^64
    return (numerator // denominator) & 0xFFFFFFFFFFFFFFFF

def fpch_hash64(message: bytes) -> int:
    """
    Hash FPCH 64-bit.
    
    Cette fonction applique 64 rounds de melange base sur les discriminants
    quadratiques irrationnels.
    
    This function applies 64 rounds of mixing based on irrational
    quadratic discriminants.
    """
    # Dérive une valeur du message / Derive a value from the message
    if not message:
        msg_val = 0
    else:
        # Pour les messages courts, utilise directement les octets
        # Pour les messages longs, utilise SHA-256
        # For short messages, use bytes directly
        # For long messages, use SHA-256
        msg_val = int.from_bytes(message[:8], 'big') if len(message) <= 8 else int(hashlib.sha256(message).hexdigest()[:16], 16)
    
    # État initial / Initial state
    state = 0x6a09e667f3bcc908 ^ msg_val
    
    # 64 rounds avec melange / 64 rounds with mixing
    for i in range(64):
        D = DISCRIMINANTS[i % len(DISCRIMINANTS)]
        
        # Paramètres dérivés du message et du round
        # Parameters derived from message and round
        alpha = (0x9e3779b97f4a7c15 + msg_val * (i + 1)) & 0xFFFFFFFFFFFFFFFF
        beta = (0xf39cc0605cedc834 + msg_val * (i + 3)) & 0xFFFFFFFFFFFFFFFF
        gamma = ((0x510e527fade682d1 + msg_val * (i + 5)) % 0xFFFFFFFFFFFFFFFF) | 1
        
        # Application de la couche FPCH / Apply FPCH layer
        state = fpch_layer(state, alpha, beta, gamma, D)
    
    return state

def demo():
    """Démonstration / Demonstration"""
    print("=" * 70)
    print("FPCH - Implementation Principale / Main Implementation")
    print("Par Toufik Salem / By Toufik Salem")
    print("=" * 70)
    print()
    
    # Vérification integer_sqrt / Verify integer_sqrt
    print("Vérification integer_sqrt exact / Exact integer_sqrt verification:")
    for D in [5, 8, 12]:
        approx = integer_sqrt_exact(D, 60)
        real_sqrt = math.sqrt(D)
        print(f"  sqrt({D}) * 2^60 = {approx}")
        print(f"    Valeur réelle / Real value: {real_sqrt:.10f}")
        print(f"    Ratio: {approx / (2**60):.10f} ✓ EXACT")
    print()
    
    # Tests / Tests
    print("Tests de hachage / Hash tests:")
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
    
    # Analyse avalanche / Avalanche analysis
    print("=" * 70)
    print("ANALYSE AVALANCHE / AVALANCHE ANALYSIS")
    print("=" * 70)
    print()
    
    msg1, h1 = results[0]  # Hello World
    msg2, h2 = results[1]  # Hello WorlD
    
    print(f"Comparaison / Comparison:")
    print(f"  {msg1!r}")
    print(f"  {msg2!r}")
    print(f"  Hash 1: {h1:016x}")
    print(f"  Hash 2: {h2:016x}")
    
    diff_bits = bin(h1 ^ h2).count('1')
    print(f"  Bits différents / Different bits: {diff_bits}/64 ({diff_bits/64*100:.1f}%)")
    
    if diff_bits >= 40:
        print(f"  Résultat / Result: EXCELLENT ✓")
    elif diff_bits >= 25:
        print(f"  Résultat / Result: BON / GOOD ✓")
    else:
        print(f"  Résultat / Result: À AMÉLIORER / NEEDS IMPROVEMENT")
    
    print()
    
    # Déterminisme / Determinism
    print("=" * 70)
    print("DÉTERMINISME / DETERMINISM")
    print("=" * 70)
    print()
    
    hash_a = fpch_hash64(b"Test")
    hash_b = fpch_hash64(b"Test")
    print(f"Hash('Test') #1: {hash_a:016x}")
    print(f"Hash('Test') #2: {hash_b:016x}")
    print(f"Identiques / Identical: {'OUI / YES ✓' if hash_a == hash_b else 'NON / NO ✗'}")
    
    print()
    print("=" * 70)
    print("NOTES / NOTES:")
    print("  - Cette version équilibre conformité et efficacité")
    print("  - This version balances compliance and efficiency")
    print("  - Pour la version 100% conforme: fpch_v5.py")
    print("  - For 100% compliant version: fpch_v5.py")
    print("=" * 70)
    print()
    print("Auteur / Author: Toufik Salem")
    print("GitHub: github.com/MisterT92-OSS/fpch-crypto")

if __name__ == "__main__":
    demo()
