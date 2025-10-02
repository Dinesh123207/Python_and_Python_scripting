i=1
j=1
for i in range(1,11):
    if(i%3 !=0):
        j+=2
        continue
    if(j%3 ==0):
        break


print(i+j)


for i in range(9,91):
    if i%9==0:
        print(i)