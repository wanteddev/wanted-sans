import os
import fileinput

script_dir = os.path.dirname(os.path.abspath(__file__))
source_path = os.path.join(script_dir, '../../splits/WantedSans-Split-Symbol.glyphspackage')
fontinfo_path = os.path.join(source_path, 'fontinfo.plist')
folder_path = os.path.join(source_path, 'glyphs')

new_layer_id = "94F54C43-8AEE-4ED6-B3C2-2A9D33534E61"

with open(fontinfo_path, 'r') as f:
    content = f.read()
id_start = content.find('id = "') + len('id = "')
id_end = content.find('"', id_start)
old_layer_id = content[id_start:id_end]

new_content = content.replace(old_layer_id, new_layer_id)

with open(fontinfo_path, 'w') as f:
    f.write(new_content)

for file_name in os.listdir(folder_path):
    if file_name.endswith(".glyph"):
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, 'r') as f:
            content = f.read()
        if old_layer_id in content:
            for line in fileinput.input(file_path, inplace=True):
                if 'layerId =' in line:
                    line_parts = line.split('"')
                    if len(line_parts) > 1:
                        line = line.replace(line_parts[1], new_layer_id)
                print(line, end='')
