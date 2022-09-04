"""
https://leetcode.com/problems/find-all-duplicates-in-an-array/

Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant extra space.
"""

from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        """
        With extra space: 
            prepare a hash map and count each element
            the answer is elements with count equals 2
        
        Without extra space:
            we need to use the same input (nums) as hash map
            since each elements apears only ONE or TWO times
            we can loop though the nums and make the corresponding value negative
            if we see a value already negate before we find the duplication                    
        """
        ans = []
        for i in range(len(nums)):
            map_key = abs(nums[i]) - 1 # nums[i] can be negated previously 
            
            if nums[map_key] < 0: # we've seen it before
                ans.append(abs(nums[i])) 
            else:
                nums[map_key] *= -1
        
        return ans