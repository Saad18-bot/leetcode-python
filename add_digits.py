n = input("Enter a number: ")

while len(n) > 1:

    total = 0

    for digit in n:
        total += int(digit)

    n = str(total)

print(n)