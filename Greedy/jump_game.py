"""
https://leetcode.com/problems/jump-game/

You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.


Constraints:
    1 <= nums.length <= 10^4
    0 <= nums[i] <= 10^5 

"""


from typing import List
from functools import cache


"""
1- DFS With memo: Time Limit Exceeded on n == 10000 -> [9997,9997,9996,9995,9994,9993,9992,9991,9990,9989,9988,9987,9986,9985,9984,9983,9982,9981 ...... 6,5,4,3,2,1,0,0]]


Example: [2,3,1,1,4]

0:2
    1 -> 1:3
        1 -> 2:1
        2 -> 3:1
        3 -> 4:4
    2 -> 2:1
        1 -> 3:1
        2 -> 4:4

"""
# class Solution:
#     def canJump(self, nums: List[int]) -> bool:

#         n = len(nums)

#         @cache
#         def dfs(i):
#             if i == n - 1:
#                 return True

#             for j in range(i+1, min(i+nums[i], n-1) + 1):
#                 if dfs(j):
#                     return True
#             return False

#         return dfs(0)


"""
2- DP
"""

# # backward DP


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_position = len(nums) - 1

        # Iterate backwards
        for i in range(len(nums))[::-1]:
            # If this index has jump count which can reach to or beyond the last position
            if i + nums[i] >= last_position:
                # Since we just need to reach to this new index
                last_position = i
        return not last_position


# # forward DP
# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         last_position = 0

#         # Iterate forward
#         for i, val in enumerate(nums):
#             # If this index has jump count which can reach to or beyond the last position
#             if i > last_position:
#                 return False
#             # Since we just need to reach to this new index
#             last_position = max(last_position, i+val)
#         return True
