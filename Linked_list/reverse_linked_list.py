"""
https://leetcode.com/problems/reverse-linked-list/

Given the head of a singly linked list, reverse the list, and return the reversed list.

"""
from typing import Optional

"""
1- iterative approach. 
The idea is to change next with prev, prev with current, and current with next.
"""
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None
        cur = head

        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp

        return prev


"""
2- Recursion
"""


# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         return self._reverse(head)

#     def _reverse(self, node, prev=None):
#         if not node:
#             return prev
#         n = node.next
#         node.next = prev
#         return self._reverse(n, node)
