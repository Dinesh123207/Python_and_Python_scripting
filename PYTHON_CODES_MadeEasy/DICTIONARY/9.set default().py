# d ={100:"durga",200:"ravi",300:"shiva"}
# print(d.setdefault(100,"suhail"))
# print(d.setdefault(200,"Ishita"))
# print(d)
# #use gfg
d = {1: 'one', 2: 'two', 3: 'three'}
value = d.setdefault(2, 'default_value')  # Key 2 exists
print("Returned value:", value)
print("Updated dictionary:", d)
