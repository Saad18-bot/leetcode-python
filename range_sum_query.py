nums = [-2, 0, 3, -5, 2, -1]

l = int(input("Enter left range: "))
r = int(input("Enter right range: "))
sum = 0

for i in range(l,r+1):
    sum += nums[i]



print(sum)