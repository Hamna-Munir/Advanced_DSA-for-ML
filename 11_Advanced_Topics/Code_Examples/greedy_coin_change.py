# Greedy Algorithm Example
# Coin Change Problem

def coin_change(coins, amount):

    coins.sort(reverse=True)
    result = []

    for coin in coins:
        while amount >= coin:
            amount -= coin
            result.append(coin)

    return result


coins = [1, 5, 10, 25]
amount = 30

print("Coins used:", coin_change(coins, amount))


# Output
# Coins used: [25, 5]
