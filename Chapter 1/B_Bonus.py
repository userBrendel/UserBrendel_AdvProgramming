# Given list
locations = ['dubai', 'paris', 'switzerland', 'London', 'amsterdam', 'New York']

# Printing the original list and find its length
print("Original List:", locations)
print("Length of the list:", len(locations))

# Using sorted() to print the list in alphabetical order 
sorted_list = sorted(locations)
print("Sorted List (Alphabetical):", sorted_list)

# the original list is still in its original order because we use the variable of original list
print("Original List:", locations) 

# Using sorted(reverse=true) to print the list in reverse alphabetical order 
reverse_sorted_list = sorted(locations, reverse=True)
print("Sorted List (Reverse Alphabetical):", reverse_sorted_list)

# Showing that the original list is still in its original order
print("Original List:", locations)

# Using reverse() to reverse the position order of the original list
locations.reverse()
print("Reversed List:", locations)

# Using sort() to change the list so it's stored in alphabetical order
locations.sort()
print("Sorted List (Alphabetical):", locations)

# Using sort() to change the list so it's stored in reverse alphabetical order
locations.sort(reverse=True)
print("Sorted List (Reverse Alphabetical):", locations)
