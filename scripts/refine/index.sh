#!/bin/zsh
set -e

script_dir="$(cd "$(dirname "$0")" && pwd)"
temp_path="$script_dir/temp"
package_path="$script_dir/../../packages"

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

echo "Moving files to appropriate directories..."
for fonts_file in "$temp_path"/*; do
    if [[ $fonts_file != *"Std"* ]]; then
        if [[ $fonts_file == *.otf && $fonts_file != *"Variable"* ]]; then
            mv "$fonts_file" "$package_path/wanted-sans/fonts/otf"
        elif [[ $fonts_file == *.ttf && $fonts_file != *"Variable"* ]]; then
            mv "$fonts_file" "$package_path/wanted-sans/fonts/ttf"
        elif [[ $fonts_file == *.ttf && $fonts_file == *"Variable"* ]]; then
            mv "$fonts_file" "$package_path/wanted-sans/fonts/variable"
        fi
    elif [[ $fonts_file == *"Std"* ]]; then
        if [[ $fonts_file == *.otf && $fonts_file != *"Variable"* ]]; then
            mv "$fonts_file" "$package_path/wanted-sans-std/fonts/otf"
        elif [[ $fonts_file == *.ttf && $fonts_file != *"Variable"* ]]; then
            mv "$fonts_file" "$package_path/wanted-sans-std/fonts/ttf"
        elif [[ $fonts_file == *.ttf && $fonts_file == *"Variable"* ]]; then
            mv "$fonts_file" "$package_path/wanted-sans-std/fonts/variable"
        fi
    fi
done

echo "Done!"
