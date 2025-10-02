# Sample dictionary with unordered keys
d = {3: "Sohan", 1: "dinesh", 2: "ram", 100: "durga", 200: "ravi", 300: "shiva"}

# Sort the dictionary keys in ascending order
# The sorted() function returns a list of keys in ascending order
sorted_keys = sorted(d)

# Iterate over the sorted keys
for key in sorted_keys:
    # Print each key and its corresponding value from the dictionary
    # d[key] accesses the value associated with the key in the dictionary
    print(f"{key}: {d[key]}")
