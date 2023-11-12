import os
import re

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(
    script_dir, '../../WantedSans.glyphspackage/fontinfo.plist')

with open(file_path, 'r') as f:
    contents = f.read()


# Update Designers
def update_designers_parameter(lines):
    update_designers = False
    addition_dflt = ' Hangeul from Source Han Sans by Jang Soo-young and Kang Joo-yeon, Sandoll Communications;'
    addition_KOR = ' 한글: 본고딕, 장수영 및 강주연, 산돌커뮤니케이션;'

    for i, line in enumerate(lines):
        if 'key = designers;' in line:
            update_designers = True
        elif update_designers:
            if 'language = dflt;' in line or 'language = KOR;' in line:
                # Check the next line if it starts with 'value = "'
                if i + 1 < len(lines) and lines[i + 1].strip().startswith('value = "'):

                    # Identify the position just before the last quote character
                    last_quote_index = lines[i + 1].rfind('"')

                    # Determine the string to add based on the language
                    addition = addition_dflt if 'language = dflt;' in line else addition_KOR

                    # Insert the addition before the last quote character
                    lines[i + 1] = lines[i + 1][:last_quote_index] + \
                        addition + lines[i + 1][last_quote_index:]

            if ');' in line:
                # End of the designers section
                update_designers = False

    return lines


# Update Trademarks
def update_trademarks_parameter(lines):
    update_trademarks = False
    addition = 'Source is a trademark of Adobe in the United States and/or other countries.'

    for i, line in enumerate(lines):
        if 'key = trademarks;' in line:
            update_trademarks = True
        elif update_trademarks:
            if 'language = dflt;' in line:
                # Scan subsequent lines to find the closing quote and semicolon
                for j in range(i + 1, len(lines)):
                    if '";' in lines[j]:
                        # Insert the addition before the closing quote and semicolon
                        lines[j] = lines[j].replace(
                            '";', f'\n{addition}";')
                        break
                update_trademarks = False
    return lines


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
"1250",
"1254",
"1257",
"949",
"bit 29"
);
'''


# Find the code for adding each function
with open(file_path, 'r+') as f:
    lines = f.readlines()
    add_code = False
    for i, line in enumerate(lines):
        if 'name = fsType;' in line:
            add_code = True
        elif add_code and ');' in line:
            lines.insert(i+1, insert_code)
            add_code = False

    lines = update_designers_parameter(lines)
    lines = update_trademarks_parameter(lines)

    f.seek(0)
    f.writelines(lines)
    f.truncate()
