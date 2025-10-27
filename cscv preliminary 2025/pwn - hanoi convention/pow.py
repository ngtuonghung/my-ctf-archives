#!/usr/bin/env python3
"""
Proof of Work Challenge - PoW required before accessing the service
"""

import hashlib
import os
import sys
import time

POW_DIFFICULTY = 6  # Number of leading zeros in the hash


def generate_challenge():
    """Generate a random challenge"""
    return os.urandom(16).hex()


def verify_pow(challenge, answer, difficulty=POW_DIFFICULTY):
    """Check if the PoW is valid"""
    try:
        answer = answer.strip()
        hash_result = hashlib.sha256((challenge + answer).encode()).hexdigest()
        return hash_result.startswith('0' * difficulty)
    except:
        return False


def main():
    print("╔══════════════════════════════════════════╗")
    print("║       PROOF OF WORK CHALLENGE            ║")
    print("╚══════════════════════════════════════════╝")
    print()
    
    challenge = generate_challenge()
    print(f"Challenge: {challenge}")
    print(f"Find a string X such that SHA256(challenge + X) starts with {POW_DIFFICULTY} zeros")
    print(f"Example: SHA256('{challenge}' + X) = 000000...")
    print()
    print("You have 120 seconds to solve...")
    print()
    
    # Set timeout for input
    sys.stdout.flush()
    
    start_time = time.time()
    timeout = 120
    
    try:
        print("Enter your answer: ", end='', flush=True)
        
        # Read with timeout
        answer = sys.stdin.readline()
        
        elapsed = time.time() - start_time
        
        if elapsed > timeout:
            print("\n❌ Time is up!")
            sys.exit(1)
        
        if verify_pow(challenge, answer):
            print("✓ Correct! Connecting...")
            sys.exit(0)
        else:
            print("❌ Wrong!")
            sys.exit(1)
            
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()