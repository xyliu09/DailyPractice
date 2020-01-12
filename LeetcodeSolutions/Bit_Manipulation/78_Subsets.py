class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        for s in range(1 << len(nums)):
            curr = []
            for i in range(len(nums)):
                if s & (1 << i): curr.append(nums[i])
            res.append(curr)
        return res
