prices = [7,1,5,3,6,4]

max_profit = 0

for i in range(len(prices)):
    for j in range(i+1, len(prices)):
        diff = prices[j] - prices[i]

        if ( diff > max_profit ):
            max_profit = diff

print("max_profit: ", max_profit)