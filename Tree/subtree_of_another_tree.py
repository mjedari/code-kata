"""
https://leetcode.com/problems/subtree-of-another-tree/

Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.
"""

"""
1- DFS O(|root| * |subRoot|)
    For each node of `root`, let's check if it's subtree equals `subRoot`. We can do that in a straightforward way by an isMatch function: 
    check if `root` and `subRoot` match at the values of their roots, plus their subtrees match.
    Then, in our main function, we want to check if `root` and `subRoot` match, or if t is a subtree of a child of s.
"""

# Definition for a binary tree node.




from typing import Optional
from hashlib import sha256
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not root:
            return False

        def isMatch(r, s):
            if not r or not s:
                return r is s

            return r.val == s.val and isMatch(r.left, s.left) and isMatch(r.right, s.right)

        if isMatch(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


"""
2- Merkle hashing O(|s| + |t|):

    For each node in a tree, we can create node.merkle, a hash representing it's subtree.
    This hash is formed by hashing the concatenation of the merkle of the left child, the node's value, and the merkle of the right child. 
    Then, two trees are identical if and only if the merkle hash of their roots are equal (except when there is a hash collision.) 
    From there, finding the answer is straightforward: we simply check if any node in s has node.merkle == t.merkle
"""


# class Solution:
#     def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
#         def hash_(x):
#             hash_object = sha256(str(x).encode('utf-8'))
#             return hash_object.hexdigest()

#         def merkle(node):
#             if not node:
#                 return '#'
#             m_left = merkle(node.left)
#             m_right = merkle(node.right)
#             node.merkle = hash_(m_left + str(node.val) + m_right)
#             return node.merkle

#         merkle(root)
#         merkle(subRoot)

#         def dfs(node):
#             if not node:
#                 return False
#             return (node.merkle == subRoot.merkle or
#                     dfs(node.left) or dfs(node.right))

#         return dfs(root)
