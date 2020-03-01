class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSum,cuSum = -2**31+1, 0
        for i in range(len(nums)):
            cuSum = max(cuSum+nums[i],nums[i])
            maxSum = max(maxSum, cuSum)
        return maxSum