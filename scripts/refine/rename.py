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
    'VF', 'StdVF'
]

file_replacements_list = [
    {
        'WantedSans': 'WantedSansVariable',
        'Wanted Sans': 'Wanted Sans Variable'
    },
    {
        'WantedSansStd': 'WantedSansStdVariable',
        'Wanted Sans Std': 'Wanted Sans Std Variable'
    }
]

for suffix, file_replacements in zip(file_suffixes, file_replacements_list):
    file_path = os.path.join(folder_path, f'WantedSans{suffix}.ttx')
    process_file(file_path, file_replacements)
