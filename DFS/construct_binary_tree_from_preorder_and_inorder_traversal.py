"""
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/


Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.


"""

# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
1- General    
    https://github.com/labuladong/fucking-algorithm/blob/english/think_like_computer/Framework%20and%20thoughts%20about%20learning%20data%20structure%20and%20algorithm.md    
"""


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder and not inorder:
            return None

        if len(preorder) == len(inorder) == 1:
            return TreeNode(preorder[0])

        root_data = preorder[0]
        root_index = inorder.index(root_data)

        left = self.buildTree(
            preorder[1:root_index + 1], inorder[0:root_index])
        right = self.buildTree(
            preorder[root_index + 1:], inorder[root_index + 1:])

        return TreeNode(root_data, left, right)


"""
2- Clean
"""
# class Solution:
#     def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
#         if inorder:
#             root_idx = inorder.index(preorder.pop(0))
#             root = TreeNode(inorder[root_idx])
#             root.left = self.buildTree(preorder, inorder[0:root_idx])
#             root.right = self.buildTree(preorder, inorder[root_idx+1:])
#             return root
