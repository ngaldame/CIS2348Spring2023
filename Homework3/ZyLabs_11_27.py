# Nathan Galdamez Gomez, 2141118

# A definition called rosterOutput
def rosterOutput():
    # Keys from athletes dictionary will be sorted
    keys = list(athletes.keys())
    keys.sort()
    
    print('ROSTER')
    # Print each athlete's attributes
    for key in keys:
        print(f'Jersey number: {key}, Rating: {athletes[key]}')
    
    
# Empty dictionary called athletes
athletes = {}

# for loop will print 5 athletes' attributes
for i in range(5):
    jersey = input(f'Enter player {i+1}\'s jersey number: \n')
    athletes[jersey] = input(f'Enter player {i+1}\'s rating: \n')
    print('\n')
    
rosterOutput()

# Print menu and input a menu option in while loop
while True:
    print('a - Add player\nd - Remove player\nu - Update player rating\n', end='')
    print('r - Output players above a rating\no - Output roster\nq - Quit')
    choice = input('Choose an option: ')
    
    # Print roster if choice is o
    if choice == 'o':
        rosterOutput()
    
    
