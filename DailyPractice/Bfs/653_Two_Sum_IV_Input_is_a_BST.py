# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def __init__(self):
        self.table = set()
        
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        q = []
        if root:
            q.append(root)
        while q:
            node = q.pop(0)
            if k - node.val in self.table:
                return True
            else:
                self.table.add(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right) 
        return False
