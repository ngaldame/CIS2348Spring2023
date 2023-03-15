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
        self.item_description = 'none'

    # print_item_cost function in class will process calculation of an item's cost
    def print_item_cost(self):
        print(f'{self.item_name} {self.item_quantity} @ ${math.floor(self.item_price)}', end=' ')
        print(f'= ${self.item_quantity * math.floor(self.item_price)}')

    def print_item_description(self):
        print(f'{self.item_name}: {self.item_description}')

# A class called ShoppingCart
class ShoppingCart:
    def __init__(self, customer_name = 'none', current_date = 'January 1, 2016', cart_items = []):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart_items
    
    # Add methods for ShoppingCart class
    def add_item(self, itemToPurchase):
        self.cart_items.append(itemToPurchase)
    def remove_item(self, s):
        r_item = False
        for i in self.cart_items:
            if i.item_name == s:
                self.cart_items.remove(i)
                r_item = True
                break
            # Maybe change else statement to if not depending on output
            else:
                print('Item not found in cart. Nothing removed.')
    # Modify item ONLY if item being purchased is the same as an item in cart_items
    def modify_item(self, itemToPurchase):
        m_item = False
        for i in range(len(self.cart_items)):
            if self.cart_items[i].item_name == itemToPurchase.item_name:
                m_item = True
                self.cart_items[i].item_quantity = itemToPurchase.item_quantity
                break
            else:
                print('Item not found in cart. Nothing modified.')
    # Just return number of items in cart
    def get_num_items_in_cart(self):
        item_num = 0
        for i in self.cart_items:
            item_num = item_num + i.item_quantity
        return item_num
    # Get the final cost of items in cart
    def get_cost_of_items(self):
        initial_cost = 0
        total_cost = 0
        for i in self.cart_items:
            initial_cost = i.item_quantity * i.item_price
            total_cost += initial_cost
        return total_cost
    # Print total cost
    def print_total(self):
        total_cost = self.get_cost_of_items()
        # if-else statement will find if total_cost is either 0 or not
        if total_cost != 0:
            print(f'{self.customer_name}\'s Shopping Cart - {self.current_date}')
            print(f'Number of Items: {self.get_num_items_in_cart}')
            for i in self.cart_items:
                i.print_item_cost()
            print(f'\nTotal: {total_cost}')
        else:
            print('SHOPPING CART IS EMPTY')
    # Print descriptions of each item
    def print_descriptions(self):
        # if-else statement will determine whether there are items in cart
        if len(self.cart_items) != 0:
            print(f'{self.customer_name}\'s Shopping Cart - {self.current_date}\n')
            print('Item Descriptions')
            for item in self.cart_items:
                item.print_item_description()
        else:
            print('SHOPPING CART IS EMPTY')
            
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
    
