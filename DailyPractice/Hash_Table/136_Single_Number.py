class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hastable ={}
        for n in nums:
            try:
                hastable.pop(n)
            except:
                hastable[n] = 1
        return hastable.popitem()[0]