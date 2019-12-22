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
        if not root:
            return True
        stack = [(root, float('inf'), float('-inf'))]
        while stack:
            node, maxvalue, minvalue = stack.pop()
            if node.val >= maxvalue:
                return False
            if node.val <= minvalue:
                return False
            if node.left:
                stack.append((node.left, node.val, minvalue))
            if node.right:
                stack.append((node.right, maxvalue, node.val))
        return True
