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

# TODO: Write the quicksort algorithm that recursively sorts the low and
#       high partitions. Add 1 to num_calls each time quicksort() is called
def quicksort(user_ids, i, k):
