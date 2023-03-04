# Nathan Galdamez Gomez, 2141118
# This is ZyLab 7.25

# The function below uses floor division in order to return accurate change
def exact_change(user_total):
    # dols is for dollars, quarts is for quarters, dimes is for dimes
    # nicks is for nickels, and penns is for pennies
    dols = user_total // 100
    user_total %= 100

    quarts = user_total // 25
    user_total %= 25

    dimes = user_total // 10
    user_total %= 10

    nicks = user_total // 5
    user_total %= 5

    penns = user_total

    return dols, quarts, dimes, nicks, penns


# Below conditional statement will control the program's execution
if __name__ == '__main__':
    # Get input from the user
    input_val = int(input())

    # if else statement will check if there is change or no change
    if input_val <= 0:
        print('no change')
    # Return change and coins if going to else statement block
    else:
        num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(input_val)

        # Print each coin type needed
        if num_dollars > 0:
            if num_dollars == 1:
                print(f'{num_dollars} dollar')
            else:
                print(f'{num_dollars} dollars')

        if num_quarters > 0:
            if num_quarters == 1:
                print(f'{num_quarters} quarter')
            else:
                print(f'{num_quarters} quarters')

        if num_dimes > 0:
            if num_dimes == 1:
                print(f'{num_dimes} dime')
            else:
                print(f'{num_dimes} dimes')

        if num_nickels > 0:
            if num_nickels == 1:
                print(f'{num_nickels} nickel')
            else:
                print(f'{num_nickels} nickels')

        if num_pennies > 0:
            if num_pennies == 1:
                print(f'{num_pennies} penny')
            else:
                print(f'{num_pennies} pennies')
