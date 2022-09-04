"""
https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

"""
from typing import List


"""
1- Greedy

    - Sort intervals by starting value (desending)
    - Only count valid intervals we need, and skip overlapping intervals

Example:
    Input
    [[10,16],[2,8],[1,6],[7,12]]
    
    
    Sorted Input
    [[10, 16], [7, 12], [2, 8], [1, 6]]
    
    shoot   start   end     shoot > end
    inf     10      16          True
    10      7       12          False
    10      2       8           True
    8       1       6           False
    
    return count of True => 2
    
"""


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        ret, shoot = 0, float('inf')
        for s, e in sorted(points, reverse=True):
            if shoot > e:
                shoot = s
                ret += 1
        return ret
