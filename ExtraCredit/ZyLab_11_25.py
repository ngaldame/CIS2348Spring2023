# Nathan Galdamez Gomez, 2141118
# This is ZyLab 11.25

# Prompt for four weights
weight_1 = float(input('Enter weight 1:\n'))
weight_2 = float(input('Enter weight 2:\n'))
weight_3 = float(input('Enter weight 3:\n'))
weight_4 = float(input('Enter weight 4:\n'))

# All weights will be added to a list called all_weights, then will be outputted
all_weights = [weight_1, weight_2, weight_3, weight_4]
print(f'Weights: {all_weights}\n')

# Average of all weights will have two digits after the decimal, and be in a variable called avg_weight
# Conversion specifier used to specify printing two digits after the decimal point
avg_weight = (weight_1 + weight_2 + weight_3 + weight_4) / 4
print('Average weight: {:.2f}'.format(avg_weight))
