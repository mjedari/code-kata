"""
https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.



"""


"""

NOTE: we can construct a Binary Tree from one traversal only (Inorder or Postorder or Preorder) but we cannot construct an **unique** Binary Tree from a single traversal (inorder or preorder or postorder)
https://www.quora.com/What-is-the-method-to-construct-a-binary-tree-when-postorder-and-preorder-is-given

case 1: 
 
    1 
   / 
  2 
 / 
3 
preorder:  1 2 3 
postorder: 3 2 1 
----------------------- 
case 2: 
 
 1 
  \ 
   2 
    \ 
     3 
preorder:  1 2 3 
postorder: 3 2 1 


For this problem we are adding extra "#" to the preorder then, we can treat it as full binary tree

               1
             /   \
            /     \
           2       3
          /      /   \
         /      /     \
        4      5       6
              / \
             /   \
            7     8

LC input: [1, 2, 3, 4, null, 5, 6, null, null, 7, 8, null, null]

We can't b

serialize:
  Preorder with # : 1 2 4 # # # 3 5 7 # # 8 # # 6 # #

deserialize:
  iterate over preorder and build the tree from root

"""

# Definition for a binary tree node.


class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root: TreeNode) -> str:
        def dfs(node):
            if node:
                pre_order.append(str(node.val))
                dfs(node.left)
                dfs(node.right)
            else:
                pre_order.append('#')
        pre_order = []
        dfs(root)
        return ' '.join(pre_order)

    def deserialize(self, data: str) -> TreeNode:
        def dfs():
            val = next(pre_order)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node
        pre_order = iter(data.split())
        return dfs()


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
