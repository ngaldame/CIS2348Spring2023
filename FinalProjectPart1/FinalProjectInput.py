# Nathan Galdamez Gomez, 2141118
# This is ZyLab 11.18

import csv
from datetime import datetime


class Prod:
    def __init__(self, l_item):
        # Complete list of items for outputting into new files
        self.l_item = l_item

    def f_inv(self):
        with open('FullInventory.csv', 'w') as file:
            products = self.l_item
            # Order the items based on the manufacturer
            collection = sorted(products.keys())

            for product in collection:
                identity = product
                name_man = products[product]['manufacturer']
                i_type = products[product]['itemtype']
                price = products[product]['price']
                s_date = products[product]['servicedate']
                damage = products[product]['damaged']
                file.write(f'{identity}, {name_man}, {i_type}, {price}, {s_date}, {damage}')


if __name__ == '__main__':
