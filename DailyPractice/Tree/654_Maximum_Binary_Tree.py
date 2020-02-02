# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import heapq
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return
        el = heapq.nlargest(1, nums)[0]
        index = nums.index(el)
        t = TreeNode(el)
        t.left = self.constructMaximumBinaryTree(nums[:index])
        t.right =self.constructMaximumBinaryTree(nums[index+1:])
        return t