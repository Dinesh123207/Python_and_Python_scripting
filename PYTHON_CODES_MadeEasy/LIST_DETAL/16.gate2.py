a=0
b=1
list = []
for i in range(6):
    a,b = b, a+b
    list.append(a)
    print(sum(x for x in list if x%2==0))
    