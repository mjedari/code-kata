"""
https://leetcode.com/problems/product-of-array-except-self/

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of
nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
"""

"""
Understand
    We are given array nums, and we want to return an array answer such that answer[i] is equal to the product of all
    the elements of nums except nums[i].
    The algorithm should be of o(n) time.
    We cannot use division!

Example
    Input: nums = [1, 2, 3, 4]
    Output: [2 * 3 * 4, 1 * 3 * 4, 1 * 2 * 4, 1 * 2 * 3]
            [24, 12, 8, 6]

Questions:
    Is our input sorted? -> No
    Can our input be empty? -> No
    Minimum length of input -> 2

Constraints
    Greedy -> O(n) time

Plan
    Recognize the pattern of prefixes and suffixes here.
    Take for example, [1, 2, 3, 4, 5]
    prefix: [1, 1, 1*2, 1*2*3, 1*2*3*4]
    suffix: [2*3*4*5, 3*4*5, 4*5, 5, 1]
    
    The prefix of each index except at i is: [1,    1,  2,  6, 24]
    The suffix of each index except at i is: [120, 60, 20,  5,  1]
    
    Resulting array (product of all elements except self): [120, 60, 40, 30, 24] = prefix[i] * suffix[i]

One pass to calculate prefix
One pass to calculate suffix
One pass to calculate result

TC: O(N)
SC: O(N)

You can do this in O(1) space (disregarding output array) by calculating prefix forwards in one pass and then multiplying it by suffix in another pass (in reverse loop).
"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        calculate = 1
        for i in range(n):
            ans.append(calculate)
            calculate *= nums[i]
        calculate = 1
        for i in range(n - 1, -1, -1):
            ans[i] *= calculate
            calculate *= nums[i]
        return ans

# import itertools
# import operator

# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         prefix = list(itertools.accumulate(nums, operator.mul, initial=1))
#         postfix = list(itertools.accumulate(nums[::-1], operator.mul, initial=1))[::-1]
#         return [prefix[i] * postfix[i + 1] for i in range(len(nums))]
