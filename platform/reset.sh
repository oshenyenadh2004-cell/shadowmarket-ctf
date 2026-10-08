#!/bin/bash
# ShadowMarket Takedown - Reset Script
# Restores Stage 4 (the only live/stateful component) to its default state.
# Static stages (1,2,3,5,6) never change, so they don't need resetting.

echo "Resetting ShadowMarket Takedown CTF box..."

cd "$(dirname "$0")"

echo "Stopping and removing existing Stage 4 container..."
docker compose down

echo "Rebuilding and restarting Stage 4 container (fresh database, fresh session state)..."
docker compose up --build -d

echo "Archiving and clearing flag validation log..."
if [ -f validation_log.txt ]; then
    cp validation_log.txt "validation_log_backup_$(date +%Y%m%d_%H%M%S).txt"
    > validation_log.txt
fi

echo "Reset complete. Stage 4 is running fresh at http://localhost:5000"
