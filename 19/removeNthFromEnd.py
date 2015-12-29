# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
consider the boundry of linklist
"""
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        pre = head
        p = head
        for i in range(n):
            p = p.next
        if not p:
            return head.next
        while p.next:
            pre = pre.next
            p = p.next
        pre.next = pre.next.next
        return head
