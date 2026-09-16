nums = [1, 2, 9, 9]

for i in range(len(nums)-1,-1,-1):

    if(nums[i] < 9):
        nums[i] = nums[i] + 1
        break

    nums[i] = 0

else:
    nums.insert(0,1)


print(nums)

   