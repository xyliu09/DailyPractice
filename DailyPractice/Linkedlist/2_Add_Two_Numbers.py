# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = curr = ListNode(0)
        carry = 0
        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            sum = v1 + v2 + carry
            carry = sum / 10
            curr.next = ListNode(sum % 10)
            curr = curr.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        if carry > 0:
            curr.next = ListNode(carry)
        return dummy.next
