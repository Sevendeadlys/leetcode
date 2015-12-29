# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
"""
traverse linklist, judge the l1 or l2.
the carry bit is carried by sum_num
"""
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sum_num = 0
        head = temp = ListNode(0)
        while l1 or l2:
            sum_num /= 10
            if l1 :
                sum_num += l1.val
                l1 = l1.next

            if l2 :
                sum_num += l2.val
                l2 = l2.next
            val = sum_num%10
            temp.next = ListNode(val)
            temp = temp.next
        if sum_num > 9 :  temp.next = ListNode(sum_num/10)
        return head.next
