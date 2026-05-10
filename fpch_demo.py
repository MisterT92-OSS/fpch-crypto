#!/usr/bin/env python3
"""
FPCH - Demonstration Script
A clean, professional demonstration of FPCH concepts
"""

import hashlib
import time
import random

def print_header(title, width=70):
    """Print a formatted header"""
    print("=" * width)
    print(title.center(width))
    print("=" * width)
    print()

def print_section(title):
    """Print a section divider"""
    print()
    print("-" * 70)
    print(f"  {title}")
    print("-" * 70)
    print()

def demonstrate_avalanche():
    """Demonstrate the avalanche effect"""
    print_section("PART 1: AVALANCHE EFFECT")
    
    print("The avalanche effect: changing one bit drastically changes the output")
    print()
    
    # Two messages differing by one bit
    msg1 = b"Hello World"
    msg2 = b"Hello WorlD"  # D instead of d
    
    print(f"Input 1:  {msg1}")
    print(f"Input 2:  {msg2}")
    print()
    
    hash1 = hashlib.sha256(msg1).hexdigest()
    hash2 = hashlib.sha256(msg2).hexdigest()
    
    print(f"Output 1: {hash1}")
    print(f"Output 2: {hash2}")
    print()
    
    # Calculate differences
    diff_bits = sum(c1 != c2 for c1, c2 in zip(hash1, hash2))
    total_bits = len(hash1) * 4  # hex chars
    
    print(f"Analysis:")
    print(f"  - Character differences: {diff_bits} / {len(hash1)}")
    print(f"  - Approximately {diff_bits * 4} bits changed")
    print(f"  - Expected: ~50% of bits should change")
    print()
    
    # Visual representation
    print("Visual comparison (X = different, . = same):")
    comparison = ''.join('X' if c1 != c2 else '.' for c1, c2 in zip(hash1, hash2))
    for i in range(0, len(comparison), 64):
        print(f"  {comparison[i:i+64]}")
    print()

def demonstrate_irrationality_concept():
    """Explain the irrationality concept with ASCII illustration"""
    print_section("PART 2: THE MATHEMATICAL FOUNDATION")
    
    print("FPCH uses irrational numbers from quadratic fields.")
    print()
    print("Concept illustration:")
    print()
    print("  sqrt(5) = 2.2360679774997896964091736687313...")
    print("  sqrt(8) = 2.8284271247461900976033774484194...")
    print("  sqrt(13) = 3.6055512754639892931192212670405...")
    print()
    
    print("These numbers have:")
    print("  1. Infinite non-repeating decimal expansions")
    print("  2. Exact integer representations (128-bit precision)")
    print("  3. Deterministic behavior across all platforms")
    print()
    
    print("Structure of FPCH computation:")
    print()
    print("     Input x (64 bits)")
    print("          |")
    print("          v")
    print("    +------------------+")
    print("    |  sqrt(D) * x^2   |  [Quadratic term]")
    print("    +------------------+")
    print("            |")
    print("            v")
    print("    +------------------+")
    print("    |    + alpha*x     |  [Linear term]")
    print("    |    + beta        |  [Constant]")
    print("    +------------------+")
    print("            |")
    print("            v")
    print("    +------------------+")
    print("    |   / (x + gamma)  |  [Rational nonlinearity]")
    print("    +------------------+")
    print("            |")
    print("            v")
    print("     Output y (64 bits)")
    print()

def demonstrate_performance():
    """Show performance metrics"""
    print_section("PART 3: PERFORMANCE")
    
    print("Running performance benchmark...")
    print()
    
    # Simulate processing
    data_sizes = [1024, 1024*1024, 10*1024*1024]  # 1KB, 1MB, 10MB
    
    print(f"{'Size':>12} {'Time (ms)':>12} {'Throughput':>15}")
    print("-" * 45)
    
    for size in data_sizes:
        data = b"X" * size
        iterations = max(1, 100000000 // size)  # Adjust iterations
        
        start = time.time()
        for _ in range(iterations):
            hashlib.sha256(data)
        end = time.time()
        
        elapsed_ms = (end - start) * 1000
        throughput = (iterations * size) / (1024*1024) / (end - start)
        
        size_str = f"{size/1024/1024:.1f} MB" if size >= 1024*1024 else f"{size/1024:.1f} KB"
        print(f"{size_str:>12} {elapsed_ms:>12.2f} {throughput:>14.2f} MB/s")
    
    print()
    print("Note: These are SHA-256 benchmarks for comparison.")
    print("FPCH-GPU implementation targets 5+ GB/s on RTX 4090.")
    print()

def demonstrate_structure():
    """Show the hash function structure"""
    print_section("PART 4: HASH FUNCTION STRUCTURE")
    
    print("Merkle-Damgard Construction:")
    print()
    print("  Message M")
    print("     |")
    print("     v")
    print("  +------------------+     +------------------+")
    print("  |    Padding       |---->|  Block 1 (512b)  |----+")
    print("  +------------------+     +------------------+    |")
    print("                            |                      |")
    print("                            v                      v")
    print("                      +------------------+     +------------------+")
    print("         +------------|    Compress      |<----|    IV (512b)     |")
    print("         |            +------------------+     +------------------+")
    print("         |                   |                          |")
    print("         |                   v                          v")
    print("         |            +------------------+     +------------------+")
    print("         +------------|    Compress      |<----|   Block 2        |")
    print("         |            +------------------+     +------------------+")
    print("         |                   |")
    print("         ...                 ...")
    print("                            |")
    print("                            v")
    print("                     +------------------+")
    print("                     |   Final Hash     |")
    print("                     |    (512 bits)    |")
    print("                     +------------------+")
    print()
    
    print("Compression function:")
    print("  - 8 parallel lanes of 64 bits each")
    print("  - Each lane processed by FPCH16 (16 layers)")
    print("  - XOR with message block between rounds")
    print()
    print("Security note: Lane independence reduces inter-lane diffusion.")
    print("Explicitly acknowledged as limitation in the paper.")
    print()

def main():
    """Main demonstration"""
    print_header("FPCH - FUNCTION OF CHAOTIC HYPERBOLIC PERMUTATION")
    print("An Invitation to Cryptanalysis")
    print()
    print("GitHub: https://github.com/MisterT92-OSS/fpch-crypto")
    print()
    
    demonstrate_avalanche()
    demonstrate_irrationality_concept()
    demonstrate_performance()
    demonstrate_structure()
    
    print_header("END OF DEMONSTRATION")
    print("For full details, see the paper and source code.")
    print()
    print("Contact: toufik.salem.perso@pm.me")
    print()

if __name__ == "__main__":
    main()
