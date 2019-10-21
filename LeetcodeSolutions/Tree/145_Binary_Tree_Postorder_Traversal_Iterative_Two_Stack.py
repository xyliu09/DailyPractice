# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []

        stack1, stack2 = [root], []
        while stack1:
            curr = stack1.pop()
            stack2.append(curr.val)
            if curr.left:
                stack1.append(curr.left)
            if curr.right:
                stack1.append(curr.right)
        return stack2[::-1]