#!/bin/zsh
set -e

script_dir="$(cd "$(dirname "$0")" && pwd)"
temp_path="$script_dir/temp"

echo "Converting Variable to ttx..."
for fonts_file in "$temp_path"/*VF.ttf; do
    ttx "$fonts_file"
    rm "$fonts_file"
done

echo "Adding Suffix from Variable..."
python3 "$script_dir/rename.py"

echo "Converting Variable to ttf..."
for fonts_file in "$temp_path"/*VF.ttx; do
    ttx "$fonts_file"
    rm "$fonts_file"
done

echo "Fixing Variable file name..."
for fonts_file in "$temp_path"/*VF.ttf; do
    mv "$fonts_file" "${fonts_file/VF/Variable[wght]}"
done

echo "Done!"
