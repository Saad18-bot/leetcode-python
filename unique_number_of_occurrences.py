arr = [1, 2, 2, 1, 1, 3]

counts = {}

for num in arr:
    if num in counts:
        counts[num] += 1
    else:
        counts[num] = 1

frequencies = list(counts.values())

if len(frequencies) == len(set(frequencies)):
    print(True)
else:
    print(False)