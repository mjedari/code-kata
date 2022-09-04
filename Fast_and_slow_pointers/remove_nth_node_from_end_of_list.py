"""
https://leetcode.com/problems/remove-nth-node-from-end-of-list/


Given the head of a linked list, remove the nth node from the end of the list and return its head.


"""
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head.next == None:
            return

        result = first = head
        second = head
        for _ in range(n):
            second = second.next

        if second == None:
            return head.next

        while second.next:
            first = first.next
            second = second.next

        first.next = first.next.next

        return result
