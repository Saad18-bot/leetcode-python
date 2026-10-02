n = 19

seen = set()

while n != 1:

    if n in seen:
        print(False)
        break

    seen.add(n)

    total = 0

    for digit in str(n):
        total += int(digit) ** 2

    n = total

else:
    print(True)
    