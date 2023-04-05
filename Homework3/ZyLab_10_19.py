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


# A class called ShoppingCart has cart_items parameter initially set to None in order to remove a Pycharm warning
class ShoppingCart:
    def __init__(self, customer_name='none', current_date='January 1, 2016', cart_items=None):
        # if statement will have cart_items become an empty list
        if cart_items is None:
            cart_items = []
            
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart_items

    # add_item function will add an item's properties to the ItemToPurchase class
    def add_item(self):
        print('ADD ITEM TO CART')
        name_item = str(input('Enter the item name:\n'))
        description = str(input('Enter the item description:\n'))
        price = int(input('Enter the item price:\n'))
        quantity = int(input('Enter the item quantity:\n'))
        self.cart_items.append(ItemToPurchase(name_item, price, quantity, description))

    # remove_item function will remove an item from cart
    def remove_item(self):
        print('REMOVE ITEM FROM CART')
        i_name = str(input('Enter name of item to remove:\n'))
        i = 0

        # for loop will search if there is actually an item in the cart or not
        for cart_item in self.cart_items:
            if cart_item.name_item == i_name:
                del self.cart_items[i]
                break
            else:
                print('Item not found in cart. Nothing removed.')

            # increment i by 1 each time in the for loop
            i += 1

    # Modify item ONLY if item being purchased is the same as an item in cart_items
    def modify_item(self):
        print('CHANGE ITEM QUANTITY')
        item_n = str(input('Enter the item name:\n'))

        # A boolean called automatically set to False since the for loop below is not running yet
        found = False

        # for loop searches if an item is already in the cart in order to modify
        for cart_item in self.cart_items:
            # if-else statement finds whether an item exists or not in order to modify it
            if cart_item.name_item == item_n:
                item_q = input('Enter the new quantity:\n')
                cart_item.quantity = item_q

                # A boolean called found is set to True if an item is already in the cart in order to modify it
                found = True
                break
            else:
                found = False

        # Nothing is modified if there is no existing item found in cart_items
        if found is False:
            print('Item not found in cart. Nothing modified.')

    # Just return number of items in cart
    def get_num_items_in_cart(self):
        item_num = 0

        # For loop searches the cart to find the total items inside the cart and returns total items regardless
        for cart_item in self.cart_items:
            item_num = item_num + cart_item.quantity
        return item_num

    # Get the final cost of items in cart
    def get_cost_of_cart(self):
        final_cost = 0

        # All the item's prices in the cart will be added up in the for loop and returned regardless
        for cart_item in self.cart_items:
            initial_cost = cart_item.quantity * cart_item.price
            final_cost += initial_cost
        return final_cost

    # Print total cost
    def print_total(self):
        final_cost = self.get_cost_of_cart()

        # if-else statement will find if final_cost is either 0 or not
        if final_cost != 0:
            self.display_cart()
        else:
            print('SHOPPING CART IS EMPTY')

    # Print descriptions of each item
    def print_descriptions(self):
        print('OUTPUT ITEMS\' DESCRIPTIONS')
        print(f'{self.customer_name}\'s Shopping Cart - {self.current_date}\n')
        print('Item Descriptions')

        # For loop will print each item and their descriptions
        for cart_item in self.cart_items:
            print(f'{cart_item.name_item}: {cart_item.description}')

    # display_cart function displays all the item's traits and final costs
    def display_cart(self):
        print('OUTPUT SHOPPING CART')
        print(f'{self.customer_name}\'s Shopping Cart - {self.current_date}')
        print(f'Number of Items: {self.get_num_items_in_cart()}\n')

        # fin_co is a variable that is set to 0 and will change if there are items in the cart
        # fin_co also will store the final cost of items in the cart_items list
        fin_co = 0

        # For loop will print the traits and final costs of each item inside the cart
        for cart_item in self.cart_items:
            print(f'{cart_item.name_item} {cart_item.quantity} @ {cart_item.price} = ${fin_co}')
            fin_co = cart_item.quantity * cart_item.price

        # if statement will determine whether the length of the cart_items list is 0
        if len(self.cart_items) == 0:
            print('SHOPPING CART IS EMPTY\n')

        # Print the final cost regardless
        print(f'Total: ${fin_co}')

