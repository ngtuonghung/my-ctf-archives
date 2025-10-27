#!/usr/bin/env bash
# set -Eeuo pipefail

# POW_TIMEOUT=120
# echo "[*] Starting PoW verification..."

# # Chạy Proof of Work với timeout
# timeout --signal=TERM --kill-after=5s "${POW_TIMEOUT}" python3 /home/quiz/pow.py

# POW_EXIT_CODE=$?

# if [ $POW_EXIT_CODE -eq 124 ] || [ $POW_EXIT_CODE -eq 137 ]; then
#     echo "⏱️  PoW timeout! Please solve faster."
#     exit 1
# elif [ $POW_EXIT_CODE -ne 0 ]; then
#     echo "❌ PoW verification failed!"
#     exit 1
# fi
# echo "[+] PoW verification passed!"

TIME_LIMIT=300
TARGET="/home/quiz/quiz"
cd /home/quiz
exec timeout --signal=TERM --kill-after=5s "${TIME_LIMIT}" stdbuf -i0 -o0 -e0 "$TARGET" "$@" 2>/dev/null