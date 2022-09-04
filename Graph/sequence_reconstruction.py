"""
PREMIUM required: https://leetcode.com/problems/sequence-reconstruction/

Check whether the original sequence `org` can be uniquely reconstructed from the sequences in `seqs`. 
The org sequence is a permutation of the integers from 1 to n, with 1 ≤ n ≤ 104. 
Reconstruction means building a shortest common supersequence of the sequences in seqs (i.e., a shortest sequence so that all sequences in seqs are subsequences of it). 
Determine whether there is only one sequence that can be reconstructed from seqs and it is the org sequence.

Example 1:
    Input: org: [1,2,3], seqs: [[1,2],[1,3]]
    Output: false
    Explanation: [1,2,3] is not the only one sequence that can be reconstructed, because [1,3,2] is also a valid sequence that can be reconstructed.

Example 2:
    Input: org: [1,2,3], seqs: [[1,2]]
    Output: false
    Explanation: The reconstructed sequence can only be [1,2].

Example 3:
    Input: org: [1,2,3], seqs: [[1,2],[1,3],[2,3]]
    Output: true
    Explanation: The sequences [1,2], [1,3], and [2,3] can uniquely reconstruct the original sequence [1,2,3].

Example 4:
    Input: org: [4,1,5,2,6,3], seqs: [[5,2,6,3],[4,1,5,2]]
    Output: true
"""

from typing import Dict, List
from collections import deque
from functools import reduce


class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        graph = self.build_graph(seqs)
        topological_order = self.topological_sort(graph)

        return topological_order == org

    def build_graph(self, seqs: List[List[int]]) -> Dict[int, set]:
        graph = {}

        for seq in seqs:
            for node in seq:
                if node not in graph:
                    graph[node] = set()
        for seq in seqs:
            for i in range(1, len(seq)):
                graph[seq[i - 1]].add(seq[i])

        return graph

    def topological_sort(self, graph: Dict[int, set]) -> List[int]:

        in_degrees = {
            node: 0 for node in graph
        }

        for node in graph:
            for neighbor in graph[node]:
                in_degrees[neighbor] += 1

        topological_order = []
        queue = deque()
        for node in graph:
            if in_degrees[node] == 0:
                queue.append(node)

        while queue:
            if len(queue) > 1:
                return None

            node = queue.popleft()
            topological_order.append(node)

            for neighbor in graph[node]:
                in_degrees[neighbor] -= 1
                if in_degrees[neighbor] == 0:
                    queue.append(neighbor)

        if len(topological_order) == len(graph):
            return topological_order

        return None


class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        # edge case handling
        # org: [1,2,3], seqs: [[1,2]]
        # since 3 isn't in seqs we don't have enough information for construct order
        nodes = reduce(set.union, seqs, set())
        if nodes != set(org):
            return False

        # graph processing
        n = len(org)
        out_degrees = [[] for _ in range(n+1)]
        in_degrees = [0 for _ in range(n+1)]

        for seq in seqs:
            # For every (from, to) in seq
            # Append to out_degrees[from]
            # Increase in_degrees[to]
            for f, t in zip(seq, seq[1:]):
                out_degrees[f].append(t)
                in_degrees[t] + 1

        # bfs search to find the unique topological sort order
        # sources: nodes with in_degrees == 0
        queue = [node for node in org if in_degrees == 0]
        order = []

        while queue:
            # at any time we have more that 1 item in q, it means we can't recognize the order
            if len(queue) != 1:
                return False

            node = queue.pop()
            order.append(node)

            for next_node in out_degrees[node]:
                in_degrees[next_node] -= 1
                if not in_degrees[next_node]:
                    queue.append(next_node)

        return org == order
