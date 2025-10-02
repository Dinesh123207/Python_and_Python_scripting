#wap to create 3 different dictionaries and concatenate /merge them into 4 th dictionary

d1 = {1: "dinesh", 2: "ram", 3: "Sohan"}
d2 = {'b': 3, 'c': 4}
d3 = {100: "durga", 200: "ravi", 300: "shiva"}
d4 = {}

# Merging all dictionaries into d4
d4.update(d1)
d4.update(d2)
d4.update(d3)

print(d4)
