# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):

        if not lists: return None

        def merge2(l1,l2):
            if not l1: return l2
            if not l2: return l1
            head = ListNode(0)
            tail = head
            while l1 and l2:
                if l1.val <= l2.val:
                    tail.next = l1
                    l1 = l1.next
                else:
                    tail.next = l2
                    l2 = l2.next
                tail = tail.next

            if l1:
                tail.next = l1
            else:
                tail.next = l2
            return head.next

        while len(lists) > 1:
            n = len(lists)
            for i in range(n//2):
                l1 = lists.pop()
                l2 = lists.pop()
                lists.insert(0,merge2(l1,l2))
        return lists[0]
