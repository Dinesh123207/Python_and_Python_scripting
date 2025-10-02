# Reading input from the user using eval
numbers = eval(input("Enter a list of 10 to 20 numbers: "))

# Check if the number of elements is between 10 and 20
if 10 <= len(numbers) <= 20:
    # Iterate and print each element with its index
    for index, number in enumerate(numbers):
        print(f"Index {index}: {number}")
else:
    print("The list should contain between 10 and 20 numbers.")
