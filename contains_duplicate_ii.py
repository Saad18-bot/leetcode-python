nums = [1, 2, 3, 1]

k = 3
found = False

if len(nums) != len(set(nums)):

    for i, num1 in enumerate(nums):

        for j, num2 in enumerate(nums):

            if num1 == num2 and i != j and abs(i - j) <= k:
                print("True")
                found = True
                break

        if found:
            break

if not found:
    print("False")