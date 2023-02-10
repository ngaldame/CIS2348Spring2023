# Nathan Galdamez Gomez, ngaldame
# This is ZyLab 5.22

# Create variables and print the services and their prices
totalPrice = 0
print('Davy\'s auto shop services')
print('Oil change -- $35\nTire rotation -- $19\nCar wash -- $7\nCar wax -- $12')
firstService = input('\nSelect first service:\n')
secondService = input('Select second service:\n')
print('\nDavy\'s auto shop invoice')
# if and else if statements for each service or '--'
if firstService == 'Oil change':
    totalPrice += 35
    print('\nService 1: Oil change, $35')
elif firstService == 'Tire rotation':
    totalPrice += 19
    print('\nService 1: Tire rotation, $19')
elif firstService == 'Car wash':
    totalPrice += 7
    print('\nService 1: Car wash, $7')
elif firstService == 'Car wax':
    totalPrice += 12
    print('\nService 1: Car wax, $12')
elif firstService == '-':
    print('\nService 1: No service')

if secondService == 'Oil change':
    totalPrice += 35
    print('Service 2: Oil change, $35')
elif secondService == 'Tire rotation':
    totalPrice += 19
    print('Service 2: Tire rotation, $19')
elif secondService == 'Car wash':
    totalPrice += 7
    print('Service 2: Car wash, $7')
elif secondService == 'Car wax':
    totalPrice += 12
    print('Service 2: Car wax, $12')
elif secondService == '-':
    print('Service 2: No service')
# Print the user inputs and the total price of both services
print(f'Total: ${totalPrice}')
