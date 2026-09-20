s = "abccccdd"

count = 0
odd = False

for char in set(s):

    if s.count(char) % 2 == 0:
        count += s.count(char)
    else:
        count += s.count(char) - 1
        odd = True

if odd:
    count += 1

print(count)
