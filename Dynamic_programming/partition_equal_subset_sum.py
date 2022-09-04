"""
https://leetcode.com/problems/partition-equal-subset-sum/

Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.


"""


from typing import List

"""
Problem:
    Can an array nums can be partitioned into two subsets such that the sum of elements in both subsets is equal?
    
    Steps to solve:
        Realize that if there is any subset nums_subset in nums where sum(nums_subset) = sum(nums)/2, we can return True.

    Map the problem to fit the 0/1 knapsack problem:
        Definition of Knapsack Problem: "Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack"
        
        let weights = values = nums
        let W = sum(nums)/2



"""


"""
1- DFS + Memo

"""
# class Solution:
#     def canPartition(self, nums: List[int]) -> bool:
#         s = sum(nums)
#         if s % 2:
#             return False

#         def dfs(nums: List[int], target: int, cache: Set[int]):
#             if target < 0: return False
#             if target == 0: return True
#             if target in cache: return False

#             cache.add(target)
#             for i, n in enumerate(nums):
#                 if dfs(nums[i+1:], target-n, cache):
#                     return True
#             return False


#         return dfs(nums, s//2, set())

"""
2- 2-D DP

NOTE: First method isn't a new list, it's just point the previous one

    from pprint import pprint as pp
    a = [[False] * 2] * 2
    b = [[False] * 2 for _ in range(2)]

    pp(a)
    pp(b)
    a[1][1] = True
    b[1][1] = True
    print()
    pp(a)
    pp(b)

    [[False, False], [False, False]]
    [[False, False], [False, False]]

    [[False, True], [False, True]]
    [[False, False], [False, True]]
"""


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2:
            return False

        s //= 2
        n = len(nums)

        dp = [[False]*(s+1) for _ in range(n+1)]

        for i in range(n+1):
            for j in range(s+1):
                if j == 0:
                    dp[i][j] = True
                elif nums[i-1] <= j:
                    dp[i][j] = dp[i-1][j-nums[i-1]] or dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]

        return dp[n][s]


"""
3- 1-D DP
"""
# class Solution:
#     def canPartition(self, nums: List[int]) -> bool:
#         s = sum(nums)
#         if s % 2:
#             return False

#         """
#         The dp array stores the total obtained sums we have come across so far.
#         Notice that dp[0] = True; if we never select any element, the total sum is 0.
#         """
#         dp = [True] + [False] * s

#         # Now, loop through each element
#         for num in nums:
#             for curr in range(s, num-1, -1):  # avoid going out-of-bounds
#                 """
#                 Case 1: The current sum (curr) has been seen before.
#                         Then, if we don't select the current element, the sum will not change.
# 						So, this total sum will still exist, and its dp value remains True.

# 				Case 2: The current sum (curr) has not been seen before,
# 				        but it can be obtained by selecting the current element.
# 						This means that dp[curr-num] = True, and thus dp[curr] now becomes True.

# 				Case 3: The current sum (curr) has not been seen before,
# 				        and it cannot be obtained by selecting the current element.
# 						So, this total sum will still not exist, and its dp value remains False.
#                 """
#                 dp[curr] = dp[curr] or dp[curr-num]

#         # Finally, we want to obtain the target sum
#         return dp[s//2]
