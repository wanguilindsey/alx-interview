#!/usr/bin/python3
"""Module for Prime Game."""


def isWinner(x, nums):
    """
    Determines the winner of a prime game.

    Args:
        x (int): Number of rounds.
        nums (list): List of integers where each integer n denotes
                     a set of consecutive integers from 1 to n.

    Returns:
        str: "Ben" or "Maria" as the winner.
        None: If the winner can't be determined.
    """
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None

    ben, maria = 0, 0
    a = [1 for _ in range(sorted(nums)[-1] + 1)]
    a[0], a[1] = 0, 0  # 0 and 1 are not prime

    # Sieve of Eratosthenes to mark primes
    for i in range(2, len(a)):
        rm_multiples(a, i)

    # Determine winner for each round
    for i in nums:
        if sum(a[0:i + 1]) % 2 == 0:
            ben += 1
        else:
            maria += 1

    if ben > maria:
        return "Ben"
    if maria > ben:
        return "Maria"
    return None


def rm_multiples(ls, x):
    """
    Marks multiples of a prime as non-prime.

    Args:
        ls (list): List marking primes.
        x (int): Prime number.
    """
    for i in range(2, len(ls)):
        try:
            ls[i * x] = 0
        except (ValueError, IndexError):
            break
