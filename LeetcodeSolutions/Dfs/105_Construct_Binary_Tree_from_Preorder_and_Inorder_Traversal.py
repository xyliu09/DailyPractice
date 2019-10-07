class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            inroot = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[inroot])
            root.left = self.buildTree(preorder, inorder[:inroot])
            root.right = self.buildTree(preorder, inorder[inroot + 1:])
            return root