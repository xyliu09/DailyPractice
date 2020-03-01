# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        odd, even = head, head.next
        oddHead, evenHead = odd, even
        while odd.next.next:
            odd.next = odd.next.next
            odd = odd.next
        while even and even.next.next:
            even.next = even.next.next
            even = even.next
        odd.next = evenHead
        return oddHead
