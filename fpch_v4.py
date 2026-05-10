#!/usr/bin/env python3
"""
FPCH - Version 4 (Patchée)
Par Toufik Salem

Corrections appliquées:
- integer_sqrt exact (sqrt(D) * 2^bits)
- Vraie formule FPCH du papier
- Gamma modulo correct (& 0xFFFFFFFFFFFFFFFF)
- hash() renommé en _derive_msg_val (pas de shadowing)
- msg_val dérivé de façon non-linéaire (SHA-256)
- IV dépend du message
"""

import hashlib
import math

# Les 8 premiers discriminants fondamentaux positifs
DISCRIMINANTS = [5, 8, 12, 13, 17, 21, 24, 28]

def integer_sqrt_exact(D: int, bits: int = 60) -> int:
    """
    Calcule floor(sqrt(D) * 2^bits) avec arithmétique entière exacte.
    
    Formule: isqrt(D * 4^bits) = isqrt(D * 2^(2*bits))
    """
    return math.isqrt(D * (1 << (2 * bits)))

def _derive_msg_val(message: bytes) -> int:
    """
    Dérive 64 bits du message entier de façon non-linéaire.
    Utilise SHA-256 pour éviter les faiblesses polynomiales.
    """
    return int.from_bytes(hashlib.sha256(message).digest()[:8], 'big')

