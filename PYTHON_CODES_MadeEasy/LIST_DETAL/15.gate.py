x = range(5)
squares = [0,1,4,9,16,25] 
result =0
for i in squares:
    if i >5:
        result +=i
        break
    result += i

else:
    result +=10
print(result)