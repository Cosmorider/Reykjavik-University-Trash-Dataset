# Reykjavik-University-Trash-Dataset
Code for collecting pictures of trash with an insanely detailed encoding scheme for research purposes

| Parameter          | Description                                              | Parameter values                          | Purpose                                  |
|--------------------|----------------------------------------------------------|-------------------------------------------|------------------------------------------|
| dc                 | Date of capture                                          | DDMMYY                                    | Identifying capture date                 |
| id                 | User ID                                                  | N/A                                       | Identifying user                         |
| li                 | Lighting                                                 | 0: No lighting <br> 1: Partial lighting <br> 2: Full lighting | Describing lighting conditions       |
| o                  | Bin origin                                               | 0: Plastic bin <br> 1: Paper bin <br> 2: General bin <br> 3: Cans bin <br> 4: Unknown | Describing bin origin                 |
| l                  | location                                               | 0: Sólinn, 1: Jörðinn, 2: Either, 3: Unknown | Describing bin origin                 |
| pi                 | Primary item count                                       | N/A                                       | Counting primary items                   |
| c                  | Composite                                                | 0: Not composite, 1: Composite           | Indicating if an item is composite       |
| cl                 | Item type                                                | 00: Aluminum cans <br> 01: Bleached paper <br> 02: Bottle cap <br> 03: Bottle labels <br> 04: Cardboard <br> 05: Empty <br> 06: Hand <br> 07: HDPE bottle <br> 08: Ice cream wrappers <br> 09: Lids <br> 10: Metallized film <br> 11: Paper cups <br> 12: Paper plastic composite <br> 13: Paper straw <br> 14: Paper tissues <br> 15: PET bottle <br> 16: Plastic food packaging <br> 17: Plastic wrapper <br> 18: Recycled cardboard <br> 19: Smoothie bottle <br> 20: Snus container <br> 21: Sticky notes <br> 22: Tetra pak <br> 23: Unbleached paper <br> 24: Electronics <br> 25: Plastic cutlery <br> 26: Plastic straws <br> 27: Plastic bags <br> 28: Polystyrene foam <br> 29: Windowed envelopes <br> 30: Books notebooks <br> 31: Magazines <br> 32: Glass jars <br> 33: Broken glass <br> 34: Food waste <br> 35: Textiles <br> 36: Wood <br> 37: Rubber <br> 38: Gum <br> 39: Mixed material container <br> 40: Food wrap <br> 41: Paper bags <br> 42: Metallic cutlery <br> 43: Ear plugs <br> 44: Paper wrap <br> 45: Nicotine pouches <br> 46: Paper container <br> 47: Paper lid <br> 48: Cupcake liners <br> 49: Receipts <br> 50: Compostable tray <br> 51: Bleached paper | Identifying item type                    |
| p                  | Partial object                                           | 0: Not partial <br> 1: Quarter partial <br> 2: Half partial <br> 3: Three quarters partial | Describing object's partiality       |
| d                  | Dirtiness                                                | 0: No dirtiness <br> 1: Partial dirtiness <br> 2: Some dirtiness <br> 3: A lot of dirtiness | Describing dirtiness level           |
| de                 | Deformation                                              | 0: Not deformed <br> 1: Partially deformed <br> 2: Somewhat deformed <br> 3: Very deformed | Describing deformation level         |
| u                  | Unopened                                                 | 0: Opened container <br> 1: Unopened container | Indicating if a container is unopened   |
| co                 | Compostable                                              | 0: Uncertain <br> 1: Not compostable, 2: Compostable | Indicating compostability             |
| m                  | Metal type                                               | 0: Not metal <br> 1: Aluminum metal <br> 2: Steel <br> 3: Copper | Identifying metal type                |
| g                  | Glass color                                              | 0: Not glass <br> 1: Transparent <br> 2: Red <br> 3: Green | Describing glass color                |
| pc                 | PET or HDPE color                                        | 0: Not PET or HDPE <br> 1: Transparent <br> 2: Red <br> 3: Green | Describing PET or HDPE color         |
| pl                 | PET or HDPE label                                        | 0: Not PET or HDPE bottle <br> 1: No label <br> 2: Covers half <br> 3: Covers third fourths, 4: Full sleeve | Describing PET or HDPE label         |
| pt                 | Plastic type                                             | 0: Not plastic or not only or not sure, 1: PET <br> 2: PE-HD <br> 3: PVC <br> 4: PE-LD <br> 5: PP <br> 6: PS <br> 7: Other | Identifying plastic type              |
| b                  | Brand                                                    | Various brands or "NO_BRAND"             | Identifying brand                      |
| pr                 | Product                                                  | Various products or "NO_PRODUCT"         | Identifying product                    |
| w                 | Waste stream                                              | 0: Plastic bin <br> 1: Paper bin <br> 2: General bin <br> 3: Cans bin <br> 4: Unknown        | Identifying product                    |
| ui                 | Under item count                                         | N/A                                       | Counting under items                   |
| r                  | Random                                                   | 0-100000                                       | Prevents image files from overwriting each other if they are exactly the same                   |

There are a couple of important things to keep in mind:
1. If there are multiple primary items, they all have individual encodings and can have either none or multiple under items. When parsing the encoding you can separate each primary item by knowing how many there are, this is also true for the under items.
2. The reason for having primary and under items, is to know when there are different items which should go into different waste streams, if this is the case, then they should always go into the general category. Therefore, when there are multiple primary items, they go into the "multiple_items" folder which was made to make a neural network model which can identify if there are object which share the same waste stream or not, and to identify if there are multiple objects.

When collecting data using this encoding, it is assumed that you manually type in the information about the item before inserting it into an "identification chamber", not afterwards.

