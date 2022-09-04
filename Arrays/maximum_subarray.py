"""
https://leetcode.com/problems/maximum-subarray

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.



"""

from typing import List
from math import inf


"""
1- Brute force, TLE, O(N ^ 2)
"""
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         ans = -inf
#         for i in range(len(nums)):
#             cur_sum = 0
#             for j in range(i, len(nums)):
#                 cur_sum += nums[j]
#                 ans = max(ans, cur_sum)
#         return ans


"""
2- DFS with Memo

- At each index i, we can either pick that element or not pick it.
- If we pick current element, then all future element must also be picked since our array needs to be contiguous.
- If we had picked any elements till now, we can either end further recursion at any time by returning sum formed till now or we can choose current element and recurse further. This denotes two choices of either choosing the subarray formed from 1st picked element till now or expanding the subarray by choosing current element respectively.
"""

# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         @cache
#         def solve(i: int, must_pick: bool) -> int:
#             if i >= len(nums):
#                 return 0 if must_pick else -inf

#             return max(nums[i] + solve(i+1, True), 0 if must_pick else solve(i+1, False))

#         return solve(0, False)

"""
3- DP, 2D
We can employ similar logic in iterative version as well. Here, we again use dp array and use bottom-up approach. Here dp[1][i] denotes maximum subarray sum ending at i (including nums[i]) and dp[0][i] denotes maximum subarray sum upto i (may or may not include nums[i]).

At each index, we update dp[1][i] as max between either only choosing current element - nums[i] or extending from previous subarray and choosing current element as well - dp[1][i-1] + nums[i]
Similarly, dp[0][1] can be updated as max between maximum sum subarray found till last index - dp[0][i-1] or max subarray sum found ending at current index dp[1][i].

Example: [-2,1,-3,4,-1,2,1,-5,4]

Initial
[[-2, 0, 0, 0, 0, 0, 0, 0, 0], [-2, 0, 0, 0, 0, 0, 0, 0, 0]]


Updated by
    dp[1][i] = max(nums[i], nums[i] + dp[1][i-1])
    dp[0][i] = max(dp[0][i-1], dp[1][i])

[[-2, 1, 1, 4, 4, 5, 6, 6, 6], [-2, 1, -2, 4, 3, 5, 6, 1, 5]]


"""

# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:

#         dp = [[0]*len(nums) for i in range(2)]

#         dp[0][0], dp[1][0] = nums[0], nums[0]

#         print(dp)
#         for i in range(1, len(nums)):
#             dp[1][i] = max(nums[i], nums[i] + dp[1][i-1])
#             dp[0][i] = max(dp[0][i-1], dp[1][i])

#         print(dp)
#         return dp[0][-1]


"""
4- DP - 1D

Example: 
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    
    
    dp[i] = max(dp[i-1]+nums[i], nums[i])
    
    
    dp =   [-2, 1, -2, 4,  3, 5, 6, -1, 4]
"""
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:

#         dp = [0] * len(nums)
#         dp[0] = nums[0]
#         for i in range(1, len(nums)):
#             dp[i] = max(dp[i-1]+nums[i], nums[i])

#         return max(dp)


"""
5- Kadane's Algorithm

We can observe that in the previous approach, dp[i] only depended on dp[i-1]. So do we really need to maintain the whole dp array of N elements? One might see the last line of previous solution and say that we needed all elements of dp at the end to find the maximum sum subarray. But we can simply optimize that by storing the max at each iteration instead of separately calculating it at the end.

Thus, we only need to maintain curMax which is the maximum subarray sum ending at i and maxTillNow which is the maximum sum we have seen till now. And this way of solving this problem is what we popularly know as Kadane's Algorithm
"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_max, max_till_now = 0, -inf

        for c in nums:
            cur_max = max(c, cur_max + c)
            max_till_now = max(max_till_now, cur_max)
        return max_till_now


"""
6- Divide & Conquer

Modelling the problem by observing that the maximum subarray sum is such that it lies somewhere -

- entirely in the left-half of array [L, mid-1], OR
- entirely in the right-half of array [mid+1, R], OR
- in array consisting of mid element along with some part of left-half and some part of right-half such that these form contiguous subarray - [L', R'] = [L', mid-1] + [mid] + [mid+1,R'], where L' >= L and R' <= R
With the above observation, we can recursively divide the array into sub-problems on the left and right halves and then combine these results on the way back up to find the maximum subarray sum.
"""

# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         def maxSubArray(A, L, R):
#             if L > R: return -inf
#             mid, left_sum, right_sum, cur_sum = (L + R) // 2, 0, 0, 0
#             for i in range(mid-1, L-1, -1):
#                 left_sum = max(left_sum, cur_sum := cur_sum + A[i])
#             cur_sum = 0
#             for i in range(mid+1, R+1):
#                 right_sum = max(right_sum, cur_sum := cur_sum + A[i])
#             return max(maxSubArray(A, L, mid-1), maxSubArray(A, mid+1, R), left_sum + A[mid] + right_sum)

#         return maxSubArray(nums, 0, len(nums)-1)
