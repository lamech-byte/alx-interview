#!/usr/bin/python3
"""
0-making_change.py
Module to calculate the fewest number of coins needed to meet a given
amount total.
"""


def makeChange(coins, total):

    if total <= 0:
        return 0
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)
    if dp[total] == float('inf'):
        return -1
    else:
        return dp[total]


if __name__ == "__main__":
    coins = [1, 2, 25]
    total_amount = 37
    print("Minimum coins needed:", makeChange(coins, total_amount))
