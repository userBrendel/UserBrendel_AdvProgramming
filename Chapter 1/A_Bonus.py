# Loop through tables from 1 to 10
for table_number in range(1, 11):
    print(f"Multiplication table of : {table_number}")
    
    # Loop through multipliers from 1 to 10
    for i in range(1, 11):
        result = table_number * i # multiplying the iteration value of 'table number' with 'i' iteration value
        print(f"{table_number} x {i} = {result}") # printing till the range iteration
    
    print("-------------")  # Separate each table with lines
