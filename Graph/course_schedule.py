"""
https://leetcode.com/problems/course-schedule/


There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.


"""

"""
Topological Sort
The aim of topological sort is to provide a partial ordering among the vertices of the graph such that if there is an edge from U to V then U <= V, which means, U comes before V in the ordering.

- Source: Any node that has no incoming edge and has only outgoing edges is called a source.
- Sink: Any node that has only incoming edges and no outgoing edge is called a sink.
- Topological ordering starts with one of the sources and ends at one of the sinks.

A topological ordering is possible only when the graph has no directed cycles, i.e. if the graph is a Directed Acyclic Graph (DAG). If the graph has a cycle, some vertices will have cyclic dependencies which makes it impossible to find a linear ordering among vertices.

a. Initialization
    We will store the graph in Adjacency Lists, which means each parent vertex will have a list containing all of its children. 
    We will do this using a Hash Table where the key will be the parent vertex number and the value will be a List containing children vertices.
    To find the sources, we will keep a Hash Table to count the in-degrees (count of incoming edges of each vertex). Any vertex with 0 in-degree will be a source.

b. Build the graph and find in-degrees of all vertices
    We will build the graph from the input and populate the in-degrees Hash Table.

c. Find all sources
    All vertices with 0 in-degrees will be our sources and we will store them in a Queue.

d. Sort
For each source:
    Add it to the sorted list.
    Get all of its children from the graph.
    Decrement the in-degree of each child by 1.
    If a child’s in-degree becomes 0, add it to the sources Queue.
    Repeat these steps, until the source Queue is empty.
    
    
PYTHON NOTE on defaultdict:
    DON'T use defaultdict if you plan to loop through a dictionary 

"""




from collections import deque
from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        if numCourses <= 0:
            return False

        # a. Initialization
        graph = {i: [] for i in range(numCourses)}  # adjacency list graph
        # count of incoming edges
        in_degree = {i: 0 for i in range(numCourses)}

        # b. Build the graph
        for prerequisite in prerequisites:
            parent, child = prerequisite[0], prerequisite[1]
            # put the child into it's parent's list
            graph[parent].append(child)
            in_degree[child] += 1

        # c. Find all sources
        sources = deque()
        for key in in_degree:
            if in_degree[key] == 0:
                sources.append(key)

        # d. Sort
        sorted_list = []
        while sources:
            vertex = sources.popleft()
            sorted_list.append(vertex)
            # get the node's children to decrement their in-degrees
            for child in graph[vertex]:
                in_degree[child] -= 1
                if in_degree[child] == 0:
                    sources.append(child)

        # if sorted_list does not contain all the courses, there is a cyclic dependency between courses
        # scheduling is not possible if there is a cyclic dependency
        return len(sorted_list) == numCourses
