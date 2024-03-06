from pathlib import Path

root_dir = Path('dados')
files_paths = root_dir.iterdir()
# print(list(files_paths))

for path in files_paths:
    # print(path.stem)
    # print(path.suffix)
    new_filename = f'new-{path.stem}{path.suffix}'
    print(new_filename)
    new_filepath = path.with_name(new_filename)
    path.rename(new_filepath)