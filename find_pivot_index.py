nums = [1, 7, 3, 6, 5, 6]

for i in range(len(nums)):

    left = sum(nums[:i])
    right = sum(nums[i+1:])

    if left == right:
        print(i)
        break
    
else:
    print(-1)