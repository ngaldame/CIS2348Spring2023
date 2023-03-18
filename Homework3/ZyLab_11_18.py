# Nathan Galdamez Gomez, 2141118
# This is ZyLab 11.18

# Get input for nums, then split nums into a variable named ns
nums = input()
ns = nums.split()
# Make an empty array called num_list
num_list = []

# for loop to search each number in ns
for n in ns:
    # if statement will append n in num_list if n > 0
    if int(n) > 0:
        num_list.append(int(n))

# Sort the list
num_list.sort()

# print each number in num_list on one single line
for num in num_list:
    print(num, end=' ')
