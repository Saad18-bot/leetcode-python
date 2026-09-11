
strs = ["flower","flies","flow"]
prefix = ""
for i in range(len(strs)):
    for word in strs:
        if (i >= len(word) or word[i] != strs[0][i]):
            print(prefix)
            exit()

    prefix += strs[0][i]

print(prefix)

            