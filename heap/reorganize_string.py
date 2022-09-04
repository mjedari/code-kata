"""
https://leetcode.com/problems/reorganize-string/

Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.
Return any possible rearrangement of s or return "" if not possible.
"""

import collections
import heapq

"""
1- heap

    The core idea is to alternatively popping out the most frequent letter.
    `pre` is used to store the most recent popped out item.
"""


class Solution:
    def reorganizeString(self, s: str) -> str:
        if s == "":
            return ""

        d = collections.Counter(s)

        heap = []
        for key, value in d.items():
            heapq.heappush(heap, [-value, key])

        res = ""
        pre = heapq.heappop(heap)
        res += pre[1]

        while heap:
            cur = heapq.heappop(heap)
            res += cur[1]

            pre[0] += 1
            if pre[0] < 0:
                heapq.heappush(heap, pre)
            pre = cur

        if len(res) != len(s):
            return ""
        else:
            return res


"""
2- Iterative

    Put the least common letters at the odd indexes and put the most common letters at the even indexes (both from left to right in order of frequency).
    The task is only impossible if some letter appears too often, in which case it'll occupy all of the even indexes and at least the last odd index, so I check the last two indexes.
"""


# class Solution:
#     def reorganizeString(self, s: str) -> str:
#         a = sorted(sorted(s), key=s.count)

#         h = len(a) // 2

#         a[1::2], a[::2] = a[:h], a[h:]
#         return ''.join(a) * (a[-1:] != a[-2:-1])
