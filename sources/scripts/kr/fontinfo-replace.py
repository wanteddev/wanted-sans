import re

file_path = '../WantedSans.glyphspackage/fontinfo.plist'

# Read and update font name
with open(file_path, 'r') as f:
    contents = f.read()

contents = re.sub(r'(Wanted Sans).*?([^\w]|$)', r'\1 KR\2', contents)

# Update Weight for KR
contents = contents.replace('axesValues = (\n500', 'axesValues = (\n480')
contents = contents.replace('axesValues = (\n600', 'axesValues = (\n560')
contents = contents.replace('axesValues = (\n700', 'axesValues = (\n640')
contents = contents.replace('axesValues = (\n800', 'axesValues = (\n720')
contents = contents.replace('weightClass = 800;\n},\n{\naxesValues = (\n900', 'weightClass = 800;\n},\n{\naxesValues = (\n800')
contents = contents.replace('"94F54C43-8AEE-4ED6-B3C2-2A9D33534E61" = 0.2;\nm01 = 0.8;', '"94F54C43-8AEE-4ED6-B3C2-2A9D33534E61" = 0.16;\nm01 = 0.84;')
contents = contents.replace('"94F54C43-8AEE-4ED6-B3C2-2A9D33534E61" = 0.4;\nm01 = 0.6;', '"94F54C43-8AEE-4ED6-B3C2-2A9D33534E61" = 0.32;\nm01 = 0.68;')
contents = contents.replace('"94F54C43-8AEE-4ED6-B3C2-2A9D33534E61" = 0.6;\nm01 = 0.4;', '"94F54C43-8AEE-4ED6-B3C2-2A9D33534E61" = 0.48;\nm01 = 0.52;')
contents = contents.replace('"94F54C43-8AEE-4ED6-B3C2-2A9D33534E61" = 0.8;\nm01 = 0.2;', '"94F54C43-8AEE-4ED6-B3C2-2A9D33534E61" = 0.64;\nm01 = 0.36;')
contents = contents.replace('"94F54C43-8AEE-4ED6-B3C2-2A9D33534E61" = 1;', '"94F54C43-8AEE-4ED6-B3C2-2A9D33534E61" = 0.8;\nm01 = 0.2;')

# Write
with open(file_path, 'w') as f:
    f.write(contents)

# Update default script
insert_code = '''},
{
name = codePageRanges;
value = (
"1252",
"949"
);
'''

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
