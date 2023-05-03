import os
import json
import re
from pathlib import Path

def process_file_name(file_name):
    file_name = file_name[:-4]  # Remove the file extension ".png"
    
    # Replace the second "d" with "de" and the second "s" with "sus"
    d_count, s_count = 0, 0
    result = []
    for c in file_name:
        if c == 'd':
            d_count += 1
            if d_count == 2:
                c = 'de'
        elif c == 's':
            s_count += 1
            if s_count == 2:
                c = 'sus'
        result.append(c)
    file_name = ''.join(result)
    
    # Split the string using uppercase letters
    parts = re.split('([A-Z])', file_name)[1:]
    keys = parts[0::2]
    values = parts[1::2]
    metadata = {}
    
    for i, key in enumerate(keys):
        if key.islower():
            metadata[key] = values[i]
        else:
            if "under_items" not in metadata:
                metadata["under_items"] = []
            item = {key.lower(): values[i]}
            if len(metadata["under_items"]) == 0:
                metadata["under_items"].append(item)
            else:
                metadata["under_items"][-1].update(item)
                
    return metadata

def main():
    folder_path = "ALL_PHOTOS"
    output_file = "metadata.json"
    metadata = {}
    
    # Get the list of files sorted by creation time
    file_list = sorted(Path(folder_path).iterdir(), key=os.path.getctime)
    
    for index, file_path in enumerate(file_list):
        if file_path.is_file() and file_path.suffix.lower() == ".png":
            metadata[str(index + 1)] = process_file_name(file_path.name)
    
    with open(output_file, "w") as f:
        json.dump(metadata, f, indent=2)

if __name__ == "__main__":
    main()