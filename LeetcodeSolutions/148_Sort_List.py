# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    @staticmethod
    def getsize(self, head):
        counter = 0
        while head:
            counter += 1
            head = head.next
        return counter

    @staticmethod
    def split(self, head, step):
        i = 1
        while i < step and head:
            head = head.next
            i += 1
        if not head:
            return None
        temp, head.next = head.next, None
        return temp

    @staticmethod
    def merge(self, l, r, head):
        cur = head
        while l and r:
            if l.val < r.val:
                cur.next, l = l, l.next
            else:
                cur.next, r = r, r.next
            cur = cur.next
        cur.next = l or r
        while cur.next:
            cur = cur.next
        return cur

    @staticmethod
    def sortlist(self, head):
        if not head:
            return None
        size = self.getsize(head)
        bs = 1
        dummy = ListNode(None)
        dummy.next = head
        left, right, tail = None, None, None
        while bs < size:
            cur = dummy.next
            tail = dummy
            while cur:
                left = cur
                right = self.split(left, bs)
                cur = self.split(right, bs)
                tail = self.merge(left, right, tail)
            bs <<= 1
        return dummy.next
