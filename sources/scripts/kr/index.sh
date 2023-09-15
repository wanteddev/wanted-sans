#!/bin/zsh
set -e

script_dir="$(cd "$(dirname "$0")" && pwd)"
original_path="$script_dir/../../WantedSansBase.glyphspackage"
target_path="$script_dir/../../WantedSans.glyphspackage"
split_path="$script_dir/../../splits/WantedSans-Split-Hangul.glyphspackage"

echo "Removing Wanted Sans if it exists..."
if [ -d "$target_path" ]; then
    rm -r "$target_path"
fi

echo "Copying Wanted Sans Base to Wanted Sans..."
cp -R "$original_path" "$target_path"

echo "Copying Hangul Split to Wanted Sans..."
cp -R "$split_path/glyphs/" "$target_path/glyphs/"

echo "Replacing Font Info..."
python3 "$script_dir/fontinfo-replace.py"

echo "Merging Order..."
python3 "$script_dir/order-merge.py"

echo "Done!"
