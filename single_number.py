nums = [4, 1, 2, 1, 2]

for i in range(len(nums)-1):
    s = nums.count(nums[i])
    if s == 1:
        print(nums[i])