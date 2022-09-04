"""
https://leetcode.com/problems/path-sum-iii/

Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

https://leetcode.com/problems/path-sum-iii/discuss/141424/

"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.ans = 0

        self.dfs(root, targetSum)

        return self.ans

    def dfs(self, root: Optional[TreeNode], targetSum: int) -> None:
        if not root:
            return

        self.check_sum(root, targetSum)
        self.dfs(root.left, targetSum)
        self.dfs(root.right, targetSum)

    def check_sum(self, root: Optional[TreeNode], targetSum: int) -> None:
        if not root:
            return

        if root.val == targetSum:
            self.ans += 1

        self.check_sum(root.left, targetSum - root.val)
        self.check_sum(root.right, targetSum - root.val)
