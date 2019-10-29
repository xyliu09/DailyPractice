class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        if len(nums) <= 2: return max(nums)
        return max(self.houseRobber(nums[1:]), self.houseRobber(nums[:-1]))

    def houseRobber(self, nums):
        prev, curr = 0, 0
        for n in nums:
            temp = prev
            prev = curr
            curr = max(temp + n, prev)
        return curr
