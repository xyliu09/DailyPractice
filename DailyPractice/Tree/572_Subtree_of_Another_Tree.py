# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        return s and (self.isIdentical(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t))

    def isIdentical(self, s, t):
        if not s and not t:
            return True
        if not s or not t:
            return False
        return s.val == t.val and self.isIdentical(s.left, t.left) and self.isIdentical(s.right, t.right)
