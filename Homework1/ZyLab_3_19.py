# Nathan Galdamez Gomez, ngaldame
# This is ZyLab 3.19

import math
# Get a wall's height, width, and area in feet
height = int(input('Enter wall height (feet):\n'))
width = int(input('Enter wall width (feet):\n'))
area = int(height * width)
print(f'Wall area: {area} square feet')
# 1 gallon of paint covers 350 square feet
single_gallon = 350
# Calculate the paint needed, which will have {:.2f} to indicate a float value
print('Paint needed: {:.2f} gallons'.format(area / single_gallon))
# Get paint cans needed and round the value up a whole number using .ceil
print('Cans needed:', math.ceil(area / single_gallon), 'can(s)\n')
# Create dictionary of wall colors for choosing a color and cost of money for choosing that color
wall_colors = {'red': 35, 'blue': 25, 'green': 23}
chosen_color = input('Choose a color to paint the wall:\n')
print(f'Cost of purchasing {chosen_color} paint: ${math.ceil(area / single_gallon) * wall_colors[chosen_color]}')
