x=[10,20,30,40,50]

ba = bytearray(x)
print(type(ba))
ba[0] = 11
for i in ba:
    print(i)

    