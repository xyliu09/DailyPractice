import bisect
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [None for _ in nums]
        pos = 0
        for n in nums:
            i = bisect.bisect_left(dp, n, 0, pos)
            dp[i] = n
            if i == pos:
                pos+=1
        return pos