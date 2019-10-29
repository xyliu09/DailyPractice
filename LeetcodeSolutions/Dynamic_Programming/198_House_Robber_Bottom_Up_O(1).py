class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev, curr = 0, 0
        for n in nums:
            temp = prev
            prev = curr
            curr = max(temp+n, prev)
        return curr