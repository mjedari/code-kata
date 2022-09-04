"""
https://leetcode.com/problems/kth-smallest-element-in-a-bst/

Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

"""
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
1- DFS, in order

Time complexity : O(N) to build a traversal.
Space complexity : O(N) to keep an inorder traversal.
"""
# class Solution:
#     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:


#         def inorder(r):
#             return inorder(r.left) + [r.val] + inorder(r.right) if r else []

#         return inorder(root)[k - 1]

"""
2: Iterative Inorder Traversal

Time complexity: O(H + k), where H is a tree height
Space complexity: O(H) to keep the stack
"""
# class Solution:
#     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
#         stack = []

#         while True:
#             while root:
#                 stack.append(root)
#                 root = root.left
#             root = stack.pop()
#             k -= 1
#             if not k:
#                 return root.val
#             root = root.right


"""
3: Iterative inorder by Python generators
"""


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def traverse(node):
            if node:
                yield from traverse(node.left)
                yield node
                yield from traverse(node.right)

        k -= 1
        for i, node in enumerate(traverse(root)):
            if i == k:
                return node.val
