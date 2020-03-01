# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left, right = 1, 1
        if root.left:
            left = self.minDepth(root.left) + 1
        if root.right:
            right = self.minDepth(root.right) + 1
        return min(left, right) if root.left and root.right else max(left, right)