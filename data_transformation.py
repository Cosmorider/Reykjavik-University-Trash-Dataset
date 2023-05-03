# -*- coding: utf-8 -*-
import os
import re
import json
from datetime import datetime
import shutil

folder_path = "ALL_PHOTOS"

broken_to_icelandic = {
    '\u00c3\u201c': "Ó",
    '\u00c3\u2020': "Æ",
    '\u00c3\u008d': "Í",
    '\u00c3\u0161': "Ú",
    '\u00c3\u008d': "Í",
    '\u00c3\u2013': "Ö",
    '\u00c3\u0090': "Ð",
    '\u00c3\u0081': "Á",
    '\u00c3\u017e': "Þ"
}

shorthand_mappings = {
    "id": "id_of_photo",
    "dc": "date_collected",
    "t": "timestamp",
    "n": "collector_name",
    "li": "lighting_conditions",
    "o": "waste_stream",
    "l": "location",
    "ct": "country",
    "mu": "municipality",
    "mrf": "mrf_facility",
    "s": "sample_number",
    "wt": "weight",
    "pi": "primary_item_count",
    "c": "composite",
    "cl": "item_type",
    "sh": "object_shape",
    "p": "partial_object",
    "d": "dirtiness_level",
    "sd": "source_of_dirtiness",
    "re": "recyclable",
    "rc": "recycling_code",
    "md": "minimizing_dirtiness",
    "de": "deformation_level",
    "u": "unopened_container",
    "co": "compostable",
    "coc": "compostability_code",
    "bi": "biodegradable",
    "ba": "barcode",
    "m": "metal_type",
    "g": "glass_color",
    "pc": "pet_or_hdpe_color",
    "pl": "pet_or_hdpe_label",
    "pt": "plastic_type",
    "b": "brand",
    "pr": "product",
    "w": "waste_stream_for_under_items",
    "ui": "under_item_count",
    "des": "decomposition_description",
    "r": "random_number",
    "sus": "suspect_comments"
}

