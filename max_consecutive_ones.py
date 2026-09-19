nums = [1, 1, 2, 0, 1, 3, 4, 1, 1, 1, 5]
max_count = 0
count = 0
for i in range(len(nums)):
    if nums[i] == 1:
        count += 1
        if count > max_count:
            max_count = count
    elif nums[i] != 1:
        count = 0

print(max_count)
