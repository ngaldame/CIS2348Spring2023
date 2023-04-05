# Nathan Galdamez Gomez, 2141118
# This is ZyLab 10.19

# import math module will round down item prices
import math


# A class called ItemToPurchase
class ItemToPurchase:
    # This is the default constructor
    def __init__(self, item_name='none', item_price=0, item_quantity=0, item_description='none'):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    # print_item_cost function in class will process calculation of an item's cost
    def print_item_cost(self):
        price = self.item_quantity * math.floor(self.item_price)
        statement = f'{self.item_name} {self.item_quantity} @ ${math.floor(self.item_price)} = ${price}'
        return statement

    # print_item_description prints the description of an item
    def print_item_description(self):
        print(f'{self.item_name}: {self.item_description}')

