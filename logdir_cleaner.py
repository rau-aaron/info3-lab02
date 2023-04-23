import argparse
import sys

from hashlib import sha256
from pathlib import Path

# Create argument parser
parser = argparse.ArgumentParser(
    prog="logdir_cleaner",
    description="Removes redundant log files from a directory",
)

parser.add_argument("target_directory", help="Directory to clean (not recursive)")

# Get target_directory from argument parser
args = parser.parse_args()
target_path = Path(args.target_directory)

# Check if the target path actually is a directory
if target_path.is_dir():
    last_hash = ""

    # Itereate over all files in the target directory
    for file in sorted(target_path.iterdir()):
        # Skip if not a file
        if not file.is_file():
            continue

        # Calculate the current file's hash value
        with open(file, "rb") as f:
            current_hash = sha256(f.read()).hexdigest()

        if current_hash == last_hash:
            file.unlink()  # Delete file
        else:
            last_hash = current_hash
else:
    print(f"Invalid target `{target_path}`.")
    sys.exit(1)
