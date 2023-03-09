# Nathan Galdamez Gomez, 2141118
# This is Coding Problem 2

# The below code is for Part C

# Use import datetime module
from datetime import datetime

# Empty array from Part A below is not needed, so it will become a comment
# dates = []

# Read all dates from inputDates.txt in order to read every single line
# Then write correctly formatted dates into parsedDates.txt
with open('inputDates.txt', 'r') as file:
    with open('parsedDates.txt', 'w') as output:
        for single_line in file:
            # Remove whitespace in each line and break if date == -1
            date = single_line.strip()
            if date == '-1':
                break

            # Try and except statement since if-elif-else statements gave me errors for wrong input
            try:
                # Either convert input date to the correct format OR output an error message
                date_holder = datetime.strptime(date, '%B %d, %Y')
                today = datetime.now()

            # Print if today is the equal or greater value
            # I used # for removing leading 0s on Windows, - is for other OSs
                if date_holder <= today:
                    output.write(date_holder.strftime('%#m/%#d/%Y') + '\n')

            # Pass if the input is not '-1' and is not correctly formatted
            except ValueError:
                pass
