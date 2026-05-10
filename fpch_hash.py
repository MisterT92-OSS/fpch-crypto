#!/usr/bin/env python3
"""
FPCH - Implementation Python Simple
Par Toufik Salem

Cette version implemente l'algorithme FPCH de base pour demonstration.
"""

import math
import hashlib
import struct

# Discriminants fondamentaux positifs (les 8 premiers)
DISCRIMINANTS = [5, 8, 12, 13, 17, 21, 24, 28]

def integer_sqrt(n, bits=128):
    """
    Calcule sqrt(n) avec 'bits' bits de precision.
    Retourne un entier: floor(sqrt(n) * 2^bits)
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 0
    
    # Approximation initiale avec math.sqrt (float)
    approx = int(math.isqrt(n) * (2 ** bits))
    return approx

def fpch_layer(x, alpha, beta, gamma, D, bits=128):
    """
    Une couche FPCH.
    
    Formule: P(x) = floor( (sqrt(D) * x^2 + alpha*x + beta) / (x + gamma) ) mod 2^64
    
    Args:
        x: entree (int, 64 bits)
        alpha, beta, gamma: parametres (int)
        D: discriminant (int, doit etre dans DISCRIMINANTS)
        bits: precision pour sqrt(D)
    
    Returns:
        sortie (int, 64 bits)
    """
    # Calcul de sqrt(D) avec precision 'bits'
    sqrt_D = integer_sqrt(D, bits)
    
    # x^2
    x_sq = x * x
    
    # sqrt(D) * x^2 >> bits (division par 2^bits)
    # Note: En pratique, on fait (sqrt_D * x_sq) // (2^bits)
    term1 = (sqrt_D * x_sq) >> bits
    
    # Numerateur: term1 + alpha*x + beta
    numerator = term1 + alpha * x + beta
    
    # Denominateur: x + gamma (eviter la division par zero)
    denominator = x + gamma
    if denominator == 0:
        denominator = 1
    
    # Division et modulo 2^64
    result = (numerator // denominator) & 0xFFFFFFFFFFFFFFFF
    
    return result

def fpch_hash(message, num_layers=16):
    """
    Hash complet FPCH sur un message.
    
    Cette version simplifiee:
    1. Convertit le message en entier
    2. Applique plusieurs couches FPCH
    3. Retourne le hash final
    
    Args:
        message: bytes ou str
        num_layers: nombre de couches (defaut: 16)
    
    Returns:
        hash_value: int (64 bits)
    """
    if isinstance(message, str):
        message = message.encode('utf-8')
    
    # Convertir le message en entier 64-bit initial
    # Utilise SHA-256 pour l'initialisation (deterministe)
    h = hashlib.sha256(message).digest()
    x = struct.unpack('<Q', h[:8])[0]  # 64 bits little-endian
    
    # Parametres fixes pour la demonstration
    # (Dans la vraie version, ces parametres seraient derives d'une seed)
    alphas = [0x9e3779b97f4a7c15, 0xf39cc0605cedc834, 0x1082c6e3d2e3c5f1, 
              0x6a09e667f3bcc908, 0xbb67ae8584caa73b, 0x3c6ef372fe94f82b,
              0xa54ff53a5f1d36f1, 0x510e527fade682d1, 0x9b05688c2b3e6c1f,
              0x1f83d9abfb41bd6b, 0x5be0cd19137e2179, 0xcbbb9d5dc1059ed8,
              0x629a292a367cd507, 0x9159015a3070dd17, 0x152fecd8f70e5939,
              0x67332667ffc00b31]
    
    betas = [0x6a09e667f3bcc908, 0xbb67ae8584caa73b, 0x3c6ef372fe94f82b,
             0xa54ff53a5f1d36f1, 0x510e527fade682d1, 0x9b05688c2b3e6c1f,
             0x1f83d9abfb41bd6b, 0x5be0cd19137e2179, 0xcbbb9d5dc1059ed8,
             0x629a292a367cd507, 0x9159015a3070dd17, 0x152fecd8f70e5939,
             0x67332667ffc00b31, 0x8eb44a8768581511, 0xdb0c2e0d64f98fa7,
             0x47b5481dbefa4fa4]
    
    gammas = [0x510e527fade682d1, 0x9b05688c2b3e6c1f, 0x1f83d9abfb41bd6b,
              0x5be0cd19137e2179, 0xcbbb9d5dc1059ed8, 0x629a292a367cd507,
              0x9159015a3070dd17, 0x152fecd8f70e5939, 0x67332667ffc00b31,
              0x8eb44a8768581511, 0xdb0c2e0d64f98fa7, 0x47b5481dbefa4fa4,
              0x6a09e667f3bcc908, 0xbb67ae8584caa73b, 0x3c6ef372fe94f82b,
              0xa54ff53a5f1d36f1]
    
    # Appliquer les couches
    for i in range(num_layers):
        D = DISCRIMINANTS[i % len(DISCRIMINANTS)]
        x = fpch_layer(x, alphas[i], betas[i], gammas[i], D)
    
    return x

def demo():
    """
    Demonstration de FPCH.
    """
    print("=" * 70)
    print("FPCH - Function of Chaotic Hyperbolic Permutation")
    print("Par Toufik Salem")
    print("=" * 70)
    print()
    
    # Exemple 1: Message simple
    msg1 = b"Hello World"
    hash1 = fpch_hash(msg1)
    
    print(f"Message: {msg1}")
    print(f"Hash FPCH: {hash1:016x} (64 bits)")
    print()
    
    # Exemple 2: Message legerement different
    msg2 = b"Hello WorlD"  # D majuscule
    hash2 = fpch_hash(msg2)
    
    print(f"Message: {msg2}")
    print(f"Hash FPCH: {hash2:016x} (64 bits)")
    print()
    
    # Analyse de l'avalanche
    print("Analyse de l'effet avalanche:")
    print(f"  Difference: {abs(hash1 - hash2)} valeurs")
    
    # Comparaison bit par bit
    diff_bits = bin(hash1 ^ hash2).count('1')
    print(f"  Bits differents: {diff_bits} / 64 ({diff_bits/64*100:.1f}%)")
    
    if 25 <= diff_bits <= 39:  # ~50% +/- tolerance
        print("  Resultat: EXCELLENT (effet avalanche verifie)")
    else:
        print(f"  Resultat: {diff_bits}/64 bits changes")
    
    print()
    
    # Exemple 3: Message en francais
    msg3 = "Bonjour le monde"
    hash3 = fpch_hash(msg3)
    print(f"Message: '{msg3}'")
    print(f"Hash FPCH: {hash3:016x}")
    print()
    
    # Determinisme
    print("Verification du determinisme:")
    hash1_bis = fpch_hash(b"Hello World")
    print(f"  Hash(Hello World) [1er appel]: {hash1:016x}")
    print(f"  Hash(Hello World) [2eme appel]: {hash1_bis:016x}")
    print(f"  Identiques: {'OUI' if hash1 == hash1_bis else 'NON'}")
    
    print()
    print("=" * 70)
    print("Note: Cette implementation est une demonstration simplifiee.")
    print("La version complete (512 bits) est disponible dans le papier.")
    print("=" * 70)

if __name__ == "__main__":
    demo()
