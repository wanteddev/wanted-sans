import os

script_dir = os.path.dirname(os.path.abspath(__file__))
folder_path = os.path.join(script_dir, 'temp/')


def process_file(file_path, replacements):
    with open(file_path, 'r') as file:
        filedata = file.read()

    for search, replace in replacements.items():
        filedata = filedata.replace(search, replace)

    with open(file_path, 'w') as file:
        file.write(filedata)


file_suffixes = [
    '-', 'Std-', 'VF', 'StdVF'
]

file_name_list = [
    {
        'Â©': '\(c\)'
    },
    {
        'Â©': '\(c\)'
    },
    {
        '<maxComponentDepth value="4"/>': '<maxComponentDepth value="5"/>'
    },
    {
        '<maxComponentDepth value="4"/>': '<maxComponentDepth value="5"/>'
    }
]

for suffix, file_replacements in zip(file_suffixes, file_name_list):
    file_names = [f for f in os.listdir(folder_path) if f.startswith(
        f'WantedSans{suffix}') and f.endswith('.ttx')]
    for file_name in file_names:
        full_path = os.path.join(folder_path, file_name)
        process_file(full_path, file_replacements)
        print(f"Fixed: {full_path}")
