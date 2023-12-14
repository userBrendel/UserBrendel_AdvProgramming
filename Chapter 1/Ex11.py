#YEAR TUPLES

# Given tuple:
year = (2017, 2003, 2011, 2005, 1987, 2009, 2020, 2018, 2009)

# Accessing the tuple item at index -3 (2020)
# Variable that is equals to the tuples 'year' with [-3]. This gets the 3rd to the last item in the tuple(2020).
index_n3 = year[-3]
print(f"Tuple index -3: {index_n3}") #Printing statement and the variable

# Reversing the tuple and printing the original tuple and reversed tuple
print(f"Original Tuple: {year}") # Original tuple. 

#(2009, 2018, 2020, 2009, 1987, 2005, 2011, 2003, 2017)
rev_year = tuple(reversed(year)) # A variable for reversed approach.
print(f"Reversed Tuple: {rev_year}")

# Counting the number of times 2009 is in the tuple (2)
count_2009 = year.count(2009) # Using '.count' to count how many times 2009 is in tuple.
print(f"Number of times 2009 is in the tuple: {count_2009}")

# Getting the index value of 2018 (7) || index starts with 0
index_2018 = year.index(2018) # Using '.index' to find the index/place of 2018.
print(f"Index value of 2018: {index_2018}")

# Finding the length of the given tuple (9)
length_year = len(year) # Using len to get the length/ amount of items in the 'year' tuple.
print(f"Length of the tuple: {length_year}")
