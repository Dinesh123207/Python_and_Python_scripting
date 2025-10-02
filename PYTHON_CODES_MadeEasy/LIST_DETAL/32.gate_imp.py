data = [1,2,3]
for i in range(len(data)):
    x = data[i]
    for j in range(i+1, len(data)):
        y = data[j]
        if x+y == 4:
            print(x*y)

         #   Walkthrough:
#Let's go through the loop iterations step-by-step:

#First iteration (i = 0):

#x = data[0] = 1
#Inner loop starts from j = 1:
#y = data[1] = 2
#x + y = 1 + 2 = 3 (Condition x + y == 4 is False)
#Next, j = 2:
#y = data[2] = 3
#x + y = 1 + 3 = 4 (Condition x + y == 4 is True)
#x * y = 1 * 3 = 3 is printed.
#Second iteration (i = 1):

#x = data[1] = 2
#Inner loop starts from j = 2:
#y = data[2] = 3
#x + y = 2 + 3 = 5 (Condition x + y == 4 is False)
#Third iteration (i = 2):

#The inner loop doesn't run because there are no more elements after index 2.