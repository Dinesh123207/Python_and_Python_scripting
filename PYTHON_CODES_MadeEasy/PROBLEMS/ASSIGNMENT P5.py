#*
#**
#***
#****
#*****
#******

for i in range(0, 5):  # Outer loop to control the number of rows (5 rows)
    print()  # Moves to the next line
    for j in range(0, i+1):  # Inner loop to print stars for each row
        print("*", end="")  # Prints stars without a newline
