#reverse order of words
s = "learning python is very easy"
t = s.split()
# t.reverse()
# print(' '.join(t))  # Output: easy very is python learning
u = []
i = len(t)-1
while i >= 0:
    u.append(t[i])
    i -= 1

print('  '.join(u))
 