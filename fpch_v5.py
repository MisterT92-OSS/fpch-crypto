#!/usr/bin/env python3
"""
FPCH V5 - Conforme au FPCH 
Toufik Salem
"""
import math
import hashlib
import hmac
import struct

# Appendice A : les 64 premiers discriminants fondamentaux positifs
D_PLUS_64 = [
 5, 8, 12, 13, 17, 21, 24, 28,
 29, 33, 37, 40, 41, 44, 53, 56,
 57, 60, 61, 65, 69, 73, 76, 77,
 85, 88, 89, 92, 93, 97,101,102,
 104,105,109,113,116,117,120,124,
 129,133,136,137,140,141,145,149,
 152,156,157,161,165,168,172,173,
 177,181,184,185,188,193,197,201,
]

# ── IV : partie fractionnelle de √D pour D ∈ {5,8,12,13,17,21,24,28} ─────────
def _frac_sqrt_bits64(D: int) -> int:
    """floor(2^64 × {√D}) = floor(√D × 2^64) mod 2^64"""
    full = math.isqrt(D * (1 << 128)) # floor(√D × 2^64) exact
    return full & 0xFFFFFFFFFFFFFFFF # partie fractionnelle × 2^64

IV = [_frac_sqrt_bits64(D) for D in [5, 8, 12, 13, 17, 21, 24, 28]]

# ── integer_sqrt conforme : 128 bits, shift 64 ────────────────────────────────
def integer_sqrt_exact(D: int, bits: int = 128) -> int:
    """floor(√D × 2^bits) — arithmétique entière exacte."""
    return math.isqrt(D * (1 << (2 * bits)))

# ── HKDF minimal (RFC 5869) ───────────────────────────────────────────────────
def _hkdf_extract(salt: bytes, ikm: bytes) -> bytes:
    return hmac.new(salt, ikm, hashlib.sha256).digest()

def _hkdf_expand(prk: bytes, info: bytes, length: int) -> bytes:
    okm, t, i = b'', b'', 1
    while len(okm) < length:
        t = hmac.new(prk, t + info + bytes([i]), hashlib.sha256).digest()
        okm += t
        i += 1
    return okm[:length]

# ── Génération des paramètres via HKDF (Déf. 3.2) ────────────────────────────
def derive_params(master_seed: bytes):
    """
    Dérive (αᵢ, βᵢ, γᵢ, Dᵢ) pour i=1..16 depuis master_seed.
    Conforme à la Définition 3.2 du papier.
    """
    prk = _hkdf_extract(master_seed, b"FPCH-v1.0-cryptanalysis")
    km = _hkdf_expand(prk, b"fpch-params", 512) # 512 bytes = 16 × 32

    params = []
    for i in range(16):
        base = 32 * i
        alpha = int.from_bytes(km[base:base+8], 'big') & 0xFFFFFFFFFFFFFFFF
        beta = int.from_bytes(km[base+8:base+16], 'big') & 0xFFFFFFFFFFFFFFFF
        gamma_raw = int.from_bytes(km[base+16:base+24], 'big') % (2**64 - 1)
        gamma = 1 + gamma_raw # garantit γ ≥ 1
        d_idx = int.from_bytes(km[base+24:base+32], 'big') % 64
        D = D_PLUS_64[d_idx]
        params.append((alpha, beta, gamma, D))
    return params

# ── Couche FPCH (Algorithm 1, bits=128, shift=64) ────────────────────────────
def fpch_layer(x: int, alpha: int, beta: int, gamma: int, D: int) -> int:
    """
    P(x) = floor( (⌊√D⌋₁₂₈ · x² >> 64 + α·x + β) / (x + γ) ) mod 2^64
    Conforme à la Définition 3.1 et Algorithm 1.
    """
    sqrt_D = integer_sqrt_exact(D, 128) # 128 bits, conforme au papier
    term1 = (sqrt_D * x * x) >> 64 # shift 64, conforme au papier
    numerator = term1 + alpha * x + beta
    denominator = x + gamma
    if denominator == 0:
        denominator = 1
    return (numerator // denominator) & 0xFFFFFFFFFFFFFFFF

# ── Padding Merkle-Damgård (Déf. 3.3) ────────────────────────────────────────
def _pad(message: bytes) -> bytes:
    """M ∥ 0x80 ∥ 0^k ∥ |M|₁₂₈ (blocs de 512 bits = 64 bytes)"""
    msg_len_bits = len(message) * 8
    padded = message + b'\x80'
    # Zéros jusqu'à ce qu'il reste 16 bytes dans le dernier bloc
    while (len(padded) % 64) != 48:
        padded += b'\x00'
    padded += msg_len_bits.to_bytes(16, 'big')
    assert len(padded) % 64 == 0
    return padded

# ── Fonction de compression (8 lanes × 64 bits) ──────────────────────────────
def _compress(state: list, block: bytes, params: list) -> list:
    """
    state : liste de 8 entiers 64 bits (les 8 lanes)
    block : 64 bytes (512 bits)
    params: liste de 16 tuples (α,β,γ,D)
    """
    # Absorption du bloc : XOR lane par lane (8 × 64 bits)
    lanes = [int.from_bytes(block[8*j:8*j+8], 'big') for j in range(8)]
    s = [state[j] ^ lanes[j] for j in range(8)]

    # 16 rounds FPCH sur chaque lane indépendamment
    for round_idx in range(16):
        alpha, beta, gamma, D = params[round_idx]
        s = [fpch_layer(s[j], alpha, beta, gamma, D) for j in range(8)]

    return s

# ── Hash complet FPCH-512 (Déf. 3.3) ─────────────────────────────────────────
def fpch_hash512(message: bytes, master_seed: bytes = b'\x00' * 32) -> bytes:
    """
    FPCH-512 conforme au papier.
    Retourne 512 bits (64 bytes).
    """
    params = derive_params(master_seed)
    padded = _pad(message)
    state = list(IV) # 8 lanes initialisées avec les √D fractionnels

    for i in range(0, len(padded), 64):
        state = _compress(state, padded[i:i+64], params)

    return b''.join(s.to_bytes(8, 'big') for s in state)

# ── Demo ──────────────────────────────────────────────────────────────────────
def demo():
    print("=" * 70)
    print("FPCH-512 V5 — Conforme au papier v8")
    print("=" * 70)

    # Vérification IV
    print("\nIV (parties fractionnelles de √D × 2^64):")
    for d, iv in zip([5,8,12,13,17,21,24,28], IV):
        print(f" √{d:2d} frac × 2^64 = {iv:016x}")

    # Tests
    print("\nTests FPCH-512:")
    tests = [b"Hello World", b"Hello WorlD", b"", b"A" * 1000]
    for msg in tests:
        h = fpch_hash512(msg)
        label = repr(msg) if len(msg) <= 20 else f"b'A'×{len(msg)}"
        print(f" {label:20} -> {h.hex()[:32]}...")

    # Avalanche
    h1 = fpch_hash512(b"Hello World")
    h2 = fpch_hash512(b"Hello WorlD")
    xor = int.from_bytes(h1, 'big') ^ int.from_bytes(h2, 'big')
    diff = bin(xor).count('1')
    print(f"\nAvalanche: {diff}/512 bits ({diff/512*100:.1f}%)")

    # Déterminisme
    assert fpch_hash512(b"test") == fpch_hash512(b"test")
    print("Déterminisme: OUI ✓")

if __name__ == "__main__":
    demo()
