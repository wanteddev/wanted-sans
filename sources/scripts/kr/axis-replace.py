# Update glyphs coordinates and axisRules

import os
import re

script_dir = os.path.dirname(os.path.abspath(__file__))
folder_path = os.path.join(script_dir, '../../WantedSansKR.glyphspackage/glyphs')

for subdir, dirs, files in os.walk(folder_path):
    for file in files:
        file_path = os.path.join(subdir, file)
        with open(file_path, 'r') as f:
            contents = f.read()
        contents = contents.replace('coordinates = (\n700', 'coordinates = (\n767.5')
        contents = contents.replace('min = 600.001;', 'min = 645.001;')
        contents = contents.replace('max = 600;', 'max = 645;')
        with open(file_path, 'w') as f:
            f.write(contents)
