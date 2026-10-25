candies = [2, 3, 5, 1, 3]
extraCandies = 3
largest = max(candies)
for i in range(len(candies)):

    candies[i] = candies[i] + extraCandies


new_list = []
for i in candies:
    if i >= largest:
        new_list.append(True)
    else:
        new_list.append(False)

print(new_list)
        

