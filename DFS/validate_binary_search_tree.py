"""
https://leetcode.com/problems/validate-binary-search-tree/

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
"""


# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
1- DFS, in order, check for order without sorting
"""


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True

        def dfs(root: TreeNode, path: List[int]):
            if root:
                dfs(root.left, path)
                path.append(root.val)
                dfs(root.right, path)

        path = []
        dfs(root, path)

        for i in range(1, len(path)):
            if path[i-1] >= path[i]:
                return False

        return True


"""
2- DFS
"""


# class Solution:
#     def isValidBST(self, root: TreeNode) -> bool:
#         return self.dfs(root, float("inf"), float("-inf"))

#     # lo -> all nodes in the the current subtree must be smaller than this value
#     # hi -> all nodes in the the current subtree must be greater than this value
#     def dfs(self, node, lo, hi):
#         if node == None:
#             return True

#         if node.val <= hi or node.val >= lo:
#             return False

#         return self.dfs(node.left, min(lo, node.val), hi) and \
#             self.dfs(node.right, lo, max(node.val, hi))
