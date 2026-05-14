# FPCH Benchmarks

**Environment:** Apple M4 Pro, macOS 15, Python 3.14
**Date:** 2026-05-14

---

## Reproducible Test Suite

```bash
cd tests/
python3 test_fpch_v6.py
```

The script is deterministic (seed = `0x5EED`) and produces a JSON report.

## Results Summary

| Test | Metric | Result | Acceptance |
|---|---|---|---|
| **Determinism** | Same input → same output | ✅ PASS | 1M repetitions |
| **Cross-Lane Mixing** | All lanes change | ✅ PASS | 8/8 lanes |
| **Weak Inputs** | Empty, 0x00, 0xFF, periodic | ✅ PASS | All distinct |
| **NIST Frequency** | Proportion of 1s | ✅ PASS | p = 0.4133 |
| **NIST Runs** | Run distribution | ✅ PASS | p = 0.6403 |
| **NIST Serial (m=4)** | Pattern distribution | ✅ PASS | p = 0.0156 |
| **Avalanche (SAC)** | Avg. changed bits | ✅ PASS | 255.9/512 (49.98%) |
| **Diffusion** | Avg. changed bits | ✅ PASS | 256.0/512 (50.00%) |
| **Collision (32-bit)** | Birthday on 50K msgs | ✅ PASS | 1 collision (theoretical 25.3%) |

## Python Performance (Reference)

| Operation | Time / call |
|---|---|
| `fpch_hash512_v6(b"test")` | ~2.5 ms (CPython, single-thread) |

**Note:** This is a reference implementation, not optimized. A C or CUDA implementation would be orders of magnitude faster.

## Comparative Notes

| Algorithm | Throughput (ref.) | Security |
|---|---|---|
| SHA-256 (OpenSSL) | ~0.8 GB/s | Proven |
| BLAKE3 | ~3.5 GB/s | Proven |
| FPCH V6 (Python) | ~0.25 MB/s | **Conjectural** |

Do **not** use FPCH in production. It is an experimental target for cryptanalysis.
