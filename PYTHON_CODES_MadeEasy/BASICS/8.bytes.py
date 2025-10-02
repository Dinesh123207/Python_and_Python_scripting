x=[10,20,30,40,50,255]#256#] # it is used to represent binary data.
b = bytes(x)
print(type(b))
print(b[0])
print(b[-1])
for i in b:
    print(i) 