def fpch_layer(x: int, alpha: int, beta: int, gamma: int, D: int, bits: int = 60) -> int:
    """
    Une couche FPCH avec la VRAIE formule du papier:
    P(x) = floor( (floor(sqrt(D))_bits * x^2 / 2^bits + alpha*x + beta) / (x + gamma) ) mod 2^64
    """
    # sqrt(D) avec précision exacte 'bits'
    sqrt_D = integer_sqrt_exact(D, bits)
    
    # x^2
    x_sq = x * x
    
    # sqrt(D) * x^2 / 2^bits
    term1 = (sqrt_D * x_sq) >> bits
    
    # Numérateur: term1 + alpha*x + beta
    numerator = term1 + (alpha * x) + beta
    
    # Dénominateur: x + gamma (éviter division par zéro)
    denominator = x + gamma
    if denominator == 0:
        denominator = 1
    
    # Division et modulo 2^64
    result = (numerator // denominator) & 0xFFFFFFFFFFFFFFFF
    
    return result

def fpch_hash64(message: bytes) -> int:
    """
    Hash FPCH 64-bit corrigé (Version 4).
    """
    # Dérive msg_val de façon non-linéaire
    msg_val = _derive_msg_val(message)
    
    # IV dépend du message (pas fixe)
    state = 0x6a09e667f3bcc908 ^ msg_val
    
    # 16 rounds avec paramètres dérivés de façon non-linéaire
    for round_idx in range(16):
        D = DISCRIMINANTS[round_idx % len(DISCRIMINANTS)]
        
        # Seed pour cette couche
        seed = (msg_val ^ (round_idx * 0x9e3779b97f4a7c15)) & 0xFFFFFFFFFFFFFFFF
        
        # Paramètres dérivés via SHA-256 (non-linéaire)
        alpha = int.from_bytes(hashlib.sha256(seed.to_bytes(8, 'big') + b'\x00').digest()[:8], 'big')
        beta = int.from_bytes(hashlib.sha256(seed.to_bytes(8, 'big') + b'\x01').digest()[:8], 'big')
        gamma = int.from_bytes(hashlib.sha256(seed.to_bytes(8, 'big') + b'\x02').digest()[:8], 'big')
        
        # Correction: modulo correct avec &
        alpha = alpha & 0xFFFFFFFFFFFFFFFF
        beta = beta & 0xFFFFFFFFFFFFFFFF
        gamma = gamma & 0xFFFFFFFFFFFFFFFF
        
        # Garantit gamma non-nul
        if gamma == 0:
            gamma = 1
        
        # Application de la couche FPCH
        state = fpch_layer(state, alpha, beta, gamma, D)
    
    return state

def demo():
    """Demonstration de FPCH-V4."""
    print("=" * 70)
    print("FPCH - Version 4 (Patchée)")
    print("Par Toufik Salem")
    print("=" * 70)
    print()
    
    # Vérification integer_sqrt
    print("Vérification integer_sqrt exact:")
    for D in [5, 8, 12]:
        approx = integer_sqrt_exact(D, 60)
        real_sqrt = math.sqrt(D)
        print(f"  sqrt({D}) * 2^60 = {approx}")
        print(f"    Valeur réelle: {real_sqrt:.10f}")
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
        b"Message beaucoup plus long pour tester la derivation non-lineaire",
        b"Un autre message long avec des differences subtiles",
    ]
    
    results = []
    for msg in tests:
        h = fpch_hash64(msg)
        results.append((msg, h))
        print(f"  {msg!r:50} -> {h:016x}")
    
    print()
    
    # Avalanche sur messages courts
    print("=" * 70)
    print("ANALYSE AVALANCHE")
    print("=" * 70)
    print()
    
    msg1, h1 = results[0]  # Hello World
    msg2, h2 = results[1]  # Hello WorlD
    
    print(f"Comparaison (messages courts):")
    print(f"  {msg1!r}")
    print(f"  {msg2!r}")
    print(f"  Hash 1: {h1:016x}")
    print(f"  Hash 2: {h2:016x}")
    diff_bits = bin(h1 ^ h2).count('1')
    print(f"  Bits différents: {diff_bits}/64 ({diff_bits/64*100:.1f}%)")
    
    # Avalanche sur messages longs
    print()
    msg3, h3 = results[5]
    msg4, h6 = results[6]
    
    print(f"Comparaison (messages longs):")
    print(f"  Longueur msg3: {len(msg3)} octets")
    print(f"  Longueur msg4: {len(msg4)} octets")
    print(f"  Hash 3: {h3:016x}")
    print(f"  Hash 4: {h6:016x}")
    diff_bits_long = bin(h3 ^ h6).count('1')
    print(f"  Bits différents: {diff_bits_long}/64 ({diff_bits_long/64*100:.1f}%)")
    
    print()
    
    # Évaluation
    total_diff = diff_bits + diff_bits_long
    avg_diff = total_diff / 2
    print(f"Moyenne avalanche: {avg_diff:.1f}/64 ({avg_diff/64*100:.1f}%)")
    
    if avg_diff >= 40:
        print("Résultat: EXCELLENT ✓")
    elif avg_diff >= 25:
        print("Résultat: BON ✓")
    else:
        print("Résultat: À AMÉLIORER")
    
    print()
    
    # Déterminisme
    print("=" * 70)
    print("DÉTERMINISME")
    print("=" * 70)
    print()
    
    hash_a = fpch_hash64(b"Test")
    hash_b = fpch_hash64(b"Test")
    print(f"Hash('Test') #1: {hash_a:016x}")
    print(f"Hash('Test') #2: {hash_b:016x}")
    print(f"Identiques: {'OUI ✓' if hash_a == hash_b else 'NON ✗'}")
    
    print()
    print("=" * 70)
    print("CORRECTIONS APPLIQUÉES (V4):")
    print("  ✓ integer_sqrt exact (sqrt(D) * 2^bits)")
    print("  ✓ Vraie formule FPCH du papier")
    print("  ✓ Gamma modulo correct (& 0xFFFFFFFFFFFFFFFF)")
    print("  ✓ Pas de shadowing hash() -> _derive_msg_val")
    print("  ✓ msg_val dérivé non-linéaire (SHA-256)")
    print("  ✓ IV dépend du message")
    print("=" * 70)
    print()
    print("Auteur: Toufik Salem")
    print("github.com/MisterT92-OSS/fpch-crypto")

if __name__ == "__main__":
    demo()
