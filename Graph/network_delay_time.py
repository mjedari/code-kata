"""
https://leetcode.com/problems/network-delay-time/


You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.


"""

from typing import List
import collections
import heapq

"""
1- Dijkstra

Dijkstra's algorithm solves the shortest-path problem for any weighted, directed graph with non-negative weights. It can handle graphs consisting of cycles, but negative weights will cause this algorithm to produce incorrect results

Time: O(E+VlogV)
Space: O(V+E)

[[2,1,1],[2,3,1],[3,4,1]], 4, 2

#1 Build a graph:     
    {
        2: {1: 1, 3: 1}, 
        3: {4: 1}
    }

#2 push into the heap
    heap = [(distance, node)]
    
#3 pop from heap

#4 push unvisited neighbors and their distance to the heap
    
"""


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(dict)

        for u, v, w in times:
            graph[u][v] = w

        heap = [(0, k)]  # (delay time, node)
        seen = {}
        while heap:
            time, node = heapq.heappop(heap)
            if node not in seen:
                seen[node] = time
                for nbr in graph[node]:
                    heapq.heappush(heap, (seen[node] + graph[node][nbr], nbr))

        return max(seen.values()) if len(seen) == n else -1


"""
2- Bellman-Ford
Time: O(VE)
Space: O(N)

https://www.youtube.com/watch?v=FtN3BYH2Zes

#1 Prepare distance map of each node to `inf` and the start node to 0
#2 For all edges we repeat a relaxation fot |v| - 1 times


# 3 Relaxation u and v with distance d
    if dist[u] + d < dist[v] then dist[v] = dist[u] + d
"""

# class Solution:
#     def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

#         dist = {v: float("inf") for v in range(1, n+1)}
#         dist[k] = 0

#         for _ in range(n-1):
#             for u, v, d in times:
#                 if dist[u] + d < dist[v]:
#                     dist[v] = dist[u] + d

#         return max(dist.values()) if max(dist.values()) < float("inf") else -1

"""
3- Floyd-Warshall
Time: O(V^3)
Space: O(V^2)

https://www.youtube.com/watch?v=oNI0rf2P9gE

#1 Prepare distance matrix N x N
#2 Set the Diagonal 0
#3 update the distance for i and j considering k as intermediate node

    dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
"""


# class Solution:
#     def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
#         dist = [[float("inf") for _ in range(N)] for _ in range(N)]

#         for u, v, w in times:
#             dist[u-1][v-1] = w

#         for i in range(N):
#             dist[i][i] = 0

#         for k in range(N):
#             for i in range(N):
#                 for j in range(N):
#                     dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])

#         return max(dist[K-1]) if max(dist[K-1]) < float("inf") else -1
