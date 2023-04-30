# Nathan Galdamez Gomez, 2141118
# This is ZyLab 12.11

user_num = int(input())
div_num = int(input())

# try-except blocks below will find if input is valid or not
try:
    quotient = user_num / div_num
    print(int(quotient))

# except block for ZeroDivisionError is below
except ZeroDivisionError:
    print('Zero Division Exception: integer division or modulo by zero')

# TODO: except block for ValueError is below (needs fixing)
except ValueError:
    print(f'Input Exception: invalid literal for int() with base 10: \'{user_num}\'')
