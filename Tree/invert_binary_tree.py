"""
https://leetcode.com/problems/invert-binary-tree/

Given the root of a binary tree, invert the tree, and return its root.

"""

# Definition for a binary tree node.


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
1- DFS

NOTE: 
    - WE SHOULD SWAP VALUES like: 
        - node.left, node.right = dfs(node.right), dfs(node.left)
        or
        left = node.left
        right = node.right        
        node.left = dfs(right)
        node.right = dfs(left)
        
    - THIS WON"T WORK
        node.left = dfs(node.right)
        node.right = dfs(node.left)

"""
# class Solution:
#     def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

#         def dfs(node: Optional[TreeNode]):
#             if node:
#                 node.left, node.right = dfs(node.right), dfs(node.left)
#                 return node


#         dfs(root)
#         return root


"""
2- BFS
"""


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = [root]

        while q:
            node = q.pop(0)
            if node:
                node.left, node.right = node.right, node.left
                q += node.left, node.right
        return root