def process_filename(filename, time):
    first_s_index = filename.find('s')
    # find the index of the second occurrence of 's' by searching after the first one
    second_s_index = filename.find('s', first_s_index + 1)

    if second_s_index >= 0:
        # construct a new string with the second 's' replaced with 'sus'
        filename = filename[:second_s_index] + 'sus' + filename[second_s_index + 1:]

    # First, find the 'sus' key-value pair
    sus_match = re.search(r'(sus)(.+)', filename)

    # Then, remove the 'sus' key-value pair from the filename
    filename = re.sub(r'sus.+', '', filename)

    key_value_pairs = re.findall(r'([a-z]+)(\d+|[A-Z][^a-z]*|[^A-Za-z0-9]+|(?<=sus).*)', filename)

    if sus_match:
        sus_tuple = sus_match.groups()
        value_value = sus_tuple[1]
        sus_tuple = (*sus_tuple[:1], value_value.replace("1",""))
        key_value_pairs.append(sus_tuple)


    if len(key_value_pairs) == 0:
        return None

    json_obj = {}
    primary_items = {}
    pi_count = 1
    ui_count = 0
    decrease_count_pi = 0
    decrease_count_ui = 0
    increase_pi = 0

    if not re.search(r"(?<![a-z])pi(?![a-z])", filename):
        pi1 = {}

    # Fixes the d problem
    count = 0
    for i in range(len(key_value_pairs)):
        if key_value_pairs[i][0] == 'd':
            count += 1
            if count % 2 == 0:  # check if this is the second 'd' encountered
                key_value_pairs[i] = ('de', key_value_pairs[i][1])

    for key, value in key_value_pairs:
        if key == "pi":
            if not re.search(r"cl", filename):
                json_obj[key] = value
                for i in range(int(value)):
                    json_obj[f"pi{i+1}"] = {}
                    for key in ["c", "cl", "sh", "p", "d", "sd", "re", "rc", "md", "de", "u", "co", "coc", "bi", "ba", "s", "m", "g", "pc", "pl", "pt", "b", "pr", "w"]:
                        json_obj[f"pi{i+1}"].update({key: None})
                    json_obj[f"pi{i+1}"].update({"ui": None})
                    json_obj[f"pi{i+1}"].update({"under_items": {}})
                    json_obj[f"pi{i+1}"].update({"des": None})
            else:
                pi_count = int(value)
                decrease_count_pi = pi_count
                json_obj[key] = value
                for i in range(1, pi_count + 1):
                    primary_items[f"pi{i}"] = {}

        elif key == "ui":
            ui_count = int(value)
            decrease_count_ui = ui_count
            increase_pi += 1
            pi_key = f"pi{increase_pi}"
            primary_items[pi_key][key] = value
            primary_items[pi_key]["under_items"] = {}
            for i in range(1, ui_count + 1):
                primary_items[pi_key]["under_items"][f"ui{i}"] = {}
            #primary_items[pi_key]["des"] = None

        elif not re.search(r"(?<![a-z])pi(?![a-z])", filename) and key in ["c", "cl", "sh", "p", "d", "sd", "re", "rc", "md", "de", "u", "co", "coc", "bi", "ba", "s", "m", "g", "pc", "pl", "pt", "b", "pr", "w"]:
            if key == "cl":
                pi1[key]=value
                pi1["sh"]=None
            elif key == "d":
                pi1[key]=value
                pi1["sd"]= None
                pi1["re"]=None
                pi1["rc"]=None
                pi1["md"]=None
            elif key == "u":
                pi1[key] = value
                pi1["co"] = None
                pi1["coc"] = None
                pi1["bi"] = None
                pi1["ba"] = None
            elif key == "pr":
                pi1[key]=value
                pi1["w"]=None
                json_obj["pi"] = "1"
                pi1["ui"]=None
                pi1["under_items"]= {}
                pi1["des"] = None
                json_obj["pi1"] = pi1
                json_obj["sus"] = "0"
            else:
                pi1[key] = value
        elif key == 'dc':
            json_obj['id'] = str(index)
            json_obj['t'] = time
        elif key == 'id':
            json_obj['n'] = "Daníel Logi Matthíasson".upper()
        elif key == "l":
            json_obj[key] = value
            json_obj["mu"] = "Reykjavíkurborg".upper()
            json_obj["mrf"] = "Terra".upper()
            json_obj["wt"] = None
        elif key == 'o' and not re.search(r"(?<![a-z])l(?![a-z])", filename):
            json_obj[key] = value
            json_obj["l"] = '3'
            json_obj["mu"] = "Reykjavíkurborg".upper()
            json_obj["mrf"] = "Terra".upper()
            json_obj["wt"] = "0"
        elif re.search(r"(?<![a-z])l(?![a-z])", filename) and key == 'o':
            json_obj[key] = value
            search_key = "l"

            # Iterate over list of tuples and search for key
            for tuple in key_value_pairs:
                if tuple[0] == search_key:
                    l_value = tuple[1]
                    break
            else:
                value = None
                print("Tuple with key", search_key, "not found.")

            json_obj["l"] = l_value
            json_obj["mu"] = "Reykjavíkurborg"
            json_obj["mrf"] = "Terra"
        elif key == 'l':
            continue

        elif key == 'r':
            continue
        else:
            if key in json_obj:
                if key == "d":
                    key = "de"
                elif key == "b":
                    key = "sus"
                json_obj[key] = value
            else:
                if primary_items:
                    current_primary_item = list(primary_items.keys())[0]
                    if "under_items" in primary_items[current_primary_item]:
                        under_items = primary_items[current_primary_item]["under_items"]
                        if under_items:
                            current_ui = list(under_items.keys())[ui_count-decrease_count_ui]
                            if key == "pt":
                                decrease_count_ui -= 1
                                under_items[current_ui][key] = value
                                under_items[current_ui]["w"] = None

                            elif key == "cl":
                                under_items[current_ui][key] = value
                                under_items[current_ui]["sh"] = None
                            elif key == "d":
                                under_items[current_ui][key] = value
                                under_items[current_ui]["sd"] = None
                                under_items[current_ui]["re"] = None
                                under_items[current_ui]["rc"] = None
                                under_items[current_ui]["md"] = None
                            elif key == "de":
                                under_items[current_ui][key] = value
                                under_items[current_ui]["co"] = None
                                under_items[current_ui]["coc"] = None
                                under_items[current_ui]["bi"] = None
                                under_items[current_ui]["ba"] = None
                            else:
                                under_items[current_ui][key] = value
                            if decrease_count_ui == 0 and key == "pt":
                                json_obj[current_primary_item] = primary_items[current_primary_item]
                                del primary_items[current_primary_item]
                        elif under_items == {} and ui_count==0:
                            primary_items[current_primary_item]["des"] = None
                            json_obj[current_primary_item] = primary_items[current_primary_item]
                            del primary_items[current_primary_item]
                            if primary_items:
                                current_primary_item = list(primary_items.keys())[0]
                                primary_items[current_primary_item][key] = value
                            elif key == "r":
                                json_obj[key] = value
                            elif key == "sus":
                                if value == "NO":
                                    json_obj[key] = "0"
                                json_obj[key] = value
                        else:
                            if key == 'b' or key == 'pr':
                                my_string_fixed = replace_broken_chars(value, broken_to_icelandic)
                                primary_items[current_primary_item][key] = my_string_fixed
                                if not sus_match and key == 'pr':
                                    json_obj["sus"] = "0"
                    else:
                        if key == "cl":
                            primary_items[current_primary_item][key] = value
                            primary_items[current_primary_item]["sh"] = None
                        elif key == "d":
                            primary_items[current_primary_item][key] = value
                            primary_items[current_primary_item]["sd"] = None
                            primary_items[current_primary_item]["re"] = None
                            primary_items[current_primary_item]["rc"] = None
                            primary_items[current_primary_item]["md"] = None
                        elif key == "u":
                            primary_items[current_primary_item][key] = value
                            primary_items[current_primary_item]["co"] = None
                            primary_items[current_primary_item]["coc"] = None
                            primary_items[current_primary_item]["bi"] = None
                            primary_items[current_primary_item]["ba"] = None
                        elif key == "pr":
                            primary_items[current_primary_item][key] = value
                            primary_items[current_primary_item]["w"] = None
                            primary_items[current_primary_item]["des"] = None
                        else:
                            primary_items[current_primary_item][key] = value
                else:
                    json_obj[key] = value

    for pi_key in primary_items.keys():
        json_obj[pi_key] = primary_items[pi_key]

    # Remove empty 'ui' objects
    for pi_key in json_obj:
        if 'ui' in pi_key:
            under_items = json_obj[pi_key]['under_items']
            for ui_key in list(under_items.keys()):
                if not under_items[ui_key]:
                    del under_items[ui_key]

    return json_obj

