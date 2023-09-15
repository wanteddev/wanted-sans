#!/bin/zsh
set -e

script_dir="$(cd "$(dirname "$0")" && pwd)"

echo "Fixing Master ID..."
python3 "$script_dir/layerid-fix.py"

echo "Done!"
