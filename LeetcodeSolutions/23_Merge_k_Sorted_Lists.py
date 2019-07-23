# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergelist(self, l1, l2):
        cur = dummy = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        cur.next = l1 or l2
        return dummy.next

    def mergeKLists(self, lists):
        lenlists = len(lists)
        if lenlists == 0:
            return lists
        interval = 1
        while interval < lenlists:
            for i in range(0, lenlists - interval, interval * 2):
                lists[i] = self.mergelist(lists[i], lists[i + interval])
            interval = interval * 2
        return lists[0]