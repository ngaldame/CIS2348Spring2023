# Nathan Galdamez Gomez, 2141118

print('\nBirthday Calculator')
print('Current day')
current_month = int(input('Month: '))
current_day = int(input('Day: '))
current_year = int(input('Year: '))
print('Birthday')
birth_month = int(input('Month: '))
birth_day = int(input('Day: '))
birth_year = int(input('Year: '))

# Create variables to get a user's age
yearAge = current_year - birth_year
monthAge = current_month - birth_month
dayAge = current_day - birth_day

# If statement prints 'Happy Birthday!' and increment yearAge by 1
if current_month == birth_month and current_day == birth_day:
    print('Happy Birthday!')
    yearAge += 1
# elif statement will print age before birthday
elif current_month <= birth_month and current_day < birth_day:
    yearAge -= 1
    print(f'You are {yearAge} years old.')
# elif statement will print current age
elif current_month >= birth_month and current_day >= birth_day:
    print(f'You are {yearAge} years old.')
