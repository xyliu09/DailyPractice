class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        L = [0 for _ in range(n)]
        R = [0 for _ in range(n)]
        res = [0 for _ in range(n)]
        L[0], R[len(nums) - 1] = 1, 1
        for i in range(1, n):
            L[i] = nums[i - 1] * L[i - 1]
        for i in reversed(range(n - 1)):
            R[i] = nums[i + 1] * R[i + 1]
        for i in range(n):
            res[i] = R[i] * L[i]

        return res