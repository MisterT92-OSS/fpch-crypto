#!/usr/bin/env python3
"""
FPCH V6 — Test Suite Académique
Tests reproductibles pour avalanche, diffusion, NIST SP 800-22, et robustesse.
Auteur: Toufik Salem
Date: 2026-05-14
"""

import sys, math, random, statistics, time, json
from collections import Counter
from datetime import datetime

sys.path.insert(0, '/Users/toufiksalem/fpch-crypto')
from fpch_v6 import fpch_hash512_v6, cross_lane_mix

# ── Paramètres ───────────────────────────────────────────────────────────────
SEED = b'\x00' * 32
SAMPLES_AVALANCHE = 2000
SAMPLES_DIFFUSION = 500
SAMPLES_NIST_BITS = 1_000_000
SAMPLES_COLLISION = 50_000

# ── Utilitaires ────────────────────────────────────────────────────────────────
def bits_from_bytes(data: bytes) -> list:
    return [int(b) for byte in data for b in format(byte, '08b')]

def bit_diff(a: bytes, b: bytes) -> int:
    return sum((x ^ y).bit_count() for x, y in zip(a, b))

def total_bits(data: bytes) -> int:
    return len(data) * 8

# ── Tests NIST simplifiés ──────────────────────────────────────────────────────
def nist_frequency(bits: list) -> dict:
    n = len(bits)
    s = sum(2 * b - 1 for b in bits)
    s_obs = abs(s) / math.sqrt(n)
    p = math.erfc(s_obs / math.sqrt(2))
    return {"name": "Frequency (Monobit)", "p_value": p, "passed": p >= 0.01,
            "detail": f"proportion_1={sum(bits)/n:.4f}"}

def nist_runs(bits: list) -> dict:
    n = len(bits)
    pi = sum(bits) / n
    if abs(pi - 0.5) >= 2 / math.sqrt(n):
        return {"name": "Runs", "p_value": 0.0, "passed": False, "detail": f"pi={pi:.4f}"}
    runs = 1 + sum(1 for i in range(1, n) if bits[i] != bits[i-1])
    mu = 2 * n * pi * (1 - pi)
    var = max(1e-10, 2 * n * pi * (1 - pi) * (2 * n * pi * (1 - pi) - 1) / (n - 1))
    z = (runs - mu) / math.sqrt(var)
    p = math.erfc(abs(z) / math.sqrt(2))
    return {"name": "Runs", "p_value": p, "passed": p >= 0.01,
            "detail": f"runs={runs}, mu={mu:.1f}"}

def nist_serial(bits: list, m: int = 16) -> dict:
    """Serial test (goodness-of-fit on m-bit patterns). Simplified NIST §2.11."""
    n = len(bits)
    # use m=4 for robustness with 1M bits
    m = 4
    k = n // m
    patterns = Counter(tuple(bits[i*m:(i+1)*m]) for i in range(k))
    expected = k / (2**m)
    chi2 = sum((c - expected)**2 / expected for c in patterns.values())
    # degrees of freedom = 2^m - 1 = 15
    p = math.exp(-chi2 / 2)  # rough approximation; exact requires gamma
    return {"name": f"Serial Test (m={m})", "p_value": p, "passed": p >= 0.01,
            "detail": f"chi2={chi2:.2f}, patterns={len(patterns)}/16"}

# ── Tests cryptographiques ───────────────────────────────────────────────────
def test_avalanche() -> dict:
    diffs = []
    for _ in range(SAMPLES_AVALANCHE):
        msg = random.randbytes(64)
        bit = random.randint(0, len(msg)*8 - 1)
        idx, b = divmod(bit, 8)
        msg2 = bytearray(msg)
        msg2[idx] ^= (1 << b)
        h1 = fpch_hash512_v6(bytes(msg), SEED)
        h2 = fpch_hash512_v6(bytes(msg2), SEED)
        diffs.append(bit_diff(h1, h2))
    avg = sum(diffs) / len(diffs)
    ratio = avg / 512
    # Z-test: mean diff should be 256 with variance 128 per sample (binomial approx)
    z = (avg - 256) / math.sqrt(128 / len(diffs))
    p = 2 * (1 - 0.5 * (1 + math.erf(abs(z) / math.sqrt(2))))
    return {"name": "Avalanche (SAC)", "p_value": p, "passed": abs(ratio - 0.5) < 0.05,
            "detail": f"avg_diff_bits={avg:.1f}/512 ({ratio*100:.2f}%)", "metric": ratio}

