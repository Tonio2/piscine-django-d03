import sys

sys.path.insert(0, "./local_lib")

from path import Path

# Create a directory and a file
dir_path = Path("new_dir")
dir_path.mkdir_p()

file_path = dir_path / "file.txt"

# Write something to the file
with file_path.open("w") as file:
    file.write("quelque chose!")

# Read and print the content of the file
with file_path.open("r") as file:
    content = file.read()
    print(content)
