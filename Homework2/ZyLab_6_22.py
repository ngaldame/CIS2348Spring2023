# Nathan Galdamez Gomez, ngaldame
# This is ZyLab 6.22

# Input 2 x values, 2 y values, and 2 z values
a_initial = int(input())
b_initial = int(input())
c_initial = int(input())
a_final = int(input())
b_final = int(input())
c_final = int(input())

# Set a boolean called check to False automatically
xFinal = 0
yFinal = 0
check = False
# The brute force approach will set check to True only if there is a solution
for x in range(-10, 11):
    for y in range(-10, 11):
        if a_initial * x + b_initial * y == c_initial and a_final * x + b_final * y == c_final:
            xFinal = x
            yFinal = y
            check = True

# if not statement is used in order to get rid of PyCharm warnings and simplify the code
if not check:
    print('No solution')
else:
    print(xFinal, yFinal)
