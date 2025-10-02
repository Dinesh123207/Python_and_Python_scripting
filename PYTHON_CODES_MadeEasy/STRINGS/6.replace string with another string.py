s="ababababaabaababaabaabababababbabbabababa"
s1=s.replace("a","b")
print(s1)
print(id(s))
print(id(s1))
# string objects are immutable then how we can change the content by using replace() method
# using id  function on both s and s1 then check the address of both , its different
