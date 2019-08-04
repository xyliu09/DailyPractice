class Solution(object):
    def __init__(self):
        self.path = []
        self.res = []

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        self.dfs(nums)
        return self.res

    def dfs(self, nums):
        if not nums:
            self.res.append(self.path[:])

        for i, n in enumerate(nums):
            if i == 0 or nums[i] != nums[i - 1]:
                self.path.append(n)
                self.dfs(nums[:i] + nums[i + 1:])
                self.path.pop()