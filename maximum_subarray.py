nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

current_sum = nums[0]
max_sum = nums[0]

current_array = [nums[0]]
max_array = [nums[0]]

for num in nums[1:]:

    if num > current_sum + num :
        current_sum = num
        current_array = [num]

    else:
        current_sum = current_sum + num
        current_array.append(num)

    if current_sum > max_sum :
        max_sum = current_sum
        max_array = current_array.copy()

print("Maximum sum: ", max_sum)
print("Maximum array: ",max_array)
          