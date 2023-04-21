# Nathan Galdamez Gomez, 2141118
# This is ZyLab 14.11

# A function called selection_sort_descend_trace
def selection_sort_descend_trace():
  # Map inputted numbers into a list
  nums = list(map(int, input().split(' ')))
  
  # Iterate through each element called i in len(nums) - 1 in for loop
  for i in range(len(nums) - 1):
    
    # Maximum index will be assigned to i
    maximum = i
    
    # for loop will find the index of the maximum value
    for j in range(i+1, len(nums)):
      # Next index will be the new maximum IF j > maximum
      if int(nums[j]) > int(nums[maximum]):
        maximum = j
      # TODO: Swap each iteration of indexes in an integer list
