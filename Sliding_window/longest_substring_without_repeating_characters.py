"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string s, find the length of the longest substring without repeating characters.
"""


"""
"abcabcbb"

left right ans seen

0 0 0 {}
0 0 1 {'a': 1}
----------------------------------------
0 1 1 {'a': 1}
0 1 2 {'a': 1, 'b': 2}
----------------------------------------
0 2 2 {'a': 1, 'b': 2}
0 2 3 {'a': 1, 'b': 2, 'c': 3}
----------------------------------------
0 3 3 {'a': 1, 'b': 2, 'c': 3}
1 3 3 {'a': 4, 'b': 2, 'c': 3}
----------------------------------------
1 4 3 {'a': 4, 'b': 2, 'c': 3}
2 4 3 {'a': 4, 'b': 5, 'c': 3}
----------------------------------------
2 5 3 {'a': 4, 'b': 5, 'c': 3}
3 5 3 {'a': 4, 'b': 5, 'c': 6}
----------------------------------------
3 6 3 {'a': 4, 'b': 5, 'c': 6}
5 6 3 {'a': 4, 'b': 7, 'c': 6}
----------------------------------------
5 7 3 {'a': 4, 'b': 7, 'c': 6}
7 7 3 {'a': 4, 'b': 8, 'c': 6}
----------------------------------------

                
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        seen = {}

        left = 0
        for right in range(len(s)):
            if s[right] in seen:
                left = max(seen[s[right]], left)

            ans = max(ans, right - left + 1)
            seen[s[right]] = right + 1

        return ans
