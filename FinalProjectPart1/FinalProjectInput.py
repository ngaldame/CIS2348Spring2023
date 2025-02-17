import csv
from datetime import datetime


# Class for methods used to create output inventory files from provided input
class OutputInventory:

    def __init__(self, item_list):
        self.item_list = item_list

    # full function will write to FullInventory.csv
    def full(self):
        # Open FullInventory.csv for writing and sort all the keys
        with open('FullInventory.csv', 'w') as the_file:
            all_items = self.item_list
            all_keys = sorted(all_items.keys())

            # for loop will iterate through each key which is an item's attribute
            for single_item in all_keys:
                iden = single_item
                name_man = all_items[single_item]['manufacturer']
                type_item = all_items[single_item]['item_type']
                the_price = all_items[single_item]['price']
                date_service = all_items[single_item]['service_date']
                damage = all_items[single_item]['damaged']

                # Write all the traits of an item to FullInventory.csv
                the_file.write(f'{iden}, {name_man}, {type_item}, {the_price}, {date_service}, {damage}\n')

    # by_type function will write to LaptopInventory.csv
    def by_type(self):

        # A csv file will have item ID, manufacturer name, price, service date, damaged written to it
        all_items = self.item_list
        all_types = []
        all_keys = sorted(all_items.keys())

        # For loop will check the item types and append them IF they are not already in the keys
        for single_item in all_items:
            type_item = all_items[single_item]['item_type']
            if type_item not in all_types:
                all_types.append(type_item)
        for single_type in all_types:

            with open('LaptopInventory.csv', 'w') as the_file:
                for single_item in all_keys:
                    iden = single_item
                    name_man = all_items[single_item]['manufacturer']
                    the_price = all_items[single_item]['price']
                    date_service = all_items[single_item]['service_date']
                    damage = all_items[single_item]['damaged']
                    type_item = all_items[single_item]['item_type']

                    # Write to file if one item's type is already inside the list
                    if single_type == type_item:
                        the_file.write(f'{iden}, {name_man}, {the_price}, {date_service}, {damage}\n')

    # past_service function will write to PastServiceDateInventory.csv
    def past_service(self):

        # A csv output file made for items past the service date and sorted from old to new
        all_items = self.item_list

        # Get all the keys and sort them
        all_keys = sorted(all_items.keys(), reverse=True)

        with open('PastServiceDateInventory.csv', 'w') as the_file:
            # for loop will get all traits if each item in the keys
            for single_item in all_keys:
                iden = single_item
                name_man = all_items[single_item]['manufacturer']
                type_item = all_items[single_item]['item_type']
                the_price = all_items[single_item]['price']
                date_service = all_items[single_item]['service_date']
                damage = all_items[single_item]['damaged']
                present = datetime.now().date()
                service_exp = datetime.strptime(date_service, "%m/%d/%Y").date()

                # Write to PastServiceDateInventory.csv IF past service date
                if service_exp < present:
                    the_file.write(f'{iden},{name_man},{type_item},{the_price},{date_service},{damage}\n')

    # damaged function will write to DamagedInventory.csv
    def damaged(self):

        # A csv output file made for all items that are damaged, and sorted from highest to lowest price
        all_items = self.item_list

        # Get order of keys to write to file based on price (reverse will print the items' prices in DESCENDING order)
        all_keys = sorted(all_items.keys(), reverse=True)
        with open('DamagedInventory.csv', 'w') as the_file:

            # for loop will get all traits if each item in the keys
            for single_item in all_keys:
                iden = single_item
                name_man = all_items[single_item]['manufacturer']
                type_item = all_items[single_item]['item_type']
                the_price = all_items[single_item]['price']
                date_service = all_items[single_item]['service_date']
                damage = all_items[single_item]['damaged']

                # if statement will write the id, manufacturer, type, price, and service to DamagedInventory.csv
                if damage:
                    the_file.write(f'{iden}, {name_man}, {type_item}, {the_price}, {date_service}')


