# Initialize an empty list to store the elements
divisible_by_10 = []

# Iterate over the range from 1 to 100
for num in range(1, 101):
    # Check if the number is divisible by 10
    if num % 10 == 0:
        # Append the number to the list
        divisible_by_10.append(num)

# Print the list of numbers divisible by 10
print("Numbers divisible by 10:", divisible_by_10)

# Calculate and print the sum of the elements in the list
sum_of_elements = sum(divisible_by_10)
print("Sum of elements:", sum_of_elements)
