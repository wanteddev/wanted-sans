import os
import re


def modify_created_and_modified_values_in_directory(relative_directory, new_value):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    folder_path = os.path.join(script_dir, relative_directory)

    for filename in os.listdir(folder_path):
        if filename.endswith('.ttx'):
            filepath = os.path.join(folder_path, filename)
            with open(filepath, 'r') as file:
                lines = file.readlines()

            modified = False
            head_found = False
            for i, line in enumerate(lines):
                if '<head>' in line:
                    head_found = True
                if head_found and ('<created value="' in line or '<modified value="' in line):
                    lines[i] = re.sub(
                        r'<(created|modified) value="[^"]+"', f'<\\1 value="{new_value}"', line)
                    modified = True

            if modified:
                with open(filepath, 'w') as file:
                    file.writelines(lines)


# 사용 예시
modify_created_and_modified_values_in_directory(
    'temp', 'Sun Nov 12 15:00:00 2023')
