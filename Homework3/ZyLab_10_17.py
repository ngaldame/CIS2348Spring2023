# Nathan Galdamez Gomez, 2141118
# This is ZyLab 10.17

# import math module will round down item prices
import math


# A class called ItemToPurchase
class ItemToPurchase:
    def __init__(self):
        self.item_name = 'none'
        self.item_price = 0
        self.item_quantity = 0

    # print_item_cost function in class will process calculation of an item's cost
    def print_item_cost(self):
        print(f'{self.item_name} {self.item_quantity} @ ${math.floor(self.item_price)}', end=' ')
        print(f'= ${self.item_quantity * math.floor(self.item_price)}')


# Below is the main driver code
if __name__ == '__main__':
    # Create 2 objects of ItemToPurchase class and get input of both item's attributes
    print('Item 1')
    one = ItemToPurchase()
    one.item_name = str(input('Enter the item name:\n'))
    one.item_price = float(input('Enter the item price:\n'))
    one.item_quantity = int(input('Enter the item quantity:\n'))

    print('\nItem 2')
    two = ItemToPurchase()
    two.item_name = str(input('Enter the item name:\n'))
    two.item_price = float(input('Enter the item price:\n'))
    two.item_quantity = int(input('Enter the item quantity:\n'))

    # Calculate total cost of items by multiplying their prices and quantities
    print('\nTOTAL COST')
    one.print_item_cost()
    two.print_item_cost()
    print(f'\nTotal: ', end='')
    print(f'${math.floor(one.item_price) * one.item_quantity + math.floor(two.item_price) * two.item_quantity}')
