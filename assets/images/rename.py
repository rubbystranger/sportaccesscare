from pathlib import Path

# Directory where this script is located
BASE_DIR = Path(__file__).resolve().parent

# Folders
folder_a = BASE_DIR / "media2"      # Files to rename -- destination
folder_b = BASE_DIR / "event"    # Files whose names will be copied -- source

# Check that folders exist
if not folder_a.exists():
    raise FileNotFoundError(f"Folder not found: {folder_a}")

if not folder_b.exists():
    raise FileNotFoundError(f"Folder not found: {folder_b}")

# Get files
files_to_rename = sorted([f for f in folder_a.iterdir() if f.is_file()])
source_files = sorted([f for f in folder_b.iterdir() if f.is_file()])

print(f"Files in Sportcare: {len(files_to_rename)}")
print(f"Files in backgrounds: {len(source_files)}")

# Ensure both folders contain the same number of files
if len(files_to_rename) != len(source_files):
    raise ValueError(
        f"Different number of files!\n"
        f"Sportcare: {len(files_to_rename)}\n"
        f"backgrounds: {len(source_files)}"
    )

# Step 1: Rename to temporary names
temp_files = []
for i, file in enumerate(files_to_rename):
    temp = folder_a / f"__temp_{i}{file.suffix}"
    file.rename(temp)
    temp_files.append(temp)

# Step 2: Rename to the names from backgrounds
for temp, source in zip(temp_files, source_files):
    new_name = source.stem + temp.suffix
    temp.rename(folder_a / new_name)

print("✅ Done! All files have been renamed successfully.")
