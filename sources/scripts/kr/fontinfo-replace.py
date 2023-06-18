import os
import re

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, '../../WantedSans.glyphspackage/fontinfo.plist')

with open(file_path, 'r') as f:
    contents = f.read()

# Update font name
contents = re.sub(r'(Wanted Sans) Std([^\w]|$)', r'\1\2', contents)

# Update master and instances
contents = contents.replace('axesValues = (\n900\n);\ncustomParameters = (\n{\nname = "Master Icon Glyph Name";\nvalue = B;',
                            'axesValues = (\n1012.5\n);\ncustomParameters = (\n{\nname = "Master Icon Glyph Name";\nvalue = B;')
contents = contents.replace('"94F54C43-8AEE-4ED6-B3C2-2A9D33534E61" = 0.2;\nm01 = 0.8;',
                            '"94F54C43-8AEE-4ED6-B3C2-2A9D33534E61" = 0.16327;\nm01 = 0.83673;')
contents = contents.replace('"94F54C43-8AEE-4ED6-B3C2-2A9D33534E61" = 0.4;\nm01 = 0.6;',
                            '"94F54C43-8AEE-4ED6-B3C2-2A9D33534E61" = 0.32653;\nm01 = 0.67347;')
contents = contents.replace('"94F54C43-8AEE-4ED6-B3C2-2A9D33534E61" = 0.6;\nm01 = 0.4;',
                            '"94F54C43-8AEE-4ED6-B3C2-2A9D33534E61" = 0.4898;\nm01 = 0.5102;')
contents = contents.replace('"94F54C43-8AEE-4ED6-B3C2-2A9D33534E61" = 0.8;\nm01 = 0.2;',
                            '"94F54C43-8AEE-4ED6-B3C2-2A9D33534E61" = 0.65306;\nm01 = 0.34694;')
contents = contents.replace('"94F54C43-8AEE-4ED6-B3C2-2A9D33534E61" = 1;',
                            '"94F54C43-8AEE-4ED6-B3C2-2A9D33534E61" = 0.81633;\nm01 = 0.18367;')

# Write changes
with open(file_path, 'w') as f:
    f.write(contents)

# Add codePageRanges
insert_code = '''},
{
name = ROS;
value = "Adobe-Identity-0";
},
{
name = codePageRanges;
value = (
"1252",
"949"
);
'''

# Find the code for adding codePageRanges
with open(file_path, 'r+') as f:
    lines = f.readlines()
    add_code = False
    for i, line in enumerate(lines):
        if 'name = fsType;' in line:
            add_code = True
        elif add_code and ');' in line:
            lines.insert(i+1, insert_code)
            add_code = False
    f.seek(0)
    f.writelines(lines)
    f.truncate()
