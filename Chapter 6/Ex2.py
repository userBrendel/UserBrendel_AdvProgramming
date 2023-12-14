#NUMPY ARRAY
# Given list
a = [20, 23, 82, 40, 32, 15, 67, 52]

# indices of even numbers
# For each pair, if the value is even, it adds the corresponding index to the list.
even_indices = [index for index, value in enumerate(a) if value % 2 == 0]
print(f"Indices of even numbers: {even_indices}")

# Sorting the array
sorted_array = sorted(a) # sorted 'a' list 
print(f"Sorted array: {sorted_array}")# display sorted list/ ascending

# Slicing elements from index 3 to the end of the array
slice_1 = a[3:] # to create a slice list of a containing elements from index 3 to the end of the array
print(f"Sliced elements from index 3 to the end: {slice_1}")

# Slice elements from index 0 to index 4
slice_2 = a[0:5] # for containing elements from index 0 to index 4 in list 
print(f"Sliced elements from index 0 to index 4: {slice_2}")

# Negative slice
negative_slice = a[-5:-2] # containing elements from index -5 to index -2
print(f"Negative slicing to get [32, 15, 67]: {negative_slice}")
