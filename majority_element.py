nums = [1, 3, 3, 2]

max_count = 0
majority = 0

for i in range(len(nums)):

    c = nums.count(nums[i])

    if c > max_count:
        max_count = c
        majority = nums[i]

print("The number that has occurred majority of times is:", majority)