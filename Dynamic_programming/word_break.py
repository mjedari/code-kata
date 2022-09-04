"""
https://leetcode.com/problems/word-break/


Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

"""

from typing import List

# TIME LIMIT EXCEEDED:
# https://www.educative.io/blog/crack-amazon-coding-interview-questions
# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         for i in range(1, len(s) + 1):
#             first = s[:i]
#             if first in wordDict:
#                 second = s[i:]
#                 if not second or second in wordDict or self.wordBreak(second, wordDict):
#                     return True

#         return False

"""
1- DP

    dp is an array that contains booleans

    dp[i] is True if there is a word in the dictionary that ends at ith index of s AND dp is also True at the beginning of the word

    Example:

        s = "leetcode"
        words = ["leet", "code"]

        dp[3] is True because there is "leet" in the dictionary that ends at 3rd index of "leetcode"
        dp[7] is True because there is "code" in the dictionary that ends at the 7th index of "leetcode" AND dp[3] is True

        The result is the last index of dp.

"""
# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#  	    dp = [False] * len(s)
#  	    for i in range(len(s)):
#  		    for w in wordDict:
#  			    if w == s[i-len(w)+1:i+1] and (dp[i-len(w)] or i-len(w) == -1):
#  				    dp[i] = True
#  	    return dp[-1]


"""
2- DFS: Branching on words in wordDict

"""


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        visited = set()

        def dfs(s, wordDict):
            if s == '':
                return True
            for word in wordDict:
                l = len(word)
                # To prune visited path (i.e NO time limit exceeded anymore)
                if s[:l] == word and s[l:] not in visited:
                    ans = dfs(s[l:], wordDict)
                    visited.add(s[l:])
                    if ans:
                        return ans
                else:
                    continue
            return False

        return dfs(s, wordDict)


"""
3- DFS: Branching on s chars

"""
# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         words = set(wordDict)
#         solutions = {'':False}

#         def dfs(st):
#             if st in words:
#                 return True
#             elif st in solutions:
#                 return solutions[st]

#             for i in range(len(st)):
#                 if dfs(st[:i]) and dfs(st[i:]):
#                     solutions[st] = True
#                     return True

#             solutions[st] = False
#             return False

#         return dfs(s)
