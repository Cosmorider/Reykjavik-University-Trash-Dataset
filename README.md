# Reykjavik university trash dataset collection code
Code for collecting pictures of trash with an insanely detailed encoding scheme for research purposes

| Parameter          | Description                                              | Parameter values                          | Purpose                                  |
|--------------------|----------------------------------------------------------|-------------------------------------------|------------------------------------------|
| id                 | ID of the picture                                        | 1-N                                       | To name the file names after the ID      |
| dc                 | Date of when a garbage bag was collected                 | DDMMYY                                    | To create visualizations of what trash goes where        |
| t	                 | Timestamp	                                            | YYYY-MM-DD HH:MM:SS	                    | To record the exact time when a trash item was collected |
| n                  | Name of collector                                        | Name                                      | To know who is responsible for taking the pictures and collecting the info  |
| li                 | Lighting                                                 | 0: No lighting <br> 1: Lighting inside bin <br> 2: Lighting inside and outside bin | To know the lighting conditions, 2 is if there is also light outside coming into the identification chamber       |
| o                  | Bin origin                                               | 0: Plastic bin <br> 1: Paper bin <br> 2: General bin <br> 3: Cans bin <br> 4: Unknown | Describing what waste stream the trash item came from (it can be correct or incorrect)                 |
| l                  | location                                                 | 0: Sólinn, 1: Jörðinn, 2: Either, 3: Unknown | From what location in HR the trash was collected from (feel free to change it based on your location) |
| ct	             | Country	                                                | Country name                              | To identify the country where the trash is collected     |
| mu	             | Municipality	                                            | Municipality name or code	                | To identify the municipality where the trash is collected |
| mrf	             | MRF Facility	                                            | MRF facility name or code	                | To identify the Material Recovery  Facility where the trash is processed |
| s                  | Sample number                                            | 1-N | To be able to take multiple pictures of the same object instance and number each instance |
| wt	             | Weight	                                                | 0: Not specified or unmeasurable <br> Other number: The weight	                        | To provide information about the weight of the trash items in total in grams |
| pi                 | Primary item count                                       | 1-N                                       | Counting primary items                                   |
| c                  | Composite                                                | 0: Not composite, 1: Composite            | To know if a trash item is not composed of just one material       |
| cl                 | Item type                                                | 00: Aluminum cans <br> 01: Bleached paper <br> 02: Bottle cap <br> 03: Bottle labels <br> 04: Cardboard <br> 05: Empty <br> 06: Hand <br> 07: HDPE bottle <br> 08: Ice cream wrappers <br> 09: Lids <br> 10: Metallized film <br> 11: Paper cups <br> 12: Paper plastic composite <br> 13: Paper straw <br> 14: Paper tissues <br> 15: PET bottle <br> 16: Plastic food packaging <br> 17: Plastic wrapper <br> 18: Recycled cardboard <br> 19: Smoothie bottle <br> 20: Snus container <br> 21: Sticky notes <br> 22: Tetra pak <br> 23: Unbleached paper <br> 24: Electronics <br> 25: Plastic cutlery <br> 26: Plastic straws <br> 27: Plastic bags <br> 28: Polystyrene foam <br> 29: Windowed envelopes <br> 30: Books notebooks <br> 31: Magazines <br> 32: Glass jars <br> 33: Broken glass <br> 34: Food waste <br> 35: Textiles <br> 36: Wood <br> 37: Rubber <br> 38: Gum <br> 39: Mixed material container <br> 40: Food wrap <br> 41: Paper bags <br> 42: Metallic cutlery <br> 43: Ear plugs <br> 44: Paper wrap <br> 45: Nicotine pouches <br> 46: Paper container <br> 47: Paper lid <br> 48: Cupcake liners <br> 49: Receipts <br> 50: Compostable tray <br> 51: Bleached paper              | Identifying item type                                    |
| sh	             | Shape of the object	                                    | 0: Not applicable or unknown <br> 1: Cylindrical <br> 2: Rectangular <br> 3: Spherical <br> 4: Cuboidal <br> 5: Conical <br> 6: Prismatic <br> 7: Toroidal <br> 8: Irregular <br> 9: Flat <br> 10: Tubular of the trash items | For research purposes, can be indicative of material composition |
| p                  | Partial object                                           | 0: Not partial <br> 1: Quarter partial <br> 2: Half partial <br> 3: Three quarters partial | Describing object's partiality             |
| d                  | Dirtiness                                                | 0: No dirtiness <br> 1: Partial dirtiness <br> 2: Some dirtiness <br> 3: A lot of dirtiness | Describing dirtiness (contamination) level (subjective)   |
| sd	             | Source of dirtiness	                                    | 0: None <br> 1: Food <br> 2: Liquids <br> 3: Chemicals <br> 4: Other	                               | To identify the source of dirtiness of the trash items |
| re	             | Recyclable or not	                                    | 0: Not recyclable <br> 1: Recyclable <br> 2: Unknown                                                                         | To indicate if the item is recyclable given the waste management from where the trash is collected (this is an educated guess somewhat)                 |
| rc	             | Recycling code	                                        | 0: No recycling code <br> Other number: Recycling code <br> Multiple: multiple recycling codes    | To know if there's a recycling code on the product and what number it is                  |
| md	             | Minimizing Dirtiness                                 	| Text	                                   | To provide guidelines or best practices on how to minimize or avoid contamination for each trash item |
| de                 | Deformation                                              | 0: Not deformed <br> 1: Partially deformed <br> 2: Somewhat deformed <br> 3: Very deformed | Describing deformation level (subjective)  |
| u                  | Unopened                                                 | 0: Opened container <br> 1: Unopened container | Indicating if a container is unopened               |
| co                 | Compostable                                              | 0: Uncertain <br> 1: Not compostable <br> 2: Compostable | Indicating if the item is compostable         |
| coc                | Compostability code                                      | 0: None <br> Else: The code (in numbers) | Gives the compostability code of the item                 |
|bi	                 | Biodegradable	                                        | 0: Not biodegradable <br> 1: Biodegradable <br> 2: Unknown	| To indicate if the item is biodegradable |
| ba                 | Barcode                                                  | 0: None <br> Else: The code (in numbers) | Gives the barcode of the item                             |
| m                  | Metal type                                               | 0: Not metal <br> 1: Aluminum metal <br> 2: Steel <br> 3: Copper | Identifying metal type            |
| g                  | Glass color                                              | 0: Not glass <br> 1: Transparent <br> 2: Red <br> 3: Green | Describing glass color                  |
| pc                 | PET or HDPE color                                        | 0: Not PET or HDPE <br> 1: Transparent <br> 2: Red <br> 3: Green | To know if the PET bottle can be processed or not      |
| pl                 | PET or HDPE label                                        | 0: Not PET or HDPE bottle <br> 1: No label <br> 2: Covers half <br> 3: Covers third fourths, 4: Full sleeve | To know if the PET bottle can be processed or not            |
| pt                 | Plastic type                                             | 0: Not plastic or not only or not sure, 1: PET <br> 2: PE-HD <br> 3: PVC <br> 4: PE-LD <br> 5: PP <br> 6: PS <br> 7: Other | Identifying plastic type |
| b                  | Brand                                                    | Various brands or "NO_BRAND"             | Identifying brand                        |
| pr                 | Product                                                  | Various products or "NO_PRODUCT"         | Identifying product                      |
| w                  | Waste stream                                             | 0: Plastic bin <br> 1: Paper bin <br> 2: General bin <br> 3: Cans bin <br> 4: Unknown        | Identifying product                                    |
| ui                 | Under item count                                         | 0-N                                      | Counting under items for a primary item  |
| des                | Description of decomposition                             | 0: None <br> Else: Description           | Giving instructions on how to correctly decompose the object to display on the bin screen, only relevant if the under types for a primary object have different item types which go into different waste streams |                     
| sus                  | If there's anything suspect                        | NO: 0: There's nothing <br> Else: Description                                | Any commentary on if there is something that is unclear or weird                              |

There are a couple of important things to keep in mind:
1. If there are multiple primary items, they all have individual encodings and can have either none or multiple under items. When parsing the encoding you can separate each primary item by knowing how many there are, this is also true for the under items.
2. The reason for having primary and under items, is to know when there are different items which should go into different waste streams, if this is the case, then they should always go into the general category. Therefore, when there are multiple primary items, they go into the "multiple_items" folder which was made to make a neural network model which can identify if there are object which share the same waste stream or not, and to identify if there are multiple objects.

![Club sandwich](sandwich.PNG)

There is a little bit of a problem where the under item is the same as the primary item. However, from my understanding it doesn't seem to be much of an issue in these cases:

![Primary and under same](primary_under_same.png)

The item types were first created to anticipate what trash items would be collected from the waste at HR, but overtime it grew organically based on the trash that I saw when I was collecting, so it is always changing.

When collecting data using this encoding, it is assumed that you manually type in the information about the item before inserting it into an "identification chamber", not afterwards.

I've thought about adding a UI and/or a program in which a photo pops up and you have to insert metadata about it, but I haven't gotten around to it.

