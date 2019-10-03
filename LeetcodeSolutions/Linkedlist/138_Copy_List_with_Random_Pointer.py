"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return None
        p = head
        while p:
            nxt = p.next
            copy = Node(p.val, nxt, None)
            p.next = copy
            p = nxt

        p = head
        while p:
            if p.random:
                p.next.random = p.random.next
            p = p.next.next
        dum = Node(0, None, None)
        p1, p2 = dum, head
        while p2:
            p1.next = p2.next
            p1 = p1.next
            p2.next = p2.next.next
            p2 = p2.next

        return dum.next