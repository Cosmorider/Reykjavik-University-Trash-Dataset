import os
import json
import re

# The directory containing the photos
photo_directory = "ALL_PHOTOS"

# A regular expression pattern to extract the metadata from the file names
pattern = r"dc(\d{6})id(\d+)li(\d)o(\d)s(\d)pi(\d+)c(\d+)cl(\d+)(.*?)r(\d+)s(\d)(.*)"

# A dictionary to store the metadata
metadata = {}

# Get the current script directory
script_directory = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the photo directory
photo_directory_path = os.path.join(script_directory, photo_directory)

# Iterate through the files in the photo directory
for filename in os.listdir(photo_directory_path):
    # Check if the file name matches the pattern
    match = re.match(pattern, filename)
    if match:
        # Extract the metadata from the file name
        metadata[filename] = {
            "dc": match.group(1),
            "id": match.group(2),
            "li": match.group(3),
            "o": match.group(4),
            "s": match.group(5),
            "pi": match.group(6),
            "c": match.group(7),
            "cl": match.group(8),
            "description": match.group(9),
            "r": match.group(10),
            "s": match.group(11),
        }

# Save the metadata to a JSON file
with open("metadata.json", "w") as outfile:
    json.dump(metadata, outfile, indent=2)