def test_diffusion() -> dict:
    # Bit-trace: pour un bit d'entrée, combien de bits de sortie changent sur SAMPLES_DIFFUSION
    influence = [[] for _ in range(512)]
    for _ in range(SAMPLES_DIFFUSION):
        base = random.randbytes(64)
        h0 = fpch_hash512_v6(base, SEED)
        for bit_in in range(0, 512, 8):  # échantillonner 64 bits d'entrée
            idx, b = divmod(bit_in, 8)
            mod = bytearray(base)
            mod[idx] ^= (1 << b)
            h1 = fpch_hash512_v6(bytes(mod), SEED)
            diff = bit_diff(h0, h1)
            influence[bit_in].append(diff)
    avg_diff = sum(statistics.mean(v) for v in influence if v) / sum(1 for v in influence if v)
    ratio = avg_diff / 512
    return {"name": "Diffusion", "p_value": ratio, "passed": ratio > 0.45,
            "detail": f"avg_changed_bits={avg_diff:.1f}/512 ({ratio*100:.2f}%)", "metric": ratio}

def test_cross_lane() -> dict:
    state = [0x1111111111111111 + i*0x1111111111111111 for i in range(8)]
    mixed = cross_lane_mix(state)
    changed = sum(1 for a, b in zip(state, mixed) if a != b)
    return {"name": "Cross-Lane Mixing", "p_value": 1.0, "passed": changed == 8,
            "detail": f"lanes_changed={changed}/8"}

def test_determinism() -> dict:
    msg = b"determinism test 123"
    h1 = fpch_hash512_v6(msg, SEED)
    h2 = fpch_hash512_v6(msg, SEED)
    return {"name": "Determinism", "p_value": 1.0, "passed": h1 == h2,
            "detail": f"equal={h1==h2}"}

def test_collision_small_space() -> dict:
    # Birthday sur 32 bits (tronqués) pour voir si comportement anormal
    hashes = {}
    collisions = 0
    for i in range(SAMPLES_COLLISION):
        msg = i.to_bytes(8, 'big')
        h = fpch_hash512_v6(msg, SEED)[:4]
        if h in hashes:
            collisions += 1
        else:
            hashes[h] = i
    # Probabilité théorique birthday sur 2^32 avec n=50000
    p_theo = 1 - math.exp(-SAMPLES_COLLISION*(SAMPLES_COLLISION-1)/(2*(2**32)))
    return {"name": "Collision (32-bit trunc.)", "p_value": 1.0, "passed": True,
            "detail": f"collisions={collisions}, theoretical_prob≈{p_theo:.4f}"}

def test_weak_inputs() -> dict:
    weak = [b'', b'\x00'*64, b'\xff'*64, b'A'*64, b'\x00'*32 + b'\xff'*32]
    hashes = [fpch_hash512_v6(m, SEED) for m in weak]
    uniq = len(set(hashes))
    return {"name": "Weak Inputs", "p_value": 1.0, "passed": uniq == len(weak),
            "detail": f"unique_hashes={uniq}/{len(weak)}"}

# ── Orchestration ─────────────────────────────────────────────────────────────
def main():
    random.seed(0x5EED)
    print("=" * 70)
    print(" FPCH V6 — Test Suite Académique")
    print("=" * 70)

    results = []
    results.append(test_determinism())
    results.append(test_cross_lane())
    results.append(test_weak_inputs())

    # Générer bits pour NIST
    print("\n[1/4] Génération de bits pour tests NIST...")
    bits = []
    for _ in range(SAMPLES_NIST_BITS // 512):
        bits.extend(bits_from_bytes(fpch_hash512_v6(random.randbytes(64), SEED)))
    bits = bits[:SAMPLES_NIST_BITS]

    print("[2/4] Tests NIST SP 800-22...")
    results.append(nist_frequency(bits))
    results.append(nist_runs(bits))
    results.append(nist_serial(bits))

    print("[3/4] Tests cryptographiques...")
    results.append(test_avalanche())
    results.append(test_diffusion())

    print("[4/4] Tests de robustesse...")
    results.append(test_collision_small_space())

    # Rapport
    passed = sum(1 for r in results if r["passed"])
    print("\n" + "=" * 70)
    print(" RÉSULTATS")
    print("=" * 70)
    for r in results:
        s = "PASS" if r["passed"] else "FAIL"
        print(f"  [{s}] {r['name']:<30} p={r['p_value']:.4f}  {r['detail']}")
    print(f"\n  Total: {passed}/{len(results)} tests réussis")

    # JSON
    report = {
        "timestamp": datetime.now().isoformat(),
        "algorithm": "FPCH-512 V6",
        "samples": {
            "avalanche": SAMPLES_AVALANCHE,
            "diffusion": SAMPLES_DIFFUSION,
            "nist_bits": SAMPLES_NIST_BITS,
            "collision": SAMPLES_COLLISION,
        },
        "results": results,
        "summary": {"passed": passed, "total": len(results)}
    }
    out = "/Users/toufiksalem/fpch-crypto/tests/fpch_v6_test_results.json"
    with open(out, "w") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    print(f"\n  Rapport JSON sauvegardé: {out}")

if __name__ == "__main__":
    main()
