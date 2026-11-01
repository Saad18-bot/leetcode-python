nums = [1, 2, 3, 1, 1, 3]

pair = 0

for i in range(len(nums)):

    for j in range(1,len(nums)):
    
        if nums[i] == nums[j] and i < j:

            pair += 1


print(pair)
