# squares ={x:x*x for x in range(1,6)}
# print(squares)
# doubles ={x:2*x for x in range(1,6)}
# print(doubles)
numbers = [1, 2, 3, 4, 5]

# Creating a dictionary where the key is the number and the value is the square of the number
squares = {num: num**2 for num in numbers}

print(squares)
# Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
