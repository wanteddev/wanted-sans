#!/bin/zsh
set -e

script_dir="$(cd "$(dirname "$0")" && pwd)"
split_path="$script_dir/../../splits/WantedSans-Split-Symbol.glyphspackage"
target_path="$script_dir/../../WantedSansBase.glyphspackage"

echo "Fixing Master ID..."
python3 "$script_dir/layerid-fix.py"

echo "Copying Symbol Split to Wanted Sans Base..."
cp -R "$split_path/glyphs/" "$target_path/glyphs/"

echo "Done!"
