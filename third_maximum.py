nums = [7, 4, 9, 2, 6, 10, 5, 5, 5, 2]
s  = set(nums)
nums1 = list(s)

nums1.sort()
d = nums1[::-1]
print(d[2])
