class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        self.dfs(nums, 0, [], res)
        return res

    def dfs(self, nums, start, path, res):
        if path not in res:
            res.append(path)
        for i in range(start, len(nums)):
            self.dfs(nums, i + 1, path + [nums[i]], res)