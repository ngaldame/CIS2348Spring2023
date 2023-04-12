# Nathan Galdamez Gomez, 2141118
# This is ZyLab 12.7

# get_age function will get an input age between 18 and 75, or throw a ValueError
def get_age():
  age = int(input())
  
  if age >= 18 and age <= 75:
    return age
  else:
    raise ValueError('Invalid age')
