#!/usr/bin/python3
"""Script that computes the minimum operations
needed for a CopyAll-Paste task.
"""


def minOperations(n):
    """
    Computes the minimum number of operations for Copy All and Paste task.

    Args:
        n (int): The target number of 'H' characters.

    Returns:
        int: The minimum number of operations needed.
    """
    if n < 2:
        return 0
    factor_list = []
    i = 1
    while n != 1:
        i += 1
        if n % i == 0:
            while n % i == 0:
                n /= i
                factor_list.append(i)
    return sum(factor_list)
