nums = [1, 2, 3, 1]
indexDiff = 3
valueDiff = 0

found = False

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):

        if abs(i - j) <= indexDiff and abs(nums[i] - nums[j]) <= valueDiff:
            found = True
            break

    if found:
        break

print(found)