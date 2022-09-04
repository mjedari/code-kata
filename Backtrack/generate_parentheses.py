"""
https://leetcode.com/problems/generate-parentheses/

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
"""


from typing import List
from itertools import permutations


"""
1- Brute force, all combination: TIME LIMIT EXCEEDED
"""


# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#         parans = '(' * n + ')' * n

#         all_comb = set(["".join(comb) for comb in permutations(parans)])

#         return [comb for comb in all_comb if self.is_balance(comb)]

#     def is_balance(self, parans: str) -> bool:
#         stack: List[str] = []
#         for paran in parans:
#             if paran == "(":
#                 stack.append(paran)
#             elif stack:
#                 stack.pop()

#         return len(stack) == 0


"""
2- General Backtrack
    `stack` to keep track of each iteration
    `res` to accumulate answers

n = 3

[]
['(']
['(', '(']
['(', '(', '(']
['(', '(', '(', ')']
['(', '(', '(', ')', ')']
['(', '(', '(', ')', ')', ')']
['(', '(', ')']
['(', '(', ')', '(']
['(', '(', ')', '(', ')']
['(', '(', ')', '(', ')', ')']
['(', '(', ')', ')']
['(', '(', ')', ')', '(']
['(', '(', ')', ')', '(', ')']
['(', ')']
['(', ')', '(']
['(', ')', '(', '(']
['(', ')', '(', '(', ')']
['(', ')', '(', '(', ')', ')']
['(', ')', '(', ')']
['(', ')', '(', ')', '(']
['(', ')', '(', ')', '(', ')']

"""


# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#         stack = []
#         res = []

#         def backtrack(openN: int, closedN: int):
#             if openN == closedN == n:
#                 res.append("".join(stack))
#                 return

#             if openN < n:
#                 stack.append("(")
#                 backtrack(openN + 1, closedN)
#                 stack.pop()

#             if closedN < openN:
#                 stack.append(")")
#                 backtrack(openN, closedN + 1)
#                 stack.pop()

#         backtrack(0, 0)
#         return res


"""
3 - Backtrack, 
    `s` (ans) is modifying, passed as parameter

Only add open paranthesis if open < n
Only add a closing paranthesis if closed < open
Valid IIF open == closed == n


(
((
(((
((()
((())
((()))
(()
(()(
(()()
(()())
(())
(())(
(())()
()
()(
()((
()(()
()(())
()()
()()(
()()()

"""


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(s='', left=0, right=0):
            if len(s) == 2 * n:
                ans.append(s)
                return
            if left < n:
                backtrack(s + '(', left+1, right)
            if right < left:
                backtrack(s + ')', left, right+1)

        backtrack()
        return ans
