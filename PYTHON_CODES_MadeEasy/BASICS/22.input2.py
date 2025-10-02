numbers =[int(x) for x in input("enter any number of values").split()] # it takes multiple inputs from user in a single line separated by space and stores them in a list after converting them into integers.
print(type(numbers))
for x in numbers:
    print(x) 