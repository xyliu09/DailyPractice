# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        def dfs(node, treeNode=root):
            if not node:
                return True
            if not treeNode:
                return False
            if node.val != treeNode.val:
                return False
            return dfs(node.next, treeNode.left) or dfs(node.next, treeNode.right)

        if not head:
            return True
        if not root:
            return False
        return dfs(head) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)