s = "loveleetcode"
d = list(s)
s1 = []
for index, i in enumerate(s):
    if s.count(i) == 1:
        print(index, i, sep=":")
        break