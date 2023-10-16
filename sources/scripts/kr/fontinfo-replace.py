import os
import re

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, '../../WantedSans.glyphspackage/fontinfo.plist')

with open(file_path, 'r') as f:
    contents = f.read()

# Update font name
contents = re.sub(r'(Wanted Sans) Std([^\w]|$)', r'\1\2', contents)

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
