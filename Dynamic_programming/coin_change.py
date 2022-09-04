"""
https://leetcode.com/problems/coin-change/

You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

"""
from typing import List


"""
1- Brute force with Memoization

Note: @functools.cache won't work due to unhashable type coins (List[int])
"""
# class Solution:

#     def best_sum(self, coins, amount, memo):
#         if amount in memo:
#             return memo[amount]

#         if amount == 0:
#             return 0

#         shortest = float("inf")

#         for i_th_coin in range(len(coins)):
#             rem = amount - coins[i_th_coin]
#             if rem >= 0:
#                 res = self.best_sum(coins, rem, memo)
#                 res += 1
#                 shortest = min(shortest, res)

#         memo[amount] = shortest
#         return memo[amount]

#     def coinChange(self, coins: List[int], amount: int) -> int:
#         ans = self.best_sum(coins, amount, {})
#         return ans if ans != float("inf") else -1


"""
2- DP: Assume dp[a] is the fewest number of coins making up amount `a`, then for every coin in coins, dp[a] = min(dp[a], dp[a - coin] + 1).

The time complexity is O(amount * coins.length) and the space complexity is O(amount)
"""


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                # coin can be used here
                if a - c >= 0:
                    # minimum "not using coin" and "using coin"
                    dp[a] = min(dp[a], 1 + dp[a-c])

        return dp[amount] if dp[amount] != amount + 1 else -1

# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:

#         if amount == 0:
#             return 0

#         value1 = [0]
#         value2 = []
#         nc = 0
#         visited = [False] * (amount+1)
#         visited[0] = True
#         while value1:
#             nc += 1
#             for v in value1:
#                 for coin in coins:
#                     newval = v + coin
#                     if newval == amount:
#                         return nc
#                     elif newval > amount:
#                         continue
#                     elif not visited[newval]:
#                         visited[newval] = True
#                         value2.append(newval)

#             value1, value2 = value2, []

#         return -1


# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         if amount == 0:
#             return 0
#         C = sorted(coins, reverse=True)
#         N = [amount//c for c in C]
#         A = 1 << amount
#         M = (A << 1)-1
#         v = 1
#         n = 1
#         while True:
#             while N and n > N[0]:
#                 del N[0]
#                 del C[0]
#             w = 0
#             for c in C:
#                 w |= (v << c) & M
#             if w & A:
#                 return n
#             if w & (A-1) == 0:
#                 return -1
#             v = w
#             n += 1
