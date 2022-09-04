"""
https://leetcode.com/problems/search-in-rotated-sorted-array/

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.


"""
from typing import List

"""
Idea:
    We have an ascending array, which is rotated at some pivot.
    Let's call the rotation the inflection point. (IP)
    One characteristic the inflection point holds is: arr[IP] > arr[IP + 1] and arr[IP] > arr[IP - 1]
    So if we had an array like: [7, 8, 9, 0, 1, 2, 3, 4] the inflection point, IP would be the number 9.

    One thing we can see is that values until the IP are ascending. And values from IP + 1 until end are also ascending (binary search, wink, wink).
    Also the values from [0, IP] are always bigger than [IP + 1, n].

intuition:
    We can perform a Binary Search.
    If A[mid] is bigger than A[left] we know the inflection point will be to the right of us, meaning values from a[left]...a[mid] are ascending.

    So if target is between that range we just cut our search space to the left.
    Otherwise go right.

    The other condition is that A[mid] is not bigger than A[left] meaning a[mid]...a[right] is ascending.
    In the same manner we can check if target is in that range and cut the search space correspondingly.

Time complexity: O(logn)
Space complexity: O(1)
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n - 1
        if n == 0: return -1
        
        while left <= right:
            mid = (right + left) // 2
            if nums[mid] == target: return mid
            
            # inflection point to the right. Left is strictly increasing
            if nums[mid] >= nums[left]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
                    
            # inflection point to the left of me. Right is strictly increasing
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            
        return -1