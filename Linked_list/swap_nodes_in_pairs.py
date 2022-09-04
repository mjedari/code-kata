"""
https://leetcode.com/problems/swap-nodes-in-pairs/

Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

F   S   T
0   1   2   3   4   !

0 -> 2  [F.next = T]
1 -> 3  [S.next = T.next]
2 -> 1  [T.next = second]

        F   S   T
0   2   1   3   4   !

1 -> 4  [F.next = T]
3 -> !  [S.next = T.next]
4 -> 3  [T.next = second]

                F   S   T
0   2   1   4   3   !

"""

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        current = ListNode()
        current.next = head
        node = current

        while node != None and node.next != None and node.next.next != None:
            first = node
            second = node.next
            third = node.next.next

            first.next = third
            second.next = third.next
            third.next = second
            node = second
        return current.next
