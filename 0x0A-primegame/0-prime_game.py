#!/usr/bin/python3

"""
    Check if a number is prime.

    Args:
        num (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """


def isWinner(x, nums):
    """
    Determine the winner of a game between Maria and Ben.

    Args:
        x (int): The number of rounds to play.
        nums (list of int): A list of integers representing the
        set of numbers for each round.

    Returns:
        str or None: The name of the player that won the most
        rounds (either "Maria" or "Ben").
                     If the winner cannot be determined, returns None.

    Constraints:
        - x and len(nums) will not be larger than 10,000.
    """
    if not nums or x < 1:
        return None
    n = max(nums)
    primes = [True for i in range(max(n + 1, 2))]
    for i in range(2, int(pow(n, 0.5)) + 1):
        if not primes[i]:
            continue
        for j in range(i*i, n + 1, i):
            primes[j] = False
    primes[0] = primes[1] = False
    c = 0
    for i in range(len(primes)):
        if primes[i]:
            c += 1
        primes[i] = c
    player1 = 0
    for n in nums:
        player1 += primes[n] % 2 == 1
    if player1 * 2 == len(nums):
        return None
    if player1 * 2 > len(nums):
        return "Maria"
    return "Ben"
