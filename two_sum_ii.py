nums = [2, 7, 11, 15]
target = 9
found = False
for i,num1 in enumerate(nums):
    for j,num2 in enumerate(nums):

        if num1 + num2 == target and i != j:
            result = [i+1,j+1]
            print(result)
            
            found = True
            break
    if found:
        break

if not found:
    print("Cant find target!!")
    