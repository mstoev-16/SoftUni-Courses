from os import listdir, path


def traverse_dir(current_path):
    for el in listdir(current_path):
        if path.isdir(path.join(current_path, el)):
            traverse_dir(path.join(current_path, el))
        else:
            extension = f".{el.split('.')[-1]}"
            if extension not in file_extensions:
                file_extensions[extension] = []
            file_extensions[extension].append(el)


file_extensions = {}
traverse_dir('.')
for current_ext, files in sorted(file_extensions.items()):
    print(current_ext)
    for file in sorted(files):
        print(f"--- {file}")