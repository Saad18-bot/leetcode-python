s = "abc"
t = "ahbgdc"

found = True
start = 0

for s1 in s:

    match = False

    for i in range(start, len(t)):

        if s1 == t[i]:
            match = True
            start = i + 1
            break

    if not match:
        found = False
        break

print(found)