# Nathan Galdamez Gomez, 2141118
# This is ZyLab 6.17

# Get input for a password
password = str(input())

# Change i to !, a to @, m to M, B to 8, and o to . by using an if else statement in the for loop
for character in password:
    if character == 'm' or character == 'a' or character == 'o' or character == 'i' or character == 'B':
        password = password.replace('m', 'M')
        password = password.replace('a', '@')
        password = password.replace('o', '.')
        password = password.replace('i', '!')
        password = password.replace('B', '8')

# password will have 'q*s' printed no matter what and password will be printed with changes or no changes
password = password + 'q*s'
print(f'{password}')
