class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        fast, slow = ListNode(0), ListNode(0)
        fast.next, slow.next = head, head
        for i in range(n):
            fast = fast.next
        dummy = slow
        while fast.next:
            slow = slow.next
            fast = fast.next
        prev = slow
        slow = slow.next.next
        prev.next = slow
        return dummy.next