"""
https://leetcode.com/problems/coin-change-2/


You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.

The answer is guaranteed to fit into a signed 32-bit integer.

"""
from typing import List
from functools import cache

"""
1- Bruteforce: 
    from itertootls import combinations_with_replacement
    make the list of all combination with replacement for r from 1 to len(coins)
    Time: O(n) + O(n ^ 2) + ... + O(n ^ n) https://rosettacode.org/wiki/Combinations_with_repetitions
    and final loop for counting combination == amount
"""

"""
2- Recursive with memoization [RUN FASTER THAN 2-D DP!]
    coins = (1, 2, 5) amount = 5
    1 2 5 -> pick 1 and call recursively with amount=4 or pick 2 and call with amount=3
    1 2 5 ...
    1 2 5 ...
    ...   ...
          
    max_depth_call = amount / least coin value = 5 / 1 = 5 = M
    branching_factor = |coins| = C
          
    Time: O(C ^ M)                  
    https://docs.python.org/3/library/functools.html
"""


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        @cache
        def f(i_th_coin, amount):
            if amount == 0:
                return 1  # If we found a way to create the desired amount

            if amount < 0 or i_th_coin >= len(coins):
                return 0  # If we went over our amount or we have no more coins left

            # Our solutions can be divided into two sets,
            #   1) Solution with i-th coin
            #   2) Solution without i-th coin
            return f(i_th_coin, amount - coins[i_th_coin]) + f(i_th_coin+1, amount)

        return f(0, amount)


"""
Classic knapsack problem

    dp[i][j] : the number of combinations to make up amount j by using the first i types of coins
    State transition:
        - not using the ith coin, only using the first i-1 coins to make up amount j, then we have dp[i-1][j] ways.
        - using the ith coin, since we can use unlimited same coin, we need to know how many ways to make up amount j - coins[i-1] by using first i coins(including ith), which is dp[i][j-coins[i-1]]
    
    Initialization: dp[i][0] = 1
    
    We can see that dp[i][j] only rely on dp[i-1][j] and dp[i][j-coins[i]], then we can optimize the space by only using one-dimension array.

"""

"""
3- 1-D Dynamic programming Time(m*n) Memroy(n)
    dp: Array of size amount + 1. One additional space is reserved because we also want to store the solution for the 0 amount.
    init: dp[0] = 1. one way to change the 0 amount
    for each coin: dp[a] = dp[a] + dp[a - coin]        
    Answer: dp[-1]
"""


# class Solution:
#     def change(self, amount: int, coins: List[int]) -> int:
#         dp = [0] * (amount + 1)
#         dp[0] = 1

#         for coin in coins:
#             for a in range(coin, amount+1):
#                 dp[a] += dp[a - coin]

#         return dp[-1]


"""
4- 2-D Dynamic programing: Time(N x M), Space(N x M)

    Table 
        - for filling cell i,j -> i = amount and j = all coins from 0 to j
        - fill the table with example and try to reach the pattern for implementation
        Example: amount = 7 coins(1, 2, 3, 5)

                1  2  3  5

            0   1  1  1  1
            1   1  1  1  1
            2   1  2  2  2
            3   1  2  3  3
            4   1  3  4  4
            5   1  3  5  6
            6   1  4  7  8
            7   1  4  8  10


            table[i][j] = x + y
            x -> solution including coin j -> table[amount - coin j][coin j]
            y -> solution excluding coin j -> table[amount][column before coin j]

            example -> i = 6, j = 2, coin j = 3 (coins 1, 2, 3)

            x -> [6 - 3][2] -> [3][2] = 3
            y -> [6][1] -> 4

            table[6][2] = x + y = 7       
"""
# class Solution:
#     def change(self, amount: int, coins: List[int]) -> int:
#         l = len(coins)
#         S = coins
#         table = [[0 for x in range(l)] for x in range(amount+1)]

#         # Fill the entries for 0 value case (n = 0)
#         for i in range(l):
#             table[0][i] = 1

#         # Fill rest of the table entries in bottom up manner
#         for i in range(1, amount+1):
#             for j in range(l):

#                 # Count of solutions including coins[j]
#                 x = table[i - coins[j]][j] if i-coins[j] >= 0 else 0

#                 # Count of solutions excluding coins[j]
#                 y = table[i][j-1] if j >= 1 else 0

#                 # total count
#                 table[i][j] = x + y

#         return table[amount][l-1]
