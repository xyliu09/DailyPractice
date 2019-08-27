"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
from collections import deque
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node: return False
        nodecopy = Node(node.val, [])
        dic={node:nodecopy}
        queue = deque([node])
        while queue:
            node = queue.popleft()
            for neighbor in node.neighbors:
                if neighbor not in dic:
                    dic[neighbor] = Node(neighbor.val, [])
                    dic[node].neighbors.append(dic[neighbor] )
                    queue.append(neighbor)
                else:
                    dic[node].neighbors.append(dic[neighbor])
        return nodecopy
