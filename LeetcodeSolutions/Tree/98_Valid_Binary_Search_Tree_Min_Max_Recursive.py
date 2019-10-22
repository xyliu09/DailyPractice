import sys


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isValid(root, -sys.maxsize + 1, sys.maxsize)

    def isValid(self, root, minValue, maxValue):
        if not root:
            return True
        if root and root.val <= minValue:
            return False
        if root and root.val >= maxValue:
            return False

        return self.isValid(root.left, minValue, root.val) & self.isValid(root.right, root.val, maxValue)
