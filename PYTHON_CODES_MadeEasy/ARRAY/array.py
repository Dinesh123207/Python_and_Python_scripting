import array as a

# Create an array of integers
arr = a.array('i', [2, 4, 5, 6, 3, 9, 8])

# Convert array to list, sort the list, and convert back to array
arr_list = list(arr)
arr_list.sort()
arr = a.array('i', arr_list)

print(arr)
