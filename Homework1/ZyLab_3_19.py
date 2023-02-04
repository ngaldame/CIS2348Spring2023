#Nathan Galdamez Gomez

import math
# Get a wall's height, width, and area in feet
height = int(input('Please enter your wall\'s height (in feet):\n'))
width = int(input('Please enter your wall\'s width (in feet):\n'))
area = int(height * width)
print(f'Wall area: {area} square feet')
# 1 gallon of paint covers 350 square feet
single_gallon = 350
# Calculate the paint needed, which will have {:.2f} to indicate a float value
print('Paint needed: {:.2f} gallons'.format(area / single_gallon))
# Get paint cans needed and round the value up a whole number using .ceil
print('Cans needed: ', math.ceil(area / single_gallon), 'can(s)\n')
# Create dictionary of wall colors for choosing a color and cost of money for choosing that color
wall_colors = {'red': 35, 'blue': 25, 'green': 23}
chosen_color = input('Please choose a color to paint the wall:\n')
print(f'The cost of purchasing {chosen_color} paint is: {wall_colors[chosen_color]}')
