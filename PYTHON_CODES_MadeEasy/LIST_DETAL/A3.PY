#wap to add all elements of list upto 100 using append function which are divisible by 10.
#hint:use append, range, for, if condition
# l = [10,20,30,40,50,60,70,80,90,100,110,120,130,140]
# t =[]
# sum =0
# for i in range(1, 101):
    
#     if i%10 ==0:
#         print(i, end =" ")

#     sum = sum +i
#     t.append(sum)
#     print(t)

l = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140]
t = []  # Empty list to store numbers divisible by 10
sum = 0  # To store the sum of numbers divisible by 10

# Loop through the list 'l'
for i in l:
    if i % 10 == 0 and i <= 100:  # Check if the number is divisible by 10 and less than or equal to 100
        t.append(i)  # Append to list 't'
        sum += i  # Add the number to 'sum'

print("List of numbers divisible by 10 and up to 100:", t)
print("Sum of these numbers:", sum)
