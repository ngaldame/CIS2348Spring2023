# Nathan Galdamez Gomez, ngaldame
# This is ZyLab 2.19

# Get input for the measurements of ingredients needed for lemonade
lemon_juice_cups = float(input('Enter amount of lemon juice (in cups):\n'))
water_cups = float(input('Enter amount of water (in cups):\n'))
agave_nectar_cups = float(input('Enter amount of agave nectar (in cups):\n'))
servings_yielded = float(input('How many servings does this make?\n'))
# The 4 lines below just print the ingredients inputted
print('\nLemonade ingredients - yields {:.2f} servings'.format(servings_yielded))
print('{:.2f} cup(s) lemon juice'.format(lemon_juice_cups))
print('{:.2f} cup(s) water'.format(water_cups))
print('{:.2f} cup(s) agave nectar'.format(agave_nectar_cups))
# This will be for servings desired and amount of ingredients desired
servings_desired = float(input('\nHow many servings would you like to make?\n'))
print('\nLemonade ingredients - yields {:.2f} servings'.format(servings_desired))
print('{:.2f} cup(s) lemon juice'.format(lemon_juice_cups * servings_desired / servings_yielded))
print('{:.2f} cup(s) water'.format(water_cups * servings_desired / servings_yielded))
print('{:.2f} cup(s) agave nectar'.format(agave_nectar_cups * servings_desired / servings_yielded))
# The lines below will convert the desired ingredients and servings to gallons
# 1 gallon is the same amount as 16 cups
print('\nLemonade ingredients - yields {:.2f} servings'.format(servings_desired))
print('{:.2f} gallon(s) lemon juice'.format(lemon_juice_cups * servings_desired / servings_yielded / 16))
print('{:.2f} gallon(s) water'.format(water_cups * servings_desired / servings_yielded / 16))
print('{:.2f} gallon(s) agave nectar'.format(agave_nectar_cups * servings_desired / servings_yielded / 16))
