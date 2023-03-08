# Nathan Galdamez Gomez, 2141118
# This is Coding Problem 2

# The below code is for Part B

# Use import datetime module
from datetime import datetime

# Empty array from Part A below is not needed, so it will become a comment
# dates = []

# Read all dates from inputDates.txt in order to read every single line
with open('inputDates.txt', 'r') as file:
    for single_line in file:
        # Remove whitespace in each line
        date = single_line.strip()
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
