class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.res = 0
        self.dfs([-1 for i in range(n)], 0)
        return self.res

    def dfs(self, nums, index):
        if index == len(nums):
            self.res += 1
            return
        for i in range(len(nums)):
            nums[index] = i
            if self.isValid(nums, index):
                self.dfs(nums, index + 1)

    def isValid(self, nums, n):
        for i in xrange(n):
            if nums[i] == nums[n] or abs(nums[n] - nums[i]) == n - i:
                return False
        return True