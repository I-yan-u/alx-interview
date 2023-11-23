#!/usr/bin/python3
""" minimum coin change problem; fewest number of coins
    needed to make up a given total value.
"""


def makeChange(coins, total):
    if total <= 0:
        return 0

    # Initialize an array to store the minimum number of coins for each value
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Calculate the minimum number of coins for each value up to the total
    for i in range(1, total + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still set to infinity, it means the total cannot be met
    return dp[total] if dp[total] != float('inf') else -1
