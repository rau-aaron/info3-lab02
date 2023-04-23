# Log directory cleaner program sketch

```py
# Get target directory from user
target_dir = get_path_from_user()

# Iterate over files in directory
for file in target_dir:
    # Calculate hash value of the file
    current_hash = calculate_hash_value(file)

    # Delete file if current_hash equals last_hash
    # or set last_hash to current_hash otherwise
    if current_hash == last_hash:
        delete_file(file)
    else:
        last_hash = current_hash
```
