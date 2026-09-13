nums = [1, 1, 2, 2, 3]

unique = []

for num in nums:
    if num not in unique:
        unique.append(num)
        
print(unique)