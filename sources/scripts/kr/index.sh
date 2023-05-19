
original_path="../../WantedSans.glyphspackage"
target_path="../../WantedSansKR.glyphspackage"

echo ".
Remove if Wanted Sans KR exists
."
if [ -f $target_path ]; then
    rm $target_path
fi

echo ".
Copy Wanted Sans to Wanted Sans KR
."
cp -R $original_path $target_path

echo ".
Copy Hangul Split to Wanted Sans KR
."
split_path="../../splits/WantedSans-Split-Hangul.glyphspackage"
cp -R $split_path/glyphs/* $target_path/glyphs/

echo ".
Replace Font Info
."
python3 fontinfo-replace.py

echo ".
Merge Order
."
python3 order-merge.py