# The main driver code is below
if __name__ == '__main__':
    items = {}
    files = ['ManufacturerList.csv', 'PriceList.csv', 'ServiceDatesList.csv']

    # For loop will read through each file and lines in the files with a delimiter of ','
    for file in files:
        with open(file, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for line in csv_reader:
                item_id = line[0]

                # Read each file and strip whitespace for ManufacturerList.csv
                if file == files[0]:
                    items[item_id] = {}
                    man_name = line[1]
                    item_type = line[2]
                    damaged = line[3]
                    items[item_id]['manufacturer'] = man_name.strip()
                    items[item_id]['item_type'] = item_type.strip()
                    items[item_id]['damaged'] = damaged
                elif file == files[1]:
                    price = line[1]
                    items[item_id]['price'] = price
                elif file == files[2]:
                    service_date = line[1]
                    items[item_id]['service_date'] = service_date

    # Create an object of the OutputInventory class and all the output files
    inventory = OutputInventory(items)
    inventory.full()
    inventory.by_type()
    inventory.past_service()
    inventory.damaged()

    # Get the different manufacturers and types in a list
    types = []
    manufacturers = []

    # Check if item manufacturers and types are in types and append them if they are not
    for item in items:
        checked_manufacturer = items[item]['manufacturer']
        checked_type = items[item]['item_type']
        if checked_manufacturer not in types:
            manufacturers.append(checked_manufacturer)
        if checked_type not in types:
            types.append(checked_type)

    # Below will be the code for Final Project Part 2
    # Prompt the user for input (will be for step iv)
    user_input = None
    while user_input != 'q':
        user_input = input('\nEnter an item manufacturer and type (ex: Apple laptop) or enter \'q\' to quit:\n')
        if user_input == 'q':
            break
        else:
            # Check each word from user to see if there is a match in manufacturer and item type
            selected_manufacturer = None
            selected_type = None
            user_input = user_input.split()
            bad_input = False
            for word in user_input:
                if word in manufacturers:
                    if selected_manufacturer:
                        # Should only have one submitted manufacturer
                        bad_input = True
                    else:
                        selected_manufacturer = word
                elif word in types:
                    if selected_type:
                        # Should only have one submitted type
                        bad_input = True
                    else:
                        selected_type = word

            # if-else statement determines if there is a match or not (will be for step i)
            if not selected_manufacturer or not selected_type or bad_input:
                print('No such item in inventory')
            else:
                # Ordered list of keys to iterate through based on highest price first using list comprehension
                # noinspection PyTypeChecker
                keys = sorted(items.keys(), key=[x for x in range(len(items)) if items[x]['price']], reverse=True)

                # Get the matching list of items based on user input
                matching_items = []

                # Store items with same type, different manufacturer, in inventory, undamaged status, not past service
                similar_items = {}
                for item in keys:
                    if items[item]['item_type'] == selected_type:

                        # Don't add damaged items or past service to matched list or similar list
                        today = datetime.now().date()
                        service_date = items[item]['service_date']
                        service_expiration = datetime.strptime(service_date, "%m/%d/%Y").date()
                        expired = service_expiration < today
                        if items[item]['manufacturer'] == selected_manufacturer:
                            if not expired and not items[item]['damaged']:
                                matching_items.append((item, items[item]))
                        else:
                            if not expired and not items[item]['damaged']:
                                similar_items[item] = items[item]

                # Output the item if matched, else notify that item is not found (will be for step ii)
                if matching_items:
                    item = matching_items[0]
                    item_id = item[0]
                    man_name = item[1]['manufacturer']
                    item_type = item[1]['item_type']
                    price = item[1]['price']

                    # Print if the item is matched
                    print(f'Your item is: {item_id}, {man_name}, {item_type}, {price}')

                    # Output item from different manufacturer that is closest in price to matched item
                    if similar_items:
                        matched_price = price

                        # Get the similar item with the closest price to the initial item
                        closest_item = None
                        closest_price_diff = None
                        for item in similar_items:
                            if closest_price_diff is None:
                                closest_item = similar_items[item]
                                closest_price_diff = abs(int(matched_price) - int(similar_items[item]['price']))
                                item_id = item
                                man_name = similar_items[item]['manufacturer']
                                item_type = similar_items[item]['item_type']
                                price = similar_items[item]['price']
                                continue

                            # print a recommended same item type from another manufacturer for part iii
                            price_diff = abs(int(matched_price) - int(similar_items[item]['price']))
                            if price_diff < closest_price_diff:
                                closest_item = item
                                closest_price_diff = price_diff
                                item_id = item
                                man_name = similar_items[item]['manufacturer']
                                item_type = similar_items[item]['item_type']
                                price = similar_items[item]['price']

                                print(f'Also look at: {item_id}, {man_name}, {item_type}, {price}')
                else:
                    print('No such item in inventory')
