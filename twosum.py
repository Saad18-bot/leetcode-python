nums = [8, 14, 3, 21, 7, 11]
target = 18
found = False
for i,num1 in enumerate(nums):
    for j,num2 in enumerate(nums):
        if num1 + num2 == 18 and i != j:
            print("Index i: ", i)
            print("Index j: ", j)
            found = True
            break
    if found:
        break

if not found:
    print("Cant find target!!")
