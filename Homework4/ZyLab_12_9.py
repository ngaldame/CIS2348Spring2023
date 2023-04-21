# Nathan Galdamez Gomez, 2141118
# This is ZyLab 12.9

# Split input into 2 parts: name and age
parts = input().split()
name = parts[0]

# age is below
age = parts[1]

while name != '-1':
  try:
    age = int(parts[1]) + 1
    print(f'{name} {age}')
    
  # ValueError exception will output 0, which will be the exception value of the age
  except ValueError as ex:
    print('{} {}'.format(name, 0))
    
  # Get next line as long as name != '-1'
  parts = input().split()
  name = parts[0]
