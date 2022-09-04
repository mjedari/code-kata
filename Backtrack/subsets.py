"""
https://leetcode.com/problems/subsets/


Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

"""
from typing import List

"""
1- Backtrack I

NOTE: 
    The End condition is when our loop finished 
    We should to add each step of the stack to the result
"""


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []
        stack = []

        def backtrack(stack, start):
            res.append(stack[:])

            for i in range(start, len(nums)):
                stack.append(nums[i])
                backtrack(stack, i + 1)
                stack.pop()

        backtrack(stack, 0)

        return res


"""
2- Backtrack II

"""
# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         ret = []
#         self.dfs(nums, [], ret)
#         return ret

#     def dfs(self, nums: List[int], path: List[int], ret: List[int]):
#         ret.append(path)
#         for i in range(len(nums)):
#             self.dfs(nums[i+1:], path+[nums[i]], ret)

"""
3- built in itertools.combinations
"""
# import itertools
# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:

#         subs = []
#         for i in range(len(nums)+1):
#             subs.extend(itertools.combinations(nums, i))

#         return subs


"""
4- Iteratively
"""


# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         res = [[]]

#         for num in nums:
#             res += [item+[num] for item in res]
#         return res


"""
6- Bit Manipulation
"""
# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         nums.sort()
#         for i in range(1<<len(nums)):
#             tmp = []
#             for j in range(len(nums)):
#                 if i & 1 << j:  # if i >> j & 1:
#                     tmp.append(nums[j])
#             res.append(tmp)
#         return res
