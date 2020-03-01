class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a= nums[0]
        for n in nums[1:]:
            a ^=n
        return a