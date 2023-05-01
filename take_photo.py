import cv2
import os
import datetime
import random
import time

def capture_photo(name, filename):
    cam = cv2.VideoCapture(0)
    ret, frame = cam.read()
    if ret:  # Check if the frame was captured successfully
        cv2.imwrite(f"{name}/{filename}.png", frame)
    else:
        print("Failed to capture frame. Skipping this photo.")
        time.sleep(1)
        capture_photo(name, filename)

def create_folder(name):
    if not os.path.exists(name):
        os.makedirs(name)

def get_samples():
    while True:
        try:
            samples = int(input("How many samples to take?: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")
    return samples

def main():
    user_id = 0
    user_name = 'Daníel Logi Matthíasson'
    date_of_capture = datetime.datetime.now().strftime("%d%m%y")

    while (1):
        samples = get_samples()
        for sample_nr in range(1, samples+1):
            if sample_nr == 1 and input("Is this a new setting (y/n): ").lower() == 'y':
                lighting = input("Enter lighting condition (0: No lighting, 1: Partial lighting, 2: Full lighting): ")
                bin_origin = input("Enter bin origin (0: Plastic bin, 1: Paper bin, 2: General bin, 3: Cans bin): ")
                location = input("Enter location of trash (0: Sólinn, 1: Jörðinn): ")
                date_of_capture = input("What is the date on the bag (DDMMYY)?: ")

            if sample_nr == 1:
                same_object = input("Is this a new object (y/n)? ")
                if same_object.lower() == "y":
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

                    # Input Item type
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
                    Item type: '''))
                    item_type = f"{item:02d}"

                    # Map the class number to the folder name
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
                        '41': 'Paper_bags'
                    }

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

                    if item in [0]:  # Metal Items
                        metal_type = input("Enter metal type (0: Not metal, 1: Aluminum metal, 2: Steel, 3: Copper): ")
                    else:
                        metal_type = '0'

                    if item in [32,33]:  # Glass Items
                        glass_color = input("Enter glass color (0: Not glass, 1: Transparent, 2: Red, 3: Green): ")
                    else:
                        glass_color = '0'

                random_number = random.randint(0, 100000)

            halt = input("Next photo? (type anything to continue)")

            # Encoding
            encoded = f"dc{date_of_capture}id{user_id}li{lighting}o{bin_origin}c{composite}cl{item_type}p{partial_object}d{dirtiness}d{deformation}u{unopened}l{location}s{sample_nr}m{metal_type}g{glass_color}pc{pet_color}pl{pet_label}pt{plastic_type}r{random_number}b{brand}pr{product}"

            # Create folder for the class type if it doesn't exist
            folder_name = class_to_folder[item_type]  # Get the folder name from the dictionary
            create_folder(folder_name)

            # Capture photo and save it
            print(f"Taking photo {sample_nr}...")
            capture_photo(folder_name, encoded)

            print(f"Photo {sample_nr} saved as {encoded}.png")

if __name__ == '__main__':
    main()