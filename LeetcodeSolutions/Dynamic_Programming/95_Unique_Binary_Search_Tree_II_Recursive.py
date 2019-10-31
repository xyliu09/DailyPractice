class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        return self.genTreeList(1, n)

    def genTreeList(self, start, end):
        res = []
        if start > end:
            res.append(None)
        for i in range(start, end + 1):
            leftList = self.genTreeList(start, i - 1)
            rightList = self.genTreeList(i + 1, end)
            for leftNode in leftList:
                for rightNode in rightList:
                    root = TreeNode(i)
                    root.left = leftNode
                    root.right = rightNode
                    res.append(root)
        return res
