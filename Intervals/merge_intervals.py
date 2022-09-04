"""
https://leetcode.com/problems/merge-intervals/

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

"""

"""
[[1, 3], [2, 6], [8, 10], [15, 18]]

s   e       s <= out[-1][1]       out
2   6       2 <= 3               [[1, 3]] -> [[1, 6]]
8   10      8 <= 6               [[1, 6]] -> [[1, 6], [8, 10]]
15  18      15 <= 10             [[1, 6]] -> [[1, 6], [8, 10], [15, 18]]

"""




from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        out = []

        for s, e in sorted(intervals, key=lambda x: x[0]):
            if out and s <= out[-1][1]:
                out[-1][1] = max(e, out[-1][1])
            else:
                out.append([s, e])

        return out
