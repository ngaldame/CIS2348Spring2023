# Nathan Galdamez Gomez, 2141118
# This is ZyLab 12.7

# get_age function will get an input age between 18 and 75, or throw a ValueError
def get_age():
    person_age = int(input())

    if 18 <= person_age <= 75:
        return person_age
    else:
        raise ValueError('Invalid age.')


# fat_burning_heart_rate function will calculate and return the fat burning heart rate
def fat_burning_heart_rate(person_age):
    # Equation for fat burning heart rate below (.7 is the same as 70%)
    rate_heart = (220 - person_age) * .7
    return rate_heart


# The main driver code is below
if __name__ == '__main__':

    # Try and except statement will determine if input is valid or not
    try:
        age = get_age()
        heart_rate = fat_burning_heart_rate(age)
        print(f'Fat burning heart rate for a {age} year-old: {heart_rate} bpm')
    except ValueError as ex:
        print(ex)
        print('Could not calculate heart rate info.\n')
