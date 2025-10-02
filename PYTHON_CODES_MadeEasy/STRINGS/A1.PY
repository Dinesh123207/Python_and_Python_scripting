# Define the input string
d = "dronacharya"

# Print each character in forward direction
print("Forward direction:")
i = 0
while i < len(d):
    print(d[i] , end = " ")
    i += 1
    

# Print each character in backward direction
print("Backward direction:")
i = len(d) - 1
while i >= 0:
    print(d[i], end = " ")
    i -= 1
