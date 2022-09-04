"""
https://leetcode.com/problems/kth-largest-element-in-an-array/

Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.


"""
import heapq
from typing import List
import random
"""
1- Heap
"""


# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         return heapq.nlargest(k, nums)[-1]


"""
2- Sort
"""


# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         return sorted(nums, reverse=True)[k-1]


"""
3- Quick select

If you see this problem in competition, the best way just to sort data and choose k-th largest element in O(n log n) overall complexity. However you can imagine, that it is not the good idea for real interview, where your expected do do something else. There is two classical ways how to find order statistic in linear time (yes, it has its mathematical name):

    1- Median of median approach with worst time complexity O(n), however it is quite painful to code and I do not think anyone expect that you do it.
    2- So-called Quick Select, which use similar idea to Quick Sort, with average complexity O(n).

Quick Select:
    1- First, we need to choose so-called pivot and partition element of nums into 3 parts: elements, smaller than pivot, equal to pivot and bigger than pivot. (sometimes two groups enough: less and more or equal)
    2- Next step is to see how many elements we have in each group: if k <= L, where L is size of left, than we can be sure that we need to look into the left part. If k > L + M, where M is size of mid group, than we can be sure, that we need to look into the right part. 
    3- Finally, if none of these two conditions holds, we need to look in the mid part, but because all elements there are equal, we can immediately return mid[0].
    
Complexity
    time complexity is O(n) in average, because on each time we reduce searching range approximately 2 times. This is not strict proof, for more details you can do some googling. Space complexity is O(n) as well.

"""


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:
            return
        pivot = random.choice(nums)
        left = [x for x in nums if x > pivot]
        mid = [x for x in nums if x == pivot]
        right = [x for x in nums if x < pivot]

        L, M = len(left), len(mid)

        if k <= L:
            return self.findKthLargest(left, k)
        elif k > L + M:
            return self.findKthLargest(right, k - L - M)
        else:
            return mid[0]
