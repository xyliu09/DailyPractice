class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        """
            nums.sort()
            res = []
            self.dfs(nums, 0, [], res)
            return res

        def dfs(self,nums, index, path, res):
            if path not in res:
                res.append(path)
            for i in range(index, len(nums)):
                self.dfs(nums, i+1, path+[nums[i]], res)
        """
        res, curr = [[]], []
        if not nums:
            return res
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                curr = [item + [nums[i]] for item in curr]
            else:
                curr = [item + [nums[i]] for item in res]
            res += curr

        return res