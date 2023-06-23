# Update glyphs coordinates and axisRules

import os
import re

script_dir = os.path.dirname(os.path.abspath(__file__))
folder_path = os.path.join(script_dir, '../../WantedSans.glyphspackage/glyphs')

for subdir, dirs, files in os.walk(folder_path):
    for file in files:
        file_path = os.path.join(subdir, file)
        with open(file_path, 'r') as f:
            contents = f.read()
        contents = contents.replace('coordinates = (\n700', 'coordinates = (\n767.5')
        contents = contents.replace('min = 601;', 'min = 646;')
        with open(file_path, 'w') as f:
            f.write(contents)
