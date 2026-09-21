s = "egg"
t = "add"

mapping1 = {}
mapping2 = {}

for i in range(len(s)):

    if s[i] in mapping1 and mapping1[s[i]] != t[i]:
        print(False)
        break

    if t[i] in mapping2 and mapping2[t[i]] != s[i]:
        print(False)
        break

    mapping1[s[i]] = t[i]
    mapping2[t[i]] = s[i]

else:
    print(True)