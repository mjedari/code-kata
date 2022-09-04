"""
https://www.youtube.com/watch?v=-kedQt2UmnE
"""

from typing import List


def knapsack(V: List[int], W: List[int], wMax: int):
    # table that stores best solution for the given max capacity
    dp = [[0] * (wMax+1) for _ in range(len(V)+1)]
    # this table remembers if a particular object is put into the knapsack
    keep = [[0] * (wMax+1) for _ in range(len(V)+1)]

    for i in range(1, len(V)+1):
        for w in range(wMax+1):
            item_value = V[i - 1]
            item_weight = W[i - 1]
            newBest = item_value + dp[i - 1][w - item_weight]

            if W[i - 1] <= w and dp[i - 1][w] < newBest:
                dp[i][w] = newBest
                keep[i][w] = 1  # mark that a new object is put into the knapsack
            else:
                dp[i][w] = dp[i - 1][w]  # use the solution from previous row
                keep[i][w] = 0

    # print(T)
    # print(keep)

    # retrieve the path by walking up from bottom right corner
    selected_items_idx = []
    w = wMax
    for i in range(len(V), 0, -1):
        # print('i=', i, 'w=', w, 'keep[i][w]=', keep[i][w])
        if keep[i][w] == 1:
            w = w - W[i - 1]
            # print(i, w)
            selected_items_idx.append(i - 1)

    return dp[len(V)][wMax], selected_items_idx


values = [10, 40, 30, 60]
weights = [5, 4, 6, 3]
capacity = 10
print(knapsack(values, weights, capacity))
