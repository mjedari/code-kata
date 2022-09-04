"""
https://leetcode.com/problems/path-sum-ii

Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.


"""

# Definition for a binary tree node.
from typing import List, Optional
"""
NOTE : it should be so_far + [node.left.val] not so_far.append(node.left.val)
"""

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        if not root:
            return

        q = [(root, [root.val])]
        res = []

        while q:
            node, so_far = q.pop(0)

            if not node.left and not node.right and sum(so_far) == targetSum:
                res.append(so_far)

            if node.left:
                q.append((node.left, so_far + [node.left.val]))

            if node.right:
                q.append((node.right, so_far + [node.right.val]))

        return res
