g = [1, 2, 3]
s = [1, 1]

g = g.sort()

s = s.sort()
child = 0
for i in range(len(g)+1):
    for j in range(len(s)):
        if i > j or i == j:
            child += 1
        
print(child)