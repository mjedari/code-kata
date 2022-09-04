"""
https://wiki.python.org/moin/TimeComplexity
"""

"""
HEAP
    https://docs.python.org/3/library/heapq.html

    - Heap, also known as the priority queue algorithm.
        Heaps are binary trees for which every parent node has a value less than or equal to any of its children. 
        This implementation uses arrays for which heap[k] <= heap[2*k+1] and heap[k] <= heap[2*k+2] for all k, counting elements from zero. 
        For the sake of comparison, non-existing elements are considered to be infinite.
        
    - The interesting property of a heap is that its smallest element is always the root, heap[0].

    - Printing a heap gives you a List view of the a tree (shouldn't be ordered) but if you pop form it it will be increasing order
"""


# l = [3, 2, 6, 5]
# heapq.heapify(l)
# print(l)  # [2, 3, 6, 5]
# l = []
# heapq.heappush(l, 3)
# heapq.heappush(l, 2)
# heapq.heappush(l, 6)
# heapq.heappush(l, 5)
# print(l)  # [2, 3, 6, 5]
# print(heapq.heappop(l))  # 2
# print(heapq.heappop(l))  # 3
# print(heapq.heappop(l))  # 5
# print(heapq.heappop(l))  # 6
# print(heapq.heappop(l))  # IndexError: index out of range

"""
Map, Filter and Reduce
"""

# map(function_to_apply, list_of_inputs)
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))


# filter(function_to_apply, list_of_inputs)
number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))


# reduce(function_to_apply, list_of_inputs)
from functools import reduce
product = reduce((lambda x, y: x * y), [1, 2, 3, 4])  # 24

reduce(lambda output, current: output +
       [(current, ord(current))], 'abc', [])  # [('a', 97), ('b', 98), ('c', 99)]
