#remove duplicates from list:
l =[1,2,3,4,5,6,7,8,9,9,8,7,6,5,4,3,2,1,4,5]
l.sort()
print(l)
i=0
for i in l:
    if l[i]==l[i+1]:
        l.remove(l[i])
        i =i+1
print(l, end =" ")