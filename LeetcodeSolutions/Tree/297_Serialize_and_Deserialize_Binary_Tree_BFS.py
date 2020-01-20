# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return None
        queue = deque([root])
        ans = []
        while queue:
            node = queue.popleft()
            if node:
                queue.append(node.left)
                queue.append(node.right)
            ans.append(str(node.val) if node else 'None')
        return ','.join(ans)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        data = data.split(',')
        root = TreeNode(data[0])
        queue = deque([root])
        index = 1
        print(data)
        while queue:
            node = queue.popleft()
            if data[index] != 'None':
                node.left = TreeNode(data[index])
                queue.append(node.left)
            index += 1
            if data[index] != 'None':
                node.right = TreeNode(data[index])
                queue.append(node.right)
            index += 1

        return root
