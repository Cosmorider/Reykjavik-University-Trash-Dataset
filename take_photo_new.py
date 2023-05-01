import cv2
import os
import datetime
import random
import time
import re

random_number = "yeah"

def capture_photo(name, subfolder, filename):
    cam = cv2.VideoCapture(0)
    ret, frame = cam.read()
    if ret and subfolder:  # Check if the frame was captured successfully
        os.makedirs(f"{name}/{subfolder}", exist_ok=True)
        cv2.imwrite(f"{name}/{subfolder}/{filename}.png", frame)
    elif ret:
        os.makedirs(f"{name}", exist_ok=True)
        cv2.imwrite(f"{name}/{filename}.png", frame)
    else:
        print("Failed to capture frame. Skipping this photo.")
        time.sleep(1)
        capture_photo(name, subfolder, filename)

def get_samples():
    while True:
        try:
            samples = int(input("How many samples to take?: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")
    return samples

def get_new_sample_nr(folder_name, encoded_prefix):
    max_sample_nr = 0
    encoded_prefix_regex = re.escape(encoded_prefix)
    
    if os.path.exists(folder_name):
        for file_name in os.listdir(folder_name):
            sample_nr_match = re.search(f"{encoded_prefix_regex}s(\d+)", file_name)
            if sample_nr_match:
                sample_nr = int(sample_nr_match.group(1))
                max_sample_nr = max(max_sample_nr, sample_nr)

    return max_sample_nr + 1

def get_input(message, validation_func=None):
    while True:
        value = input(message)
        if validation_func is None or validation_func(value):
            return value
        print("Invalid input. Please try again.")
    
def create_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

def main():
    user_id = 0
    user_name = 'Daníel Logi Matthíasson'
    date_of_capture = datetime.datetime.now().strftime("%d%m%y")

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
    '39': 'Mixed_material_container',
    '40': 'Food_wrap',
    '41': 'Paper_bags',
    '42': 'Metallic_cutlery',
    '43': 'Ear_plugs',
    '44': 'Paper_wrap',
    '45': 'Nicotine_pouches',
    '46': 'Paper_container',
    '47': 'Paper_lid',
    '48': 'Cupcake_liners',
    '49': 'Receipts',
    '50': 'Compostable_tray',
    '51': 'Bleached_paper',
    }

    while (1):
        samples = get_samples()
        for sample_nr in range(1, samples+1):
            if sample_nr == 1 and input("Is this a new setting (y/n): ").lower() == 'y':
                lighting = input("Enter lighting condition (0: No lighting, 1: Partial lighting, 2: Full lighting): ")
                bin_origin = input("Enter bin origin (0: Plastic bin, 1: Paper bin, 2: General bin, 3: Cans bin, 4: Unknown): ")
                location = input("Enter location of trash (0: Sólinn, 1: Jörðinn, 2: Either, 3: Unknown): ")
                date_of_capture = input("What is the date on the bag (DDMMYY)?: ")

            if sample_nr == 1:
                exact_same = "n"
                same_items = "n"
                while(1):
                    same_object_type = input("Is this a new object type (y/n)? ").lower()
                    if same_object_type != "y" and same_object_type != "n":
                        print("You didn't input 'y' or 'n'")
                    else:
                        break

                if same_object_type.lower() == "n":
                    while(1):
                        exact_same = input("Is it the exact same one (y/n)?").lower()
                        if exact_same != "y" and exact_same != "n":
                            print("You didn't input 'y' or 'n'")
                        else:
                            break

                elif same_object_type.lower() == "y":
                    primary_item_count = int(input("How many primary items are there?: "))
                    primary_items_encoded = []

                    if primary_item_count > 1:
                        same_items = input("Are the primary items the exact same with the same under items (y/n)? ").lower()

                    for pi in range(primary_item_count):
                        dirtiness = input("Enter dirtiness (0: No dirtiness, 1: Partial dirtiness, 2: Some dirtiness, 3: A lot of dirtiness): ")
                        deformation = input("Enter deformation (0: Not deformed, 1: Partially deformed, 2: Somewhat deformed, 3: Very deformed): ")
                        partial_object = input("Enter partial object (0: Not partial, 1: Quarter partial, 2: Half partial, 3: Three quarters partial): ")

                        # Input brand and product
                        brand = input("Enter brand or type 'no': ").upper().replace(" ", "_")
                        product = input("Enter product or type 'no': ").upper().replace(" ", "_")

                        if brand == "NO":
                            brand = "NO_BRAND"
                        if product == "NO":
                            product = "NO_PRODUCT"
                        item = int(input('''Enter item type:
                            00 - Aluminum cans
                            01 - Bleached paper
                            02 - Bottle cap
                            03 - Bottle labels
                            04 - Cardboard
                            05 - empty
                            06 - Hand
                            07 - HDPE bottle
                            08 - Ice cream wrappers
                            09 - Lids
                            10 - Metallized film
                            11 - Paper cups
                            12 - Paper & plastic composite
                            13 - Paper straw
                            14 - Paper tissues
                            15 - PET bottle
                            16 - Plastic food packaging
                            17 - Plastic wrapper
                            18 - Recycled cardboard
                            19 - Smoothie bottle
                            20 - Snus container
                            21 - Sticky notes
                            22 - Tetra pak
                            23 - Unbleached paper
                            24 - Electronics
                            25 - Plastic cutlery
                            26 - Plastic straws
                            27 - Plastic bags
                            28 - Polystyrene foam
                            29 - Windowed envelopes
                            30 - Books and notebooks
                            31 - Magazines
                            32 - Glass jars
                            33 - Broken glass
                            34 - Food waste
                            35 - Textiles
                            36 - Wood
                            37 - Rubber
                            38 - Gum
                            39 - Mixed material containers
                            40 - Food wrap
                            41 - Paper bags
                            42 - Metallic cutlery
                            43 - Ear plugs
                            44 - Paper wrap
                            45 - Nicotine pouches
                            46 - Paper container
                            47 - Paper lid
                            48 - Cupcake liners
                            49 - Receipts
                            50 - Compostable tray
                            51 - Bleached paper
                            Item type: '''))
                        item_type = f"{item:02d}"

                        if item == 0 or item==7 or item==8 or item==10 or item==15 or item==16 or item==17 or item == 19 or item==20 or item==21 or item==32 or item == 39:
                            unopened = input("Enter unopened container (0: Opened container, 1: Unopened container): ")
                        else:
                            unopened = 0

                        # Input composite
                        if item == 10 or item == 20 or item == 22 or item == 29 or item == 39 or item == 12:
                            composite = '1'
                        elif item == 33 or item==35 or item==26 or item == 25 or item == 21 or item == 19 or item==14 or item==13 or item==9 or item==6 or item==5 or item==3 or item==2 or item==1 or item == 40:
                            composite = '0'
                        else:
                            composite = input("Enter composite (0: Not composite, 1: Composite): ")
                        if composite == '1' and item!=17 and item !=16:
                            plastic_type = "0"
                        else:
                            if item == 7:
                                plastic_type = '2'
                            elif item == 15:
                                plastic_type = '1'
                            elif item == 40:
                                plastic_type = '1'
                            else:
                                plastic_type = input("Enter plastic type (0: Not plastic or not only or not sure, 1: PET, 2: PE-HD, 3: PVC, 4: PE-LD, 5: PP, 6: PS, 7: Other): ")

                        # PET, Glass, and Metal specific inputs
                        if item == 15 or item == 7 or item == 40:  # PET or HDPE Bottle
                            pet_color = input("Enter PET or HDPE color (0: Not PET or HDPE, 1: Transparent, 2: Red, 3: Green): ")
                            pet_label = input("Enter PET or HDPE label (0: Not PET or HDPE bottle, 1: No label, 2: Covers half, 3: Covers third fourths, 4: Full sleeve): ")
                        else:
                            pet_color = '0'
                            pet_label = '0'

                        if item in [11, 13, 14, 23, 36, 44, 46, 47, 48]:
                            compostable = input("Enter compostability (0: Uncertain, 1: Not compostable, 2: Compostable)")
                        else:
                            compostable = '1'

                        if item in [0]:  # Metal Items
                            metal_type = input("Enter metal type (0: Not metal, 1: Aluminum metal, 2: Steel, 3: Copper): ")
                        else:
                            metal_type = '0'

                        if item in [32,33]:  # Glass Items
                            glass_color = input("Enter glass color (0: Not glass, 1: Transparent, 2: Red, 3: Green): ")
                        else:
                            glass_color = '0'

                        
                        # Get under items info
                        under_item_count = int(input(f"How many under items are there for primary item {pi + 1}?: "))
                        primary_item_info = f"c{composite}cl{item_type}p{partial_object}d{dirtiness}d{deformation}u{unopened}co{compostable}m{metal_type}g{glass_color}pc{pet_color}pl{pet_label}pt{plastic_type}b{brand}pr{product}ui{under_item_count}"

                        under_items_encoded = []
                        for ui in range(under_item_count):
                            item = int(input('''Enter under item type:
                                00 - Aluminum cans
                                01 - Bleached paper
                                02 - Bottle cap
                                03 - Bottle labels
                                04 - Cardboard
                                05 - empty
                                06 - Hand
                                07 - HDPE bottle
                                08 - Ice cream wrappers
                                09 - Lids
                                10 - Metallized film
                                11 - Paper cups
                                12 - Paper & plastic composite
                                13 - Paper straw
                                14 - Paper tissues
                                15 - PET bottle
                                16 - Plastic food packaging
                                17 - Plastic wrapper
                                18 - Recycled cardboard
                                19 - Smoothie bottle
                                20 - Snus container
                                21 - Sticky notes
                                22 - Tetra pak
                                23 - Unbleached paper
                                24 - Electronics
                                25 - Plastic cutlery
                                26 - Plastic straws
                                27 - Plastic bags
                                28 - Polystyrene foam
                                29 - Windowed envelopes
                                30 - Books and notebooks
                                31 - Magazines
                                32 - Glass jars
                                33 - Broken glass
                                34 - Food waste
                                35 - Textiles
                                36 - Wood
                                37 - Rubber
                                38 - Gum
                                39 - Mixed material containers
                                40 - Food wrap
                                41 - Paper bags
                                42 - Metallic cutlery
                                43 - Ear plugs
                                44 - Paper wrap
                                45 - Nicotine pouches
                                46 - Paper container
                                47 - Paper lid
                                48 - Cupcake liners
                                49 - Receipts
                                50 - Compostable tray
                                51 - Bleached paper
                                Item type: '''))
                            item_type = f"{item:02d}"

                            # Input composite
                            if item == 10 or item == 20 or item == 22 or item == 29 or item == 39 or item == 12:
                                composite = '1'
                            elif item == 33 or item==35 or item==26 or item == 25 or item == 21 or item == 19 or item==14 or item==13 or item==9 or item==6 or item==5 or item==3 or item==2 or item==1 or item == 40:
                                composite = '0'
                            else:
                                composite = input("Enter composite (0: Not composite, 1: Composite): ")
                            if composite == '1' and item!=17 and item !=16:
                                plastic_type = "0"
                            else:
                                if item == 7:
                                    plastic_type = '2'
                                elif item == 15:
                                    plastic_type = '1'
                                elif item == 40:
                                    plastic_type = '1'
                                else:
                                    plastic_type = input("Enter plastic type (0: Not plastic or not only or not sure, 1: PET, 2: PE-HD, 3: PVC, 4: PE-LD, 5: PP, 6: PS, 7: Other): ")

                            if item in [11, 13, 14, 23, 36, 44, 46, 47, 48]:
                                compostable = input("Enter compostability (0: Uncertain, 1: Not compostable, 2: Compostable)")
                            else:
                                compostable = '1'

                            # PET, Glass, and Metal specific inputs
                            if item == 15 or item == 7 or item == 40:  # PET or HDPE Bottle
                                pet_color = input("Enter PET or HDPE color (0: Not PET or HDPE, 1: Transparent, 2: Red, 3: Green): ")
                                pet_label = input("Enter PET or HDPE label (0: Not PET or HDPE bottle, 1: No label, 2: Covers half, 3: Covers third fourths, 4: Full sleeve): ")
                            else:
                                pet_color = '0'
                                pet_label = '0'

                            if item in [0]:  # Metal Items
                                metal_type = input("Enter metal type (0: Not metal, 1: Aluminum metal, 2: Steel, 3: Copper): ")
                            else:
                                metal_type = '0'

                            if item in [32,33]:  # Glass Items
                                glass_color = input("Enter glass color (0: Not glass, 1: Transparent, 2: Red, 3: Green): ")
                            else:
                                glass_color = '0'
                            under_item_info = f"cl{item_type}p{partial_object}d{dirtiness}d{deformation}co{compostable}m{metal_type}g{glass_color}pc{pet_color}pl{pet_label}pt{plastic_type}"
                            under_items_encoded.append(under_item_info)
                        
                        # Combine primary item info with under items info
                        combined_primary_item_info = f"{primary_item_info}" + "".join(under_items_encoded)

                        if same_items == "y":
                            for _ in range(primary_item_count):
                                primary_items_encoded.append(combined_primary_item_info)
                            break

                    # Determine folder
                    if primary_item_count == 1:
                        folder_name = class_to_folder[item_type]
                        subfolder_name=None
                    elif primary_item_count > 1:
                        folder_name = "multiple_items"
                        unique_item_types = set([primary_item[:6] for primary_item in primary_items_encoded])  # Extract unique item types
                        if len(unique_item_types) == 1:
                            print(unique_item_types)
                            subfolder_name = class_to_folder[next(iter(unique_item_types))[4:]]
                        else:
                            subfolder_name = "multiple_different"
                        create_folder(folder_name)
                        folder_name = f"{folder_name}/{subfolder_name}"

                    sus = input("Suspect? Why?(no or else)").upper()

                    if sus == "NO":
                        sus="0"
                    else:
                        sus = "1"+sus

                    create_folder(folder_name)

                if exact_same == "y" and type(random_number) == str:
                    print("RESTART THIS PROGRAM IMMEDIATELY")

                elif exact_same == "n":
                    random_number = random.randint(0, 100000)

                elif exact_same == "y":
                    encoded_prefix = f"dc{date_of_capture}id{user_id}li{lighting}o{bin_origin}pi{primary_item_count}" + "".join(primary_items_encoded) + f"r{random_number}"
                    sample_nr = get_new_sample_nr(folder_name, encoded_prefix)

            halt = input("Next photo? (type anything to continue)")

            encoded = f"dc{date_of_capture}id{user_id}li{lighting}o{bin_origin}s{sample_nr}pi{primary_item_count}" + "".join(primary_items_encoded) + f"r{random_number}"+f"s{sus}"

            # Capture photo and save it
            print(f"Taking photo {sample_nr}...")
            capture_photo(folder_name, subfolder_name, encoded)

            print(f"Photo {sample_nr} saved as {encoded}.png")

if __name__ == '__main__':
    main()