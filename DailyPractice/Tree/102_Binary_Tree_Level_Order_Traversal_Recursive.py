# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        self.traverse(root, res, 0)
        return res

    def traverse(self, curr, res, level):
        if not curr:
            return
        if len(res) <= level:
            res.append([])
        res[level].append(curr.val)
        self.traverse(curr.left, res, level + 1)
        self.traverse(curr.right, res, level + 1)
