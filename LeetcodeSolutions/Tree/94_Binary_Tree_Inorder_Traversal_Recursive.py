# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return
        res = []
        if root.left:
            left = self.inorderTraversal(root.left)
            res += left
        res.append(root.val)
        if root.right:
            right = self.inorderTraversal(root.right)
            res += right
        return res