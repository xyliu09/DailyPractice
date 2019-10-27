class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        memo = [-1 for i in range(len(nums) + 1)]
        return self.helper(nums, len(nums) - 1, memo)

    def helper(self, nums, i, memo):
        if i < 0:
            return 0
        if memo[i] >= 0:
            return memo[i]
        memo[i] = max(self.helper(nums, i - 1, memo), self.helper(nums, i - 2, memo) + nums[i])
        return memo[i]