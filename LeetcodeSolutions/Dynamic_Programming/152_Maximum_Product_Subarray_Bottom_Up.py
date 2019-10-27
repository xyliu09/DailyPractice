class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res, imin, imax = -2 ** 31 + 1, 1, 1
        for candidate in nums[:]:
            res = max(imin * candidate, imax * candidate, candidate, res)
            imin, imax = min(imax * candidate, imin * candidate, candidate), max(imax * candidate, imin * candidate,
                                                                                 candidate)
        return res