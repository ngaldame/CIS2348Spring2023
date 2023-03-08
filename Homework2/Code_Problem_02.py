# Nathan Galdamez Gomez, 2141118
# This is Coding Problem 2

# The below code is for Part A

# Use import datetime module and create an empty array to store input dates later
from datetime import datetime

dates = []

# Get the date as an input called day and stop the while loop if input is -1
while not False:
    date = input()
    if date == '-1':
        break
    # Try and except statement since if-elif-else statements gave me errors for wrong input
    try:
        # Either convert input date to the correct format OR output an error message
        date_holder = datetime.strptime(date, '%B %d, %Y')
        today = datetime.now()

        # Print if today is the greater value
        # I used # for removing leading 0s on Windows
        if date_holder <= today:
            print(date_holder.strftime('%#m/%#d/%Y'))
    except ValueError:
        pass
