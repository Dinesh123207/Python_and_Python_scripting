s = {1,2,3,4,5,6}
fs = frozenset(s)
print(type(fs))
s.append(5) # it shows error because frozenset is immutable ie items cant be added or removed.
print(fs)