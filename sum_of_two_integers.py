a = 2
b = 3

c = bin(a)[2:]
d = bin(b)[2:]

binary = c & d

result = int(binary,2)

print(result)