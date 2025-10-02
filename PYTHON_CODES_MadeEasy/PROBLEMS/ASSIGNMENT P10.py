# wap to display sum of first n natural numbers, take n value as input from keyboard:
# Taking input from the user
#n = int(input("Enter the value of n: "))
n = 20
# Initialize variables
total = 0
i = 1

# Using while loop to calculate the sum
while i <= n:
    total += i
    i += 1

# Display the result
print(f"The sum of the first {n} natural numbers is: {total}")
