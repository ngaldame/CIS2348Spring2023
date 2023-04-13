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
    
    # Get next line
    parts = input.split()
    name = parts[0]
    
  # TODO: Finish except ValueError statement
  except ValueError as ex:
