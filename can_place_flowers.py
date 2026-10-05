fb = [1, 0, 0, 0, 1, 0, 0]
n = 2

for i in range(len(fb)+1):
    if fb[i] == 0 and fb[i-1] == 0 and fb[i+1] == 0 and n != 0 and fb[i] != fb[-1]:
        fb[i] = 1
        n -= 1


print(fb)



    
