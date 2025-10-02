#wap to print characters at even and odd position for the given string
s = "dronacharya"
# printing characters at even position
i =0
while i<= len(s):
    if i%2==0:
        print(s[i], end= " ")
    i+=1


#printing at the odd position
i=0
while i<=len(s):
 if i %3==0:
    
    print(s[i], end=" ")
    
 i +=1   
        