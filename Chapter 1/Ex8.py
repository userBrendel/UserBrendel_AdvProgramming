#PYRAMID PATTERN NUMBERS

# Number of rows in the pattern
rows = 5

#NESTED LOOP: LOOP INSIDE A LOOP

# Outer loop (Rows)
for out in range(1, rows + 1):  # (1, 5 + 1) or 1 to 5. Range starts with zero therefore i added 1 to iterate 1 to 5 rows.
    
    # Inner loop (Columns)
    for inner in range(1, out + 1):  # Generates each column in the current row (from 1 to the current row number).
        # For example, in row 1, it generates column 1. In row 2, it generates columns 1 and 2, and so on.
        
        # In the inner loop, the current value of 'inner' will print.
        print(inner, end=" ") 
        # Printing the current number. end=" " ensures that the numbers are printed with a space, so they appear horizontally.

# Once the inner loop is complete for the current row, the outer loop will be make the next row, creating a new line/row in the pattern.
    print()


