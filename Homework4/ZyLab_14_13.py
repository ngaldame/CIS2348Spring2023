# Nathan Galdamez Gomez, 2141118
# This is ZyLab 14.13

# Global variable
num_calls = 0


# A function called partition will contain the partitioning algorithm
def partition(user_ids, i, k):
    # The middle element in the array will be the pivot, which will be a variable called focus
    focus = user_ids[(i + k) // 2]

    # Values being compared in the array will be called low and h
    # low and h are the index variables to the left and right of the current elements being sorted
    low = i - 1
    h = k + 1

    # The nested while loops will compare both the low and high index variables to the input
    while True:
        low = low + 1

        while user_ids[low] < focus:
            low = low + 1

        h = h - 1

        while user_ids[h] > focus:
            h = h - 1

        if low >= h:
            return h

        # Swap the elements if the element left of the pivot is larger than the element right of the pivot
        user_ids[low], user_ids[h] = user_ids[h], user_ids[low]


# quicksort algorithm recursively sorts the low and high partitions. Add 1 to num_calls each time quicksort() is called
def quicksort(user_ids, i, k):
    # Reference the num_calls variable by using global and increment num_calls by 1
    global num_calls
    num_calls = num_calls + 1

    # if statement below will recursively sort the low and high partitions
    if i < k:
        # split index found by calling partition in next line of code
        seperate = partition(user_ids, i, k)

        # Both sides of the subarray will be called recursively
        quicksort(user_ids, i, seperate)
        quicksort(user_ids, seperate + 1, k)


# Finish main driver code
if __name__ == '__main__':

    # user IDs will be in an input variable called user_ident and stored into an array called user_idents
    user_idents = []
    user_ident = input()

    # while loop will append input into the array
    while user_ident != '-1':
        user_idents.append(user_ident)
        user_ident = input()

    # Initial call to quicksort
    quicksort(user_idents, 0, len(user_idents) - 1)

    # Print number of calls to quicksort
    print(num_calls)

    # Print sorted user ids
    for user_ident in user_idents:
        print(user_ident)
