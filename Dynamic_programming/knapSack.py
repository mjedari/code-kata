"""
Given weights and profits of n items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack.

"""
# Basic solution


from functools import cache


# def solve_knapsack(profits, weights, capacity):

#     def knapsack(cap, idx):
#         # base checks
#         if cap <= 0 or idx >= len(profits):
#             return 0

#         # recursive call after choosing the element at the currentIndex
#         # if the weight of the element at currentIndex exceeds the capacity, we shouldn't process this
#         p1 = 0
#         if weights[idx] <= cap:
#             p1 = profits[idx] + knapsack(cap - weights[idx], idx + 1)

#         # recursive call after excluding the element at the currentIndex
#         p2 = knapsack(cap, idx + 1)

#         return max(p1, p2)

#     return knapsack(capacity, 0)


# Top-down Dynamic Programming with Memoization
# def solve_knapsack(profits, weights, capacity):

#     @cache
#     def knapsack(cap, idx):
#         # base checks
#         if cap <= 0 or idx >= len(profits):
#             return 0

#         # recursive call after choosing the element at the currentIndex
#         # if the weight of the element at currentIndex exceeds the capacity, we shouldn't process this
#         p1 = 0
#         if weights[idx] <= cap:
#             p1 = profits[idx] + knapsack(cap - weights[idx], idx + 1)

#         # recursive call after excluding the element at the currentIndex
#         p2 = knapsack(cap, idx + 1)

#         return max(p1, p2)

#     return knapsack(capacity, 0)


"""
Bottom-up Dynamic Programming

https://www.youtube.com/watch?v=-kedQt2UmnE

dp = [n + 1] x [W + 1]

The rows (items)    -> 0 to n
The cols (capacity) -> 0 to W


This means, dp[i][c] will represent the maximum knapsack profit for capacity `c` calculated from the first `i` items.

Steps
#1- Setting the 0th row and column to 0.
#2- For each cell [i][c], we have two options:
    - include object [i].
    - exclude object [i].
- There are two conditions that should be satisfied to include object [i]:
    - The total weight after including object [i] should not exceed the weight limit.
    - The profit after including object [i] should be greater as compared to when the object is not included.

        0       1       2       3       4       5   
-------------------------------------------------
        0       0       0       0       0       0
1, 10   0      10      10      10      10      10
2, 15   0      10      15      25      25      25
3, 30   0      10      15      30      40      45
4, 40   0      10      15      30      40      50



"""


def solve_knapsack(profits, weights, capacity):
    n = len(profits)
    if capacity <= 0 or n == 0 or len(weights) != n:
        return 0

    dp = [[0 for x in range(capacity+1)] for y in range(n)]

    # populate the capacity = 0 columns, with '0' capacity we have '0' profit
    for i in range(0, n):
        dp[i][0] = 0

    # if we have only one weight, we will take it if it is not more than the capacity
    for c in range(0, capacity+1):
        if weights[0] <= c:
            dp[0][c] = profits[0]

    for i in range(1, n):
        for c in range(1, capacity+1):
            profit1, profit2 = 0, 0
            if weights[i] <= c:
                profit1 = profits[i] + dp[i-1][c-weights[i]]
            profit2 = dp[i-1][c]
            dp[i][c] = max(profit1, profit2)

    # maximum profit will be at the bottom-right corner.
    return dp[n-1][capacity]


profits = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50
print(solve_knapsack(profits, weights, capacity))
