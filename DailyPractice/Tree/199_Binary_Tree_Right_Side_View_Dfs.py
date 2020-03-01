# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.rightViewUtil(root, res, 1)
        return res

    def rightViewUtil(self, node, res, depth):
        if not node:
            return
        if len(res) < depth:
            res.append(node.val)
        self.rightViewUtil(node.right, res, depth + 1)
        self.rightViewUtil(node.left, res, depth + 1)