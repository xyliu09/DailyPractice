# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        self.traverse(root, res, 0)
        return res

    def traverse(self, curr, res, level):
        if not curr:
            return res
        if len(res) <= level:
            res.append([])
        if level % 2 == 0:
            res[level].append(curr.val)
        else:
            res[level].insert(0, curr.val)
        self.traverse(curr.left, res, level + 1)
        self.traverse(curr.right, res, level + 1)