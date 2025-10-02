# wap to take a tuple of numbers from the keyboard and print its sum and average? use eval function to
#take input.
# Take a tuple of numbers as input using eval
t = eval(input("Enter a tuple of numbers: "))

# Print the tuple
for i in t:
    print(i, end=" ")

# Calculate and print the sum and average
print("\nSum:", sum(t))
print("Average:", sum(t) / len(t))
