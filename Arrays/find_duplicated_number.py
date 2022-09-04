"""
https://leetcode.com/problems/find-the-duplicate-number/

Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.
"""

"""
Similar to detect a cycle in a linked list (Floyd’s Cycle Detection Algorithm)

https://www.techiedelight.com/detect-cycle-linked-list-floyds-cycle-detection-algorithm/

Only cycle detection isn't enough:
[2,5,9,6,9,3,8,9,7,1]
          

f s
---
0 0
1 3
3 4
2 4

f c
---
7 2
9 9

Why floyds algorithm works?
https://www.codingninjas.com/blog/2020/09/09/floyds-cycle-detection-algorithm/
"""




from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # start hopping from Node_#0
        slow, fast = 0, 0

        # Step_#1
        # Cycle detection
        # Let slow jumper and fast jumper meet somewhere in the cycle
        while True:

            # slow jumper hops 1 step, while fast jumper hops two steps forward.
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        # Step_#2
        # Locate the start node of cycle (i.e., the duplicate number)
        check = 0
        while True:

            slow = nums[slow]
            check = nums[check]

            if slow == check:
                break

        return check
