class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        maxPosition = 0
        for i, x in enumerate(nums):
            if i > maxPosition:
                return False
            maxPosition = max(maxPosition, i + x)
        return maxPosition >= len(nums)-1