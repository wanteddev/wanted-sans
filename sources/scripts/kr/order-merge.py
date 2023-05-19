import os

script_dir = os.path.dirname(os.path.abspath(__file__))
target_path = os.path.join(script_dir, '../../WantedSansKR.glyphspackage/order.plist')
original_path = os.path.join(script_dir, '../../splits/WantedSans-Split-Hangul.glyphspackage/order.plist')
target_line = 'zero,'


def insert_code(target_path, original_path, target_line):

    with open(target_path, 'r') as a:
        target_lines = a.readlines()

    with open(original_path, 'r') as b:
        b_lines = b.readlines()[1:-1]  # Exclude the first and last lines

    # find target_line from original_path
    for i, line in enumerate(target_lines):
        if target_line in line:
            # Insert the entire code of 'original_path' above target_line
            target_index = i - 1
            target_lines = target_lines[:target_index+1] + b_lines + target_lines[target_index+1:]
            break

    # Add ',' from last code of original_path
    target_lines[target_index + len(b_lines)] = target_lines[target_index + len(b_lines)].rstrip() + ',\n'

    # Write the modified content to target_path
    with open(target_path, 'w') as a:
        a.writelines(target_lines)


insert_code(target_path, original_path, target_line)
