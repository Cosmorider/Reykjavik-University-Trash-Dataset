import os
import re

def update_date_in_filenames(folder_name, new_date):
    for root, _, files in os.walk(folder_name):
        for file in files:
            if file.endswith('.png'):
                new_file = re.sub(r'dc\d{6}', f'dc{new_date}', file)
                if new_file != file:
                    os.rename(os.path.join(root, file), os.path.join(root, new_file))

if __name__ == '__main__':
    new_date = input("Enter the new date (DDMMYY): ")
    
    class_to_folder = {
        '00': 'Aluminum_cans',
        '01': 'Bleached_paper',
        '02': 'Bottle_cap',
        '03': 'Bottle_labels',
        '04': 'Cardboard',
        '05': 'Empty',
        '06': 'Hand',
        '07': 'HDPE_bottle',
        '08': 'Ice_cream_wrappers',
        '09': 'Lids',
        '10': 'Metallized_film',
        '11': 'Paper_cups',
        '12': 'Paper_plastic_composite',
        '13': 'Paper_straw',
        '14': 'Paper_tissues',
        '15': 'PET_bottle',
        '16': 'Plastic_food_packaging',
        '17': 'Plastic_wrapper',
        '18': 'Recycled_cardboard',
        '19': 'Smoothie_bottle',
        '20': 'Snus_container',
        '21': 'Sticky_notes',
        '22': 'Tetra_pak',
        '23': 'Unbleached_paper',
        '24': 'Electronics',
        '25': 'Plastic_cutlery',
        '26': 'Plastic_straws',
        '27': 'Plastic_bags',
        '28': 'Polystyrene_foam',
        '29': 'Windowed_envelopes',
        '30': 'Books_notebooks',
        '31': 'Magazines',
        '32': 'Glass_jars',
        '33': 'Broken_glass',
        '34': 'Food_waste',
        '35': 'Textiles',
        '36': 'Wood',
        '37': 'Rubber',
        '38': 'Gum',
        '39': 'Mixed material container',
        '40': 'Food_wrap'
    }

    for folder in class_to_folder.values():
        if os.path.exists(folder):
            update_date_in_filenames(folder, new_date)
            print(f"Updated date for all files in the {folder} folder.")
        else:
            print(f"{folder} does not exist. Skipping this folder.")