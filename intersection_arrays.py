nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
nums3 = []
for num in nums1:
    for num1 in nums2:
        if num == num1 and num not in nums3:
           nums3.append(num)
        else:
            continue
            
print(nums3)