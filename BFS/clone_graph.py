"""
https://leetcode.com/problems/clone-graph/

Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.
"""


# Definition for a Node.
import collections


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


"""
1- Clean
"""


# class Solution:
#     def cloneGraph(self, node: Node) -> Node:

#         if not node:
#             return node

#         res = {node: Node(node.val)}
#         q = collections.deque([node])

#         while q:
#             n = q.popleft()
#             for nbr in n.neighbors:
#                 if nbr not in res:
#                     res[nbr] = Node(nbr.val)
#                     q.append(nbr)
#                 res[n].neighbors.append(res[nbr])

#         return res[node]


"""
2- General
"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':

        if not node:
            return node

        cloned = {node: Node(node.val)}
        q = [node]

        while q:
            n = q.pop()

            for nbr in n.neighbors:
                if nbr not in cloned:
                    cloned[nbr] = Node(nbr.val)
                    q.append(nbr)

                cloned[n].neighbors.append(cloned[nbr])

        return cloned[node]
