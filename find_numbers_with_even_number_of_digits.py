nums = [12, 345, 2, 6, 7896]

even_num = 0

for i in range(len(nums)):

    n = len(str(nums[i])) 

    if n % 2 == 0:

          even_num += 1  



print(even_num)

