from os import listdir

file_extensions = {}
files = listdir('.')

for file in files:
    extension = f".{file.split('.')[-1]}"
    if extension not in file_extensions:
        file_extensions[extension] = []
    file_extensions[extension].append(file)

with open('report.txt', 'a') as output_file:
    for current_ext, current_files in sorted(file_extensions.items()):
        output_file.write(f"{current_ext}\n")
        for file in sorted(current_files):
            output_file.write(f"--- {file}\n")
