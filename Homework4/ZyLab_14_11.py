# Nathan Galdamez Gomez, 2141118
# This is ZyLab 14.11

# A function called selection_sort_descend_trace
def selection_sort_descend_trace():
  # Map inputted numbers into a list called nums
  nums = []
  nums = [int(num) for num in input('').split()]
  
  # Iterate through each element called i in len(nums) - 1 in for loop
  for i in range(len(nums) - 1):
    
    # Maximum index will be assigned to i
    maximum = i
    
    # for loop will find the index of the maximum value
    for j in range(i+1, len(nums)):
      # Next index will be the new maximum IF j > maximum
      if int(nums[j]) > int(nums[maximum]):
        maximum = j
      
    # Swap each iteration of indexes with maximum index in an integer list
    nums[i], nums[maximum] = nums[maximum], nums[i]
      
    # Output the list of numbers in nums with a for loop then print a new line
    for maximum in nums:
      print(maximum, end=' ')
    print()
    
  # Return the list called nums
  return nums
      
# Main driver code calling selection_sort_descend_trace function to execute program
if __name__ == '__main__':
  selection_sort_descend_trace()
