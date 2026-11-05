accounts = [[2, 8], [3, 4, 5], [10, 1]]

highest_customer_wealth = 0
richest_customer = 0

for i in range(len(accounts)):

    customer_wealth = 0

    for j in range(len(accounts[i])):
        customer_wealth += accounts[i][j]

    if customer_wealth > highest_customer_wealth:
        highest_customer_wealth = customer_wealth
        richest_customer = i + 1

print("Richest customer:", richest_customer)
print("Highest wealth:", highest_customer_wealth)