def replace_broken_chars(s, replacements):
    for k, v in replacements.items():
        if k in s:
            s = s.replace(k, v)
    return s

output = []

# Get all .png files in the folder
png_files = [filename for filename in os.listdir(folder_path) if filename.endswith('.png')]

# Sort the files by their creation time (oldest first)
sorted_files = sorted(png_files, key=lambda f: os.path.getmtime(os.path.join(folder_path, f)))
sorted_time = [os.path.getmtime(os.path.join(folder_path, i)) for i in sorted_files]

broken_to_icelandic = {
    "\u00c3\u201c": "Ó",
    "\u00c3\u2020": "Æ",
    "\u00c3\u008d": "Í",
    "\u00c3\u0161": "Ú",
    "\u00c3\u2013": "Ö",
    "\u00c3\u0090": "Ð",
    "\u00c3\u0081": "Á",
    "\u00c3\u017e": "Þ",
    "\u00c3\u009d": "Ý",
    "\u00c3\u2030": "É",
    "\u00cd\u00de": "Í",
}

# Process the sorted files
index = 1
for filename in sorted_files:
    print(index)
    # create new filename
    new_filename = f"{index}.png"
    # copy file to new folder
    shutil.copy(os.path.join("ALL_PHOTOS", filename), os.path.join("updated_metadata", new_filename))
    json_obj = process_filename(filename.replace(".png", ""), datetime.fromtimestamp(sorted_time[sorted_files.index(filename)]).strftime('%Y-%m-%d %H:%M:%S'))
    if json_obj is not None:
        output.append(json_obj)
        index+=1

# create updated_metadata directory
if not os.path.exists("updated_metadata"):
    os.makedirs("updated_metadata")

metadata_file = "updated_metadata/metadata.json"
with open(metadata_file, "w") as outfile:
    json.dump(output, outfile, indent=2)