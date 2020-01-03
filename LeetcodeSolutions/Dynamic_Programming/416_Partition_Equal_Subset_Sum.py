class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total = 0
        for number in nums:
            total += number
        if total % 2: return False
        total /= 2
        dp = [[False for i in range(total + 1)] for j in range(len(nums) + 1)]

        dp[0][0] = True
        for i in range(1, len(nums) + 1):
            dp[i][0] = True
        for j in range(1, total + 1):
            dp[0][j] = False
        for i in range(1, len(nums) + 1):
            for j in range(1, total + 1):
                if j >= nums[i - 1]:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
        return dp[len(nums)][total]