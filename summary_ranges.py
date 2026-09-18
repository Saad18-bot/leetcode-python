nums = [0, 1, 2, 4, 5, 7]

output = []
start = nums[0]

for i in range(1, len(nums)):

    if nums[i] != nums[i - 1] + 1:

        if start == nums[i - 1]:
            output.append(str(start))
        else:
            output.append(str(start) + "->" + str(nums[i - 1]))

        start = nums[i]

if start == nums[-1]:
    output.append(str(start))
else:
    output.append(str(start) + "->" + str(nums[-1]))

print(output)