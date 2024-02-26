#!/bin/zsh
set -e

script_dir="$(cd "$(dirname "$0")" && pwd)"
temp_path="$script_dir/temp"
package_path="$script_dir/../../packages"
wanted_sans_path="$package_path/wanted-sans/fonts"
wanted_sans_std_path="$package_path/wanted-sans-std/fonts"

echo "Converting fonts to ttx..."
for fonts_file in "$temp_path"/*.(ttf|otf); do
    ttx "$fonts_file"
    rm "$fonts_file"
done

echo "Adding Macintosh Name Table..."
python3 "$script_dir/namerecord.py"

echo "Fixing Font Creation Date..."
python3 "$script_dir/date.py"

echo "Fixing Unintended strings..."
python3 "$script_dir/validate.py"

if find "$temp_path" -type f -name '*VF.ttx' -print -quit | grep -q '.'; then
    echo "Adding Suffix from Variable..."
    python3 "$script_dir/rename.py"
fi

echo "Converting fonts to ttf..."
for fonts_file in "$temp_path"/*.ttx; do
    ttx "$fonts_file"
    rm "$fonts_file"
done

find "$temp_path" -type f -name '*VF.ttf' -print0 | while IFS= read -r -d '' fonts_file; do
    echo "Fixing Variable file name..."
    mv "$fonts_file" "${fonts_file/VF/Variable}"
done


echo "Moving files to appropriate directories..."
for fonts_file in "$temp_path"/*; do
    if [[ $fonts_file != *"Std"* ]]; then
        if [[ $fonts_file == *.otf ]]; then
            target_path="$wanted_sans_path/otf"
        elif [[ $fonts_file == *.ttf && $fonts_file != *"Variable"* ]]; then
            target_path="$wanted_sans_path/ttf"
        elif [[ $fonts_file == *.ttf && $fonts_file == *"Variable"* ]]; then
            target_path="$wanted_sans_path/variable"
        fi
    elif [[ $fonts_file == *"Std"* ]]; then
        if [[ $fonts_file == *.otf ]]; then
            target_path="$wanted_sans_std_path/otf"
        elif [[ $fonts_file == *.ttf && $fonts_file != *"Variable"* ]]; then
            target_path="$wanted_sans_std_path/ttf"
        elif [[ $fonts_file == *.ttf && $fonts_file == *"Variable"* ]]; then
            target_path="$wanted_sans_std_path/variable"
        fi
    fi

    mv "$fonts_file" "$target_path"
done

echo "Done!"
