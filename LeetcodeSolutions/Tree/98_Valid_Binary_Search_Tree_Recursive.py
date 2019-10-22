# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        arr = self.inOrder(root, [])
        for i in range(len(arr) - 1):
            if arr[i] >= arr[i + 1]:
                return False
        return True

    def inOrder(self, root, arr):
        if not root:
            return arr

        self.inOrder(root.left, arr)
        arr.append(root.val)
        self.inOrder(root.right, arr)
        return arr
