#!/usr/bin/env bash
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
python3 "$DIR/../../generator.py" --length 8 --no-symbols
read -p "Press enter to continue..."

