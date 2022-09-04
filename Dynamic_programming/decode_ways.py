"""
https://leetcode.com/problems/decode-ways/

A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

The test cases are generated so that the answer fits in a 32-bit integer.


"""


"""
1- DP
    Problem Reduction: variation of n-th staircase with n = [1, 2] steps.

    The tricky part is handling the corner cases (e.g. s = "30").

    Let dp[ i ] = the number of ways to parse the string s[0: i + 1]

    For example: s = "231"
    
    DP
        index 0: extra base offset. dp[0] = 1
        index 1: # of ways to parse "2" => dp[1] = 1
        index 2: # of ways to parse "23" => "2" and "23", dp[2] = 2
        index 3: # of ways to parse "231" => "2 3 1" and "23 1" => dp[3] = 2

"""


class Solution:
    def numDecodings(self, s: str) -> int:

        if not s or s[0] == "0":
            return 0

        dp = [0 for x in range(len(s) + 1)]

        # base case initialization
        dp[0] = 1
        dp[1] = 1

        for i in range(2, len(s) + 1):
            # One step jump
            if 0 < int(s[i-1:i]) <= 9:
                dp[i] += dp[i - 1]
            # Two step jump
            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i - 2]
        return dp[len(s)]
