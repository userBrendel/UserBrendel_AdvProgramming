#READING TO A LIST
# opening file and setting it as file
with open("Chapter 4/numbers.txt", "r") as file:
    strings_num = file.readlines()  # Reading all lines from the file that consist of strings
    numbers = [int(num.strip()) for num in strings_num] # Converting each string element in the list to an integer 

    # Iterating using 'for' 'in' over the list of numbers to print each one
    for number in numbers:
        print(number)



