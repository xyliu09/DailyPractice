# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        self.node = []
        for l in lists:
            while l:
                self.node.append(l.val)
                l = l.next
        self.node.sort()
        head = curr = ListNode(0)
        for n in self.node:
            curr.next = ListNode(n)
            curr = curr.next
        return head.next