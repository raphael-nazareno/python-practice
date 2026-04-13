accounts = [[1,5],[7,3],[3,5]]
wealth = []

for account in accounts:
    total = 0
    for money in account:
        total += money
    wealth.append(total)

max_wealth = max(wealth)
print(max_wealth)


for account in accounts:
        total = sum(account)
        if total > max_wealth:
            max_wealth = total
