nums = [4, 3, 2, 7, 8, 2, 3, 1]

nums = list(set(nums))
nums.sort()

output = []

for i in range(1, len(nums) + 1):
    if i not in nums:
        output.append(i)

print(output)