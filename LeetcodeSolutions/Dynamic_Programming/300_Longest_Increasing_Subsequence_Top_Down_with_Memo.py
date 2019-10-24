class Solution(object):
    # tle n^2
    def __init__(self):
        self.memo = None

    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.memo = [[None for _ in range(len(nums) + 1)] for i in range(len(nums))]
        return self.helper(nums, -1, 0)

    def helper(self, nums, previndex, pos):
        if len(nums) == pos:
            return 0
        if self.memo[previndex + 1][pos] >= 0:
            return self.memo[previndex + 1][pos]
        taken = 0
        if previndex < 0 or nums[pos] > nums[previndex]:
            taken = 1 + self.helper(nums, pos, pos + 1)
        nottaken = self.helper(nums, previndex, pos + 1)
        self.memo[previndex + 1][pos] = max(taken, nottaken)
        return self.memo[previndex + 1][pos]