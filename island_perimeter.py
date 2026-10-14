grid = [
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 0]
]

perimeter = 0

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 1:
            perimeter += 4

            if i > 0 and grid[i - 1][j] == 1:
                perimeter -= 1

            if j > 0 and grid[i][j - 1] == 1:
                perimeter -= 1

print(perimeter)