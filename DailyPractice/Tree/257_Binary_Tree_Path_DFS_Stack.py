# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res = []
        stack = [(root, "")]
        if root:
            while stack:
                node, ls = stack.pop()
                if not node.right and not node.left:
                    res.append(ls + str(node.val))
                if node.right:
                    stack.append((node.right, ls + str(node.val) + "->"))
                if node.left:
                    stack.append((node.left, ls + str(node.val) + "->"))

        return res


