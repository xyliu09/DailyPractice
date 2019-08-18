# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        q = []
        q.append(root)
        q.append(root)
        while q:
            n1 = q.pop(0)
            n2 = q.pop(0)
            if not n1 and not n2: continue
            if not n1 or not n2 or n1.val != n2.val: return False
            q.append(n1.left)
            q.append(n2.right)
            q.append(n1.right)
            q.append(n2.left)
        return True

    