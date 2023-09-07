#!/usr/bin/python3

def is_prime(num):
    """
    Check if a number is prime.

    Args:
        num (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def isWinner(x, nums):
    """
    Determine the winner of a game between Maria and Ben.

    Args:
        x (int): The number of rounds to play.
        nums (list of int): A list of integers representing the
        set of numbers for each round.

    Returns:
        str or None: The name of the player that won the most rounds
        (either "Maria" or "Ben").
                     If the winner cannot be determined, returns None.

    Constraints:
        - x and len(nums) will not be larger than 10,000.
    """
    if x <= 0 or not nums:
        return None

    # Calculate the maximum number in nums
    max_num = max(nums)

    # Precompute primes using the Sieve of Eratosthenes
    primes = [False, False] + [True] * (max_num - 1)
    for p in range(2, int(max_num**0.5) + 1):
        if primes[p]:
            for i in range(p * p, max_num + 1, p):
                primes[i] = False

    # Count the number of primes in nums
    prime_count = sum(1 for num in nums if primes[num])

    # Determine the winner based on the prime count
    if prime_count % 2 == 0:
        return "Ben"
    else:
        return "Maria"


# Example usage
if __name__ == "__main__":
    print("Winner: {}".format(isWinner(3, [4, 5, 1])))
