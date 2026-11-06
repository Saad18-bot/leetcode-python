mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
d1 = 0
d2 = 0
total_d = 0
for i in range(len(mat)):
    for j in  range(len(mat)):

        d1 = mat[i][j] + mat[i+1][j+1] + mat[i+2][j+2]
        d2 = mat[i][j+2] + mat[i+1][j+1] + mat[i+2][j]
        break

total_d = d1 + d2
print(total_d)



        