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
    # Add a new player's attributes and add them to the athletes dictionary if choice is a
    elif choice == 'a':
        jersey = input('Enter a new player's jersey number:\n')
        rate = input('Enter the player's rating:\n')
        athletes[jersey] = rate
    # Delete a player from the roster and dictionary if choice is d
    elif choice == 'd':
        jersey = input('Enter a player's jersey number:\n')
        del athletes[jersey]
    # Update a player's rating if choice is u
    elif choice == 'u':
        jersey = input('Enter a player's jersey number:\n')
        rate = input('Enter a new rating for player:\n')
        # athletes dictionary now contains updated player attributes
        athletes[jersey] = rate
    # Output players that have a rating above inputted rating if choice is r
    elif choice == 'r':
        rate = input('Enter a rating:\n')
        keys = list(athletes.keys())
        keys.sort()
        print(f'ABOVE {rate}')
        
        # a variable called tracker will keep track of the number of players
        tracker = 0
        for key in keys:
            # Print the attributes of the players
            if athletes[key] > rating:
                print(f'Jersey number: {key}, Rating: {players[key]}')
                
                # tracker will increment by 1
                tracker += 1
     
     # Quit if choice is q
     elif choice == 'q':
        break
