"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        curr = head
        while curr:
            node = Node(curr.val, curr.next)
            curr.next = node
            curr = curr.next.next

        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        dummy = Node(0, None, None)
        p1, p2 = dummy, head
        while p2:
            p1.next = p2.next
            p1 = p1.next
            p2.next = p2.next.next
            p2 = p2.next
        return dummy.next

