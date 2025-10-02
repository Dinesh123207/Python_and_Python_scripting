#wap to find maximum of three numbers using conditionals
a=10
b=int(input("enter second number"))
c=int(input("enter number 3"))
if a>b and a>c:
    print(a)
elif b>c and b>a:
    print(b)
else:
    print(c)    