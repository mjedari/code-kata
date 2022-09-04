"""
PREMIUM Required https://leetcode.com/problems/graph-valid-tree/

Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

Example 1:
    Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
    Output: true
Example 2:
    Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
    Output: false

"""


from typing import List
from collections import defaultdict

"""
A tree is a special undirected graph. It satisfies two properties
    It is connected
    It has no cycle.

Being Connected means you can start from any node and reach any other node. 
To prove it, we can do a DFS and add each node we visit to a set. 
After we visited all the nodes, we compare the number of nodes in the set with the total number of nodes. If they are the same then every node is accessible from any other node and the graph is connected.


To prove an undirected graph having no cycle, we can also do a DFS. If a graph contains a cycle, then we would visit a certain node more than once. THERE IS A MINOR CAVEAT, since the graph is undirected, when we visit a child we would always add parent to the next visit list. This creates a trivial cycle and not the real cycle we want. We can avoid detecting trivial cycle but adding an additional parent state in the DFS call.
We can check both properties in one DFS call since cycle detection always keeps track of a visited set.

"""


# class Solution:
#     def validTree(self, n: int, edges: List[List[int]]) -> bool:
#         graph = defaultdict(list)

#         # build the graph
#         for src, dest in edges:
#             graph[src].append(dest)
#             graph[dest].append(src)

#         visited = set()

#         def dfs(root, parent):  # returns true if graph has no cycle
#             visited.add(root)
#             for node in graph[root]:
#                 if node == parent:  # trivial cycle, skip
#                     continue
#                 if node in visited:
#                     return False

#                 if not dfs(node, root):
#                     return False
#             return True

#         return dfs(0, -1) and len(visited) == n


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)

        # build the graph
        for src, dest in edges:
            graph[src].append(dest)
            graph[dest].append(src)

        visited = set()

        def dfs(root):
            visited.add(root)
            for node in graph[root]:
                if node in visited:
                    continue
                dfs(node)

        dfs(0)
        return len(visited) == n and len(edges) == n - 1
