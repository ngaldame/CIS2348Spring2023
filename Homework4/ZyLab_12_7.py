# Nathan Galdamez Gomez, 2141118
# This is ZyLab 12.7

# get_age function will get an input age between 18 and 75, or throw a ValueError
def get_age():
  age = int(input())
  
  if age >= 18 and age <= 75:
    return age
  else:
    raise ValueError('Invalid age')

# fat_burning_heart_rate function will calculate and return the fat burning heart rate
def fat_burning_heart_rate(age):
  # Equation for fat burning heart rate below (.7 is the same as 70%)
  heart_rate = (220 * .7) - age
  return heart_rate

# TODO: Make and finish main driver code
if __name__ == '__main__':
  # Finish main driver code
