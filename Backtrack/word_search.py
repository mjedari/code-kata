"""
https://leetcode.com/problems/word-search/

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
"""

from typing import List


"""
1- Backtrack: compress version
"""


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def is_in_board(p: int, q: int) -> bool:
            return 0 <= p < n and 0 <= q < m

        def f(i: int, j: int, word: str):
            if len(word) == 0:
                return True
            if not is_in_board(i, j) or board[i][j] != word[0]:
                return False

            tmp = board[i][j]
            board[i][j] = "#"
            rem = word[1:]
            res = f(i+1, j, rem) or f(i-1, j, rem) or f(i,
                                                        j+1, rem) or f(i, j-1, rem)
            board[i][j] = tmp

            return res

        n = len(board)
        m = len(board[0])

        for i in range(n):
            for j in range(m):
                if f(i, j, word):
                    return True
        return False


"""
2- Backtrack: extended version
"""


# class Solution:
#     def exist(self, board: List[List[str]], word: str) -> bool:
#         if not board:
#             return False

#         self.board = board
#         for i in range(len(board)):
#             for j in range(len(board[0])):
#                 if self.dfs(i, j, word):
#                     return True
#         return False

#     # check whether can find word, start at (i,j) position
#     def dfs(self, i: int, j: int, word: str):
#         if len(word) == 0:  # all the characters are checked
#             return True

#         if not self.is_in_board(i, j) or word[0] != self.board[i][j]:
#             return False

#         # first character is found, check the remaining part
#         tmp = self.board[i][j]
#         self.board[i][j] = "#"  # avoid visit again
#         rem_chars = word[1:]

#         # check whether can find "word" along one direction
#         res = self.dfs(i - 1, j, rem_chars) or self.dfs(i + 1, j, rem_chars) or self.dfs(
#             i, j - 1, rem_chars) or self.dfs(i, j + 1, rem_chars)

#         self.board[i][j] = tmp  # update the board to original value

#         return res

#     def is_in_board(self, i: int, j: int) -> bool:
#         return i >= 0 and i < len(self.board) and j >= 0 and j < len(self.board[0])
