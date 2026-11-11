c = "G()(al)"

for i in range(len(c)):
    if  "G" in c[i]:
        continue
    elif "()" in c:
        "()".replace("()","o")
    elif "(al)" in c:
        "(al)".replace("(al)","al")


print(c)