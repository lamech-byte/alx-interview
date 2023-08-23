#!/usr/bin/python3

def makeChange(coins, total):
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for val in range(1, total + 1):
        min_coins = float('inf')
        for coin in coins:
            if coin <= val:
                min_coins = min(min_coins, dp[val - coin] + 1)
        dp[val] = min_coins

    if dp[total] == float('inf'):
        return -1
    return dp[total]


if __name__ == "__main__":
    print(makeChange([1, 2, 25], 37))
    print(makeChange([1256, 54, 48, 16, 102], 1453))
