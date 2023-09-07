#!/usr/bin/python3

""" Prime Game """


def isWinner(x, nums):
    """
    Args:
        x: the number of rounds
        nums: an array of n
    Returns:
        name of the player that won the most rounds
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
