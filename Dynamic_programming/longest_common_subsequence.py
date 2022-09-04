"""
https://leetcode.com/problems/longest-common-subsequence/
"""

"""

1- DP

The ith row and jth column shows the length of the LCS between X_{1..i} and Y_{1..j}.

If a[i] == b[j]
    LCS for i and j would be 1 plus LCS till the i-1 and j-1 indexes.
else
    we will take the largest LCS if we skip a character from one of the string (max(m[i - 1][j], m[i][j - 1]).

Example
    "abcde"
    "ace"
    
[        a  c  e  
     [0, 0, 0, 0], 
  a  [0, 1, 1, 1], 
  b  [0, 1, 1, 1], 
  c  [0, 1, 2, 2], 
  d  [0, 1, 2, 2], 
  e  [0, 1, 2, 3]
]


"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

        for i, c in enumerate(text1, 1):
            for j, d in enumerate(text2, 1):
                if c == d:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        print(dp)
        return dp[-1][-1]


"""
2- DFS 
    Time Limit Exceeded
    Input
        "ylqpejqbalahwr"
        "yrkzavgdmdgtqpg"
    
  With memo ~3 seconds
"""

# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         return self.helper(text1, text2, 0, 0)

#     @cache
#     def helper(self, s1, s2, i, j):
#         if i == len(s1) or j == len(s2):
#             return 0
#         if s1[i] == s2[j]:
#             return 1 + self.helper(s1, s2, i + 1, j + 1)
#         else:
#             return max(self.helper(s1, s2, i+1, j), self.helper(s1, s2, i, j + 1))
