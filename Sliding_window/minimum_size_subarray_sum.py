"""
https://leetcode.com/problems/minimum-size-subarray-sum/

Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.
"""

from typing import List

"""
Sliding window

1- more readable: with prefix_sum (Space(N))
2- withtout prefix_sum (Space(1))

[2, 3, 1, 2, 4, 3]

[0, 2, 5, 6, 8, 12, 15]

left    right   cond            min_len
0       1       2 >= 7          float("inf")
0       2       5 >= 7          float("inf")
0       3       6 >= 7          float("inf")
0       4       8 >= 7          4
1       4       7 >= 7          3
2       4       6 >= 7          3
2       5       7 >= 7          3
3       5       6 >= 7          3
3       6       9 >= 7          3
4       6       7 >= 7          2
5       6       3 >= 7          2
5       7       -----------------

"""


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        n = len(nums)

        if n == 1:
            return 1 if nums[0] == target else 0

        prefix_sum = [0] * (n + 1)

        for i, num in enumerate(nums, 1):
            prefix_sum[i] = prefix_sum[i - 1] + num

        left = 0
        right = 1
        min_len = float("inf")

        while right < len(prefix_sum):
            if prefix_sum[right] - prefix_sum[left] >= target:
                min_len = min(min_len, right - left)
                if min_len == 1:
                    break
                left += 1
            else:
                right += 1

        return 0 if min_len == float("inf") else min_len


# class Solution:
#     def minSubArrayLen(self, target: int, nums: List[int]) -> int:
#         i, res = 0, len(nums) + 1
#         for j in range(len(nums)):
#             target -= nums[j]
#             while target <= 0:
#                 res = min(res, j - i + 1)
#                 target += nums[i]
#                 i += 1
#         return res % (len(nums) + 1)
