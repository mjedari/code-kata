"""
https://leetcode.com/problems/longest-increasing-subsequence/

Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].



"""
# def call_counter(func):
#     def helper(*args, **kwargs):
#         helper.calls += 1
#         return func(*args, **kwargs)
#     helper.calls = 0
#     helper.__name__= func.__name__

#     return helper
from typing import List
import bisect
"""
1-1 Brute-Force

    Time Complexity : O(2^N), all subsets
    Space Complexity : O(N), max recursive stack depth.
    
    Caching (stop extending the tree path) won't help
    
    input: list(range(2500))
        Memory Limit Exceeded on LC 
        RecursionError: maximum recursion depth exceeded on local
"""


# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:

#         # @call_counter
#         def gen_subsets(nums: List[int], path: List[int], ret: List[int]):
#             # stop extending the path
#             if len(path) > 1 and path[-1] <= path[-2]:
#                 return

#             # Generating subsets
#             ret.append(path)
#             for i in range(len(nums)):
#                 gen_subsets(nums[i+1:], path+[nums[i]], ret)

#         ret = []
#         gen_subsets(nums, [], ret)
#         return len(sorted(ret, key=len)[-1])


"""
1-2 Another Brute-Force

    Time Complexity : O(2^N), all subsets
    Space Complexity : O(N), max recursive stack depth.
"""
# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         def f(nums: List[int], i:int, prev:int) -> int:

#             if i >= len(nums):
#                 return 0

#             take = 0
#             dont_take = f(nums, i+1, prev)

#             if nums[i] > prev:
#                 take = 1 + f(nums, i + 1, nums[i])


#             return max(take, dont_take)

#         return f(nums, 0, float("-inf"))
"""
2- Dynamic Programming
    
    
    Time: O(N^2), where N <= 2500 is the number of elements in array nums.
    Space: O(N)
    
    Example: 
    
    in = [1, 2, 4, 3]
    
    - Let dp[i] is the longest increase subsequence which ends at nums[i].
    
    - if nums[i] > nums[j] then dp[i] = max(dp[i], 1 + dp[j])
    
    i   j   dp
    1   0   [1, 1, 1, 1]

    2   0   [1, 2, 1, 1]

    2   1   [1, 2, 2, 1]

    3   0   [1, 2, 3, 1]

    3   1   [1, 2, 3, 2]

    3   2   [1, 2, 3, 3]    
"""
# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         if not nums:
#             return 0

#         n = len(nums)
#         dp = [1] * n

#         for i in range(1, n):
#             for j in range(i):
#                 if nums[i] > nums[j]:
#                     dp[i] = max(dp[i], 1 + dp[j])

#         return max(dp)
"""
3- Greedy with Binary Search (Patience sort)
    https://www.youtube.com/watch?v=22s1xxRvy28

    Let's construct the idea from following example.
        - Consider the example nums = [2, 6, 8, 3, 4, 5, 1], let's try to build the increasing subsequences starting with an empty one: sub1 = [].
        - Let pick the first element, sub1 = [2].
        - 6 is greater than previous number, sub1 = [2, 6]
        - 8 is greater than previous number, sub1 = [2, 6, 8]
        - 3 is less than previous number, we can't extend the subsequence sub1, but we must keep 3 because in the future there may have the longest subsequence start with [2, 3], sub1 = [2, 6, 8], sub2 = [2, 3].
        - With 4, we can't extend sub1, but we can extend sub2, so sub1 = [2, 6, 8], sub2 = [2, 3, 4].
        - With 5, we can't extend sub1, but we can extend sub2, so sub1 = [2, 6, 8], sub2 = [2, 3, 4, 5].
        - With 1, we can't extend neighter sub1 nor sub2, but we need to keep 1, so sub1 = [2, 6, 8], sub2 = [2, 3, 4, 5], sub3 = [1].
        - Finally, length of longest increase subsequence = len(sub2) = 4.
        
    - In the above steps, we need to keep different sub arrays (sub1, sub2..., subk) which causes poor performance. But we notice that we can just keep one sub array, when new number x is not greater than the last 
    element of the subsequence sub, we do binary search to find the smallest element >= x in sub, and replace with number x.
    
    - Let's run that example nums = [2, 6, 8, 3, 4, 5, 1] again:
        - Let pick the first element, sub = [2].
        - 6 is greater than previous number, sub = [2, 6]
        - 8 is greater than previous number, sub = [2, 6, 8]
        - 3 is less than previous number, so we can't extend the subsequence sub. We need to find the smallest number >= 3 in sub, it's 6. Then we overwrite it, now sub = [2, 3, 8].
        - 4 is less than previous number, so we can't extend the subsequence sub. We overwrite 8 by 4, so sub = [2, 3, 4].
        - 5 is greater than previous number, sub = [2, 3, 4, 5].
        - 1 is less than previous number, so we can't extend the subsequence sub. We overwrite 2 by 1, so sub = [1, 3, 4, 5].
        - Finally, length of longest increase subsequence = len(sub) = 4.
        
        
        Time: O(N * logN), where N <= 2500 is the number of elements in array nums.
        Space: O(N), we can achieve O(1) in space by overwriting values of sub into original nums array.
"""


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []
        for num in nums:
            if len(sub) == 0 or sub[-1] < num:
                sub.append(num)
            else:
                # Find the index of the smallest number >= num
                idx = bisect.bisect_left(sub, num)
                sub[idx] = num  # Replace that number with num
        return len(sub)


"""
5- There is another crazy idea using Binary Index Tree or Fenwick Tree
Fenwick Tree: https://www.youtube.com/watch?v=uSFzHCZ4E-8
"""


# Function to map
# numbers using coordinate
# compression


def coordinateCompression(arr, n):

    # Set will store
    # all unique numbers
    s = dict()
    for i in range(n):
        s[arr[i]] = 1

    # Map will store
    # the new elements
    index = 0
    mp = dict()

    for itr in sorted(s):

        # For every new number in the set,
        index += 1

        # Increment the index of the
        # current number and store it
        # in a hashmap. Here index
        # for every element is the
        # new value with with the
        # current element is replaced
        mp[itr] = index
    for i in range(n):

        # now change the current element
        # to range 1 to N.
        arr[i] = mp[arr[i]]

# Function to calculate
# length of maximum
# increasing sequence till
# i'th index


def query(BIT, index, n):

    ans = 0
    while (index > 0):
        ans = max(ans, BIT[index])

        # Go to parent node
        index -= index & (-index)
    return ans

# Function for updating
# BIT array for maximum
# increasing sequence till
# i'th index


def update(BIT, index, n):

    # If 4 is inserted in BIT,
    # check for maximum length
    # subsequence till element 3.
    # Let this subsequence length be x.
    # If x + 1 is greater than
    # the current element in BIT,
    # update the BIT array
    x = query(BIT, index - 1, n)
    value = x + 1
    while (index <= n):

        # Store maximum length subsequence length till index
        # Here index is the
        # coordinate compressed element
        BIT[index] = max(BIT[index], value)

        # Go to child node and update that node
        index += index & (-index)

# Function to calculate
# maximum Longest Increasing
# Sequence length


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        coordinateCompression(nums, n)
        BIT = [0]*(n + 1)

        for i in range(n):
            # Add elements
            # from left to right
            # in BIT
            update(BIT, nums[i], n)

        ans = query(BIT, n, n)
        return ans
