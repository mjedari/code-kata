"""
https://leetcode.com/problems/number-of-operations-to-make-network-connected/

There are n computers numbered from 0 to n - 1 connected by ethernet cables connections forming a network where connections[i] = [ai, bi] represents a connection between computers ai and bi. Any computer can reach any other computer directly or indirectly through the network.

You are given an initial computer network connections. You can extract certain cables between two directly connected computers, and place them between any pair of disconnected computers to make them directly connected.

Return the minimum number of times you need to do this in order to make all the computers connected. If it is not possible, return -1.



"""


from typing import List
from collections import defaultdict


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:

        # IF WE DON'T HAVE AT LEAST N - 1 CABLES, IT IS IMPOSSIBLE TO CONNECT THE GRAPH
        if len(connections) < n - 1:
            return -1

        # CREATE THE (UNDIRECTED) GRAPH
        graph = self.createGraph(connections)
        # print(f"Graph : {graph}\n")

        # FIND NUMBER OF COMPONENTS
        numComponents = self.findNumComponents(n, graph)
        # print(f"numComponents : {numComponents}")

        # RETURN THE NUMBER OF COMPONENTS IN THE GRAPH
        return numComponents - 1

    def createGraph(self, connections):
        graph = defaultdict(set)
        for c in connections:
            graph[c[0]].add(c[1])
            graph[c[1]].add(c[0])
        return graph

    def findNumComponents(self, n, graph):
        numComponents = 0
        visited = set()
        for i in range(n):
            if i not in visited:
                self.dfs(graph, i, visited)
                numComponents += 1
        return numComponents

    def dfs(self, graph, i, visited):

        # BASE CASE
        if i in visited:
            return

        # ADD I TO VISITED
        visited.add(i)

        # VISIT ALL NEIGHBORS
        for nb in graph.get(i, []):
            self.dfs(graph, nb, visited)
