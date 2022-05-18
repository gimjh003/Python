import sys
import pathlib

file_path = sys.argv[1]

if len(sys.argv) != 2:
    print("python check_empty_dir.py <file path>")
    sys.exit()

main_dir = pathlib.Path(file_path).iterdir()
for lst in main_dir:
    print(lst)