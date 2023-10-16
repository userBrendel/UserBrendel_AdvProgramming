#defining a variable for the first answer
answer1 = str(input("What shape do you want to calculate:\n(t)riangle\n(r)ectangle\n(c)ircle\n"))#first choice the user has to make.

if answer1 == "t": #if the first answer is equal to t then:
    #defining a variable for the second answer
    answer2 = str(input("\nWhat do you want to calculate:\n(a)rea\n(c)ircumference\n"))#user has to make another choice
    if answer2 == "a": #if second answer is a then:
      #asking user for base and height enable to calculate the are of a triangle -- defining a variable for base and height to be used in calculation area formula
        b = float(input("\nEnter the base of the triangle:"))
        h = float(input("Enter the height of the triangle:"))
        area = (1/2) * b * h #formula/ calculation / defining area to be printed later on
        print("\nThe area of the triangle is:", area) #will show the calculated result

#SAME METHOD TO BE APPLIED AS FORE THE FOLLOWING
#A CHANGE OF FORMULAS
    elif answer2 == "c":#if second answer is c then:
        a1 = float(input("\nEnter the length of the 1st side of the triangle:"))
        a2 = float(input("Enter the length of the 2nd side of the triangle:"))
        a3 = float(input("Enter the length of the 3rd side of the triangle:"))
        cir = a1 + a2 + a3
        print("\nThe circumference of the triangle is:", cir)
    else:#if second answer is not a/c then:
        print("Invalid")


elif answer1 == "r": #if the first answer is equal to r then:
    answer2 = str(input("\nWhat do you want to calculate:\n(a)rea\n(c)ircumference\n"))
    if answer2 == "a":
        length = float(input("\nEnter the length of the rectangle:"))
        width = float(input("Enter the width of the rectangle:"))
        area = length * width
        print("\nThe area of the rectangle is:", area)
    elif answer2 == "c":
        length = float(input("\nEnter the length of the rectangle:"))
        width = float(input("Enter the width of the rectangle:"))
        cir = 2 * (length + width)
        print("\nThe circumference of the rectangle is:", cir)
    else:
        print("Invalid")

elif answer1 == "c": #if the first answer is equal to c then:
    answer2 =  str(input("\nWhat do you want to calculate:\n(a)rea\n(c)ircumference\n"))
    if answer2 == "a":
        radius = float(input("\nEnter the radius of the circle:"))
        area =3.14 * radius**2
        print("The area of the circle is:", area)
    elif answer2  == "c":
        radius = float(input("\nEnter the radius of the circle:"))
        cir= 2 * 3.14 * radius
        print("The circumference of the circle is:", cir)
    else:
        print("Invalid")


else: #if the first answer is something else than t/r/c then:
  print("\nEnter t/r/c only. Try again")
