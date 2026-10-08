nums = [3, 2, 3]

result = []

for i in nums:

    if nums.count(i) > len(nums) // 3 and i not in result:
        result.append(i)

print(result)