n=4
result =1
for i in range(1,n+1):
    for j in range(i,0,-1):
        result *= j
    result //=i
    print(result)
print(result)        

######################3
#Walkthrough:
# Let's go through the loop iteration by iteration:

# First iteration (i = 1):

# Inner loop (j = 1):
# result = 1 * 1 = 1
# After the inner loop: result //= 1 → result = 1
# Prints: 1
# Second iteration (i = 2):

# Inner loop (j = 2, 1):
# result = 1 * 2 = 2
# result = 2 * 1 = 2
# After the inner loop: result //= 2 → result = 1
# Prints: 1
# Third iteration (i = 3):

# Inner loop (j = 3, 2, 1):
# result = 1 * 3 = 3
# result = 3 * 2 = 6
# result = 6 * 1 = 6
# After the inner loop: result //= 3 → result = 2
# Prints: 2
# Fourth iteration (i = 4):

# Inner loop (j = 4, 3, 2, 1):
# result = 2 * 4 = 8
# result = 8 * 3 = 24
# result = 24 * 2 = 48
# result = 48 * 1 = 48
# After the inner loop: result //= 4 → result = 12
# Prints: 12
#Final output:
#The final value of result after all the iterations is 12.