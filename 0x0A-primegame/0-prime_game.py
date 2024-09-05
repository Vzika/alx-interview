#!/usr/bin/python3
"""Prime Game
"""


def isWinner(x, nums):
    """Prime Game
    """
    if x < 1 or not nums:
        return None

    n = max(nums)

    primes = [True for _ in range(max(n + 1, 2))]
    primes[0], primes[1] = False, False

    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1

    primes = [i for i, p in enumerate(primes) if p]

    wins = 0
    for n in nums:
        wins += sum(p <= n for p in primes) % 2 == 1

    if wins * 2 == len(nums):
        return None

    if wins * 2 > len(nums):
        return "Maria"

    return "Ben"


# print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
