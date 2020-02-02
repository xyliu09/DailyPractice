# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        total = 0
        self.res = 0

        def s(root):
            if not root:
                return 0
            left, right = s(root.left), s(root.right)
            self.res = max(self.res, (total - left) * left, (total - right) * right)
            return left + root.val + right

        total = s(root)
        s(root)
        return self.res % (10 ** 9 + 7)
