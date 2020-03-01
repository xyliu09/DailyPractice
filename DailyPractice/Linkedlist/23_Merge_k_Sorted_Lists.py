# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from Queue import PriorityQueue


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        '''
        dummy = curr = ListNode(0)
        for i in range(len(lists)):
            minNodeValue = float('-inf')
            for lists[i].val
                minNodeValue = min(minNodeValue, minValue)
            curr.next = ListNode(minNodeValue)
            curr = curr.next
        return dummy.next
        '''
        head = point = ListNode(0)
        q = PriorityQueue()
        for l in lists:
            if l:
                q.put((l.val, l))
        while not q.empty():
            val, node = q.get()
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                q.put((node.val, node))
        return head.next
    '''
    # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        interval = 1
        while interval <= len(lists):
            for i in range(0, len(lists)-interval, interval*2):
                lists[i] = self.mergeTwoLists(lists[i], lists[i+interval])
            interval *= 2
        return lists[0] if len(lists) > 0 else None
        
    def mergeTwoLists(self, l1, l2):
        dummy = curr = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                curr.next= l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 or l2  
        return dummy.next
        s
    
    '''
