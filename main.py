import shutil
from pathlib import Path

# Use custom path if available, if not use home
path = "/mnt/f/test"

# Unpack directory
p = Path(path)

# Iterate sub directories
for sub in p.iterdir():
    if sub.is_dir():
        subpath = p / sub

        # Iterate subdirectories in subdirectories
        for item in subpath.iterdir():

            # Move subdirectories
            shutil.move(item, p)
            print(f"Moving: {item} -> {p}")

        # Remove emptysubdirectories
        subpath.rmdir()

