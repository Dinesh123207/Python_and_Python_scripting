s = "ABCABCBBCDEFFFEEBEEEACABCDEFABCDEF"
t = s.split( )
print(t)
i =0
for i in range(len(t)):
    for j in range(len(t)):
     if t[i] ==t[j]:
    
        
        
     else:
       print(t[i], end = " ")