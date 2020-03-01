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
        self.res = []
        if root:
            self.helper(root, [str(root.val)])
        return self.res

    def helper(self, root, path):
        if not root.left and not root.right:
            path_res = '->'.join(path)
            self.res.append(path_res)
        if root.left:
            self.helper(root.left, path + [str(root.left.val)])
        if root.right:
            self.helper(root.right, path + [str(root.right.val)])


