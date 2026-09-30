n_stairs = int(input("Enter number of stairs to climb : "))

a = 1
b = 1

for i in range(n_stairs):

    a, b = b, a+b


print(a)