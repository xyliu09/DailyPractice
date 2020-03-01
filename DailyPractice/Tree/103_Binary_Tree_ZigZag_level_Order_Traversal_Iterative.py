import collections
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
        if not root:
            return
        q = collections.deque([root])
        res = []
        zigZag = False
        while q:
            currlevel, size = [], len(q)
            for i in range(size):
                node = q.popleft()
                currlevel.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if zigZag:
                currlevel.reverse()
            zigZag = not zigZag
            res.append(currlevel)
        return res