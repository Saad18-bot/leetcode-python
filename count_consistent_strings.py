allowed = "ab"
words = ["ad", "bd", "aaab", "baa", "badab"]

count = 0

for word in words:

    consistent = True

    for char in word:
        if char not in allowed:
            consistent = False
            break

    if consistent:

        count += 1


print(count)