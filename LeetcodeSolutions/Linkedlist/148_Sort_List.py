# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return None

        def getSize(head):
            counter = 0
            while head:
                counter += 1
                head = head.next
            return counter

        def split(head, step):
            i = 1
            while i < step and head:
                head = head.next
                i += 1
            if not head:
                return None
            temp, head.next = head.next, None
            return temp

        def merge(l, r, head):
            cur = head
            while l and r:
                if l.val < r.val:
                    cur.next, l = l, l.next
                else:
                    cur.next, r = r, r.next
                cur = cur.next
            cur.next = l or r
            while cur.next: cur = cur.next
            return cur

        size = getSize(head)
        bs = 1
        dummy = ListNode(None)
        dummy.next = head
        l, r, tail = None, None, None
        while bs < size:
            cur = dummy.next
            tail = dummy
            while cur:
                l = cur
                r = split(l, bs)
                cur = split(r, bs)
                tail = merge(l, r, tail)
            bs <<= 1
        return dummy.next