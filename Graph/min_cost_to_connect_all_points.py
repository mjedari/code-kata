"""
https://leetcode.com/problems/min-cost-to-connect-all-points/submissions/

You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

 
"""
"""
1- Prim's Algorithm

Time: O(ElogV) = O(N^2 * logN), where N <= 1000 is number of points.
Space: O(N)

https://www.youtube.com/watch?v=4ZlRH0eK-qQ

#1 Build a graph and distance matrix: [[0,0],[2,2],[3,10],[5,2],[7,0]]

[
    [[1, 4], [2, 13], [3, 7], [4, 7]], 
    [[0, 4], [2, 9], [3, 3], [4, 7]], 
    [[0, 13], [1, 9], [3, 10], [4, 14]], 
    [[0, 7], [1, 3], [2, 10], [4, 4]], 
    [[0, 7], [1, 7], [2, 14], [3, 4]]
]

#2 start with first node, pop it from heap (i.e it will be pop the smallest one)

#3 accumulate the distance and return it
"""




from typing import List
import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def manhattan(p1, p2): return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

        n = len(points)
        graph = [[] for _ in range(n)]

        for i in range(n):
            for j in range(i+1, n):
                dist = manhattan(points[i], points[j])
                graph[i].append([j, dist])
                graph[j].append([i, dist])

        def prime(src):
            seen = set()
            min_heap = [[0, src]]  # pair of (dist, vertex)
            total_dist = 0
            while len(seen) < n:
                dist, u = heapq.heappop(min_heap)
                if u not in seen:
                    seen.add(u)
                    total_dist += dist
                    for v, d in graph[u]:
                        if v not in seen:
                            heapq.heappush(min_heap, [d, v])
            return total_dist

        return prime(0)


"""
2- Kruskal's Algorithm (use Union-Find) 

https://www.youtube.com/watch?v=wU6udHRIkcc
"""

# class UnionFind:
#     def __init__(self, n):
#         self.parent = [i for i in range(n)]

#     def find(self, u):
#         if u != self.parent[u]:
#             self.parent[u] = self.find(self.parent[u])
#         return self.parent[u]

#     def union(self, u, v):
#         pu, pv = self.find(u), self.find(v)
#         if pu == pv: return False
#         self.parent[pu] = pv
#         return True

# class Solution:
#     def minCostConnectPoints(self, points: List[List[int]]) -> int:
#         manhattan = lambda p1, p2: abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

#         edges = []
#         n = len(points)
#         for i in range(n):
#             for j in range(i + 1, n):
#                 edges.append([manhattan(points[i], points[j]), i, j])

#         edges.sort()  # Sort increasing order by dist
#         uf = UnionFind(n)
#         ans = 0
#         for d, u, v in edges:
#             if uf.union(u, v):
#                 ans += d
#                 n -= 1
#             if n == 1: break  # a bit optimize when we found enough n-1 edges!
#         return ans
