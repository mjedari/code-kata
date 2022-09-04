"""
https://leetcode.com/problems/binary-tree-level-order-traversal/

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
"""


from typing import Optional, List


"""
1- Clean
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# class Solution:
#     def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         if not root:
#             return []

#         ans, cur_level = [], [root]
#         while cur_level:
#             # append all value in current level
#             ans.append([node.val for node in cur_level])

#             # update cur_level to new list of non None nodes
#             level = []
#             for node in cur_level:
#                 level.extend([node.left, node.right])
#             cur_level = [leaf for leaf in level if leaf]
#         return ans


"""
2- General
"""


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        q = [[root]]
        res = []

        while q:
            nodes = q.pop()
            res.append([node.val for node in nodes])

            level = []
            for node in nodes:
                if node.left:
                    level.append(node.left)

                if node.right:
                    level.append(node.right)
            if level:
                q.append(level)

        return res
