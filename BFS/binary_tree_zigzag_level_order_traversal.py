"""
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).
"""


# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
1- General
"""


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return

        q = [[root]]
        direction = 1
        res = []
        while q:
            nodes = q.pop()

            res.append([node.val for node in nodes][::direction])
            direction *= -1

            next_level = []
            for node in nodes:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            if next_level:
                q.append(next_level)

        return res


"""
2- Clean
"""


# class Solution:
#     def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         if not root:
#             return []

#         res, level, direction = [], [root], 1

#         while level:
#             res.append([n.val for n in level][::direction])
#             direction *= -1
#             level = [kid for node in level for kid in (
#                 node.left, node.right) if kid]
#         return res
