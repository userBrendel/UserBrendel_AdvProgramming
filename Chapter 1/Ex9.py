#INTEGERS LIST
#USING DIFFERENT APPROACH WITH LIST



# Creating an int list with 10 values
int_list = [5, 9, 4, 100, 3, 9, 11, 7, 1, 10]

# Output of the list using a for loop
print("My integer list output:")
for num in int_list: # num = items in the list.
    print(num, end=" ") # printing num with space.
print("\n")# New line for next approach

# Output of the highest and lowest value
print("Highest value:", max(int_list)) # printing with statement and printing the highest number in the list wit 'max' (100)
print("Lowest value:", min(int_list))  # printing with statement and printing the highest number in the list wit 'min' (1)
print() # New line for next approach

# Sorting the elements in ascending order
int_list.sort() # First i sort the list with '.sort' || sort is to fix the list to lowest to highest
print("Sorted in ascending order:", int_list) # This will print the sorted list. 
print() 
# Sorting the elements in descending order
int_list.sort(reverse=True) # Same approach, but this time 'reverse=true.' (highest to lowest)
print("Sorted in descending order:", int_list)
print()

# Appending two elements (adding items to the list)
int_list.append(15)
int_list.append(4)

# Printing after appending (will show at the last portion of the list)
print("List after appending two elements:", int_list)
