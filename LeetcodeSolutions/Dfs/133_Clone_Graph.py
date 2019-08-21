
# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return False
        nodecopy = Node(node.val, [])
        dic = {node: nodecopy}
        self.dfs(node, dic)
        return nodecopy

    def dfs(self, node, dic):
        for neighbor in node.neighbors:
            if neighbor not in dic:

                neighborcopy = Node(neighbor.val, [])
                dic[neighbor] = neighborcopy
                dic[node].neighbors.append(neighborcopy)
                self.dfs(neighbor, dic)
            else:
                dic[node].neighbors.append(dic[neighbor])