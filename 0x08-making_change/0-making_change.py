#!/usr/bin/python3
"""
0-making_change.py
Module to calculate the fewest number of coins needed to meet a given
amount total.
"""


def makeChange(coins, total):
    """
    Calculate the fewest number of coins needed to meet a given
    amount total.

    Args:
    coins (list): List of coin values available for making change.
    total (int): The target amount to be achieved using the available coins.

    Returns:
    int: The fewest number of coins needed to meet the total amount.
         If the total is 0 or less, returns 0.
         If the total cannot be met by any combination of the available
         coins, returns -1.

    Algorithm:
    This function utilizes dynamic programming to solve the coin change
    problem.
    It builds an array 'dp' where dp[i] represents the minimum number of coins
    needed to achieve the amount 'i'. It iterates through the coin values
    and updates
    the 'dp' array incrementally to calculate the minimum coins required
    for each amount.
    The final result is stored in dp[total].

    Example:
    >>> makeChange([1, 2, 25], 37)
    7
    >>> makeChange([1256, 54, 48, 16, 102], 1453)
    -1
    """

    if total <= 0:
        return 0

    # Initialize an array to store the minimum number of coins needed
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    if dp[total] == float('inf'):
        return -1
    else:
        return dp[total]


# Example usage
if __name__ == "__main__":
    coins = [1, 2, 25]
    total_amount = 37
    print("Minimum coins needed:", makeChange(coins, total_amount))
