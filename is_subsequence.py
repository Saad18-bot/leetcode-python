s = "abc"
t = "ahbgdc"
found = False
d = ""
for s1 in s:

    for t1 in t:

        if s1 == t1 :

            d.append(s1)
            found = True
            break

    if found:
        print(True)
        print(d)
        break

if not found:
    print("Is Not A Subsequence")