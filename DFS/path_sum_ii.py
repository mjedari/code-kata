"""
https://leetcode.com/problems/path-sum-ii/submissions/

Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.


"""

# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        self.dfs(root, targetSum, [], res)
        return res

    def dfs(self, root: Optional[TreeNode], targetSum: int, ls: List[int], res: List[List[int]]):
        if root:
            if not root.left and not root.right and targetSum == root.val:
                ls.append(root.val)
                res.append(ls)

            self.dfs(root.left, targetSum-root.val, ls+[root.val], res)
            self.dfs(root.right, targetSum-root.val, ls+[root.val], res)
