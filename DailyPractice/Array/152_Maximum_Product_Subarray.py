class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res, imin, imax = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            candidate = (nums[i], nums[i]*imin, nums[i]*imax)
            imin = min(candidate)
            imax = max(candidate)
            res = max(res, imax)
        return res

a= Solution()
a.maxProduct([1,2,3,4,5])