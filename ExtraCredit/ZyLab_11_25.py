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

# Max element will be initialized a variable called max_weight, which will be at index 0
# Conversion specifier used to specify printing two digits after the decimal point
max_weight = all_weights[0]

# for loop will search each weight in all_weights
for weight in all_weights:

    # if statement will determine if a weight is greater than the initialized max_weight
    if weight > max_weight:
        max_weight = weight

# Print the max weight
print('Max weight: {:.2f}'.format(max_weight))

# Prompt the user for a number between 1 and 4, which will be the user specified location
location = int(input('Enter a list location (1 - 4):\n'))

# if-elif statements will output the inputted location along with their respective weights in pounds and kilograms
# 1 kilogram is equal to 2.2 pounds.
if location == 1:
    kilo_weight_1 = all_weights[0] / 2.2
    print('Weight in pounds: {:.2f}'.format(all_weights[0]))
    print('Weight in pounds: {:.2f}'.format(kilo_weight_1))
elif location == 2:
    kilo_weight_2 = all_weights[1] / 2.2
    print('Weight in pounds: {:.2f}'.format(all_weights[1]))
    print('Weight in pounds: {:.2f}'.format(kilo_weight_2))
elif location == 3:
    kilo_weight_3 = all_weights[2] / 2.2
    print('Weight in pounds: {:.2f}'.format(all_weights[2]))
    print('Weight in pounds: {:.2f}'.format(kilo_weight_3))
elif location == 4:
    kilo_weight_4 = all_weights[3] / 2.2
    print('Weight in pounds: {:.2f}'.format(all_weights[3]))
    print('Weight in pounds: {:.2f}'.format(kilo_weight_4))

# Sort the weights in  the list all_weights from lightest to heaviest weight and print the sorted list
all_weights.sort()
print(f'Sorted list: {all_weights}')
