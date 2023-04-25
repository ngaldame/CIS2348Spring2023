# Nathan Galdamez Gomez, 2141118
# This is ZyLab 14.11

# A function called selection_sort_descend_trace with an argument named num_values
def selection_sort_descend_trace(num_values):

    # Iterate through each element called i in len(num_values) - 1 in for loop
    for i in range(len(num_values) - 1):

        # Maximum index will be assigned to i
        maximum = i

        # for loop will find the index of the maximum value
        for j in range(i + 1, len(num_values)):
            # Next index will be the new maximum IF j > maximum
            if int(num_values[j]) > int(num_values[maximum]):
                maximum = j

        # Swap each iteration of indexes with maximum index in an integer list
        num_values[i], num_values[maximum] = num_values[maximum], num_values[i]

        # Output the list of numbers in num_values with a for loop then print a new line regardless
        for maximum in num_values:
            print(maximum, end=' ')
        print()

    # Return the list called nums
    return num_values


# Main driver code calling selection_sort_descend_trace function to execute program
if __name__ == '__main__':
    # Map inputted numbers into a list called values
    values = [int(value) for value in input('').split()]

    # Call the function and pass values into the function
    selection_sort_descend_trace(values)
