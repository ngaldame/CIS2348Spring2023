# Nathan Galdamez Gomez

print('Birthday Calculator\n')
print('Enter the current date in this order: month, day, and year.')
current_month = int(input('Current Month: '))
current_day = int(input('Current Day: '))
current_year = int(input('Current Year: '))
print('Enter your birthday in this order: month, day, and year.')
birth_month = int(input('Birth Month: '))
birth_day = int(input('Birth Day: '))
birth_year = int(input('Birth Year: '))

yearAge = current_year - birth_year
monthAge = current_month - birth_month
dayAge = current_day - birth_day

if current_month == birth_month and current_day == birth_day:
    print('Happy Birthday!')
# Do non-birthday code later
