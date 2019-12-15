class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dic = {0:1}
        count = 0
        su = 0
        for i in range(len(nums)):
            su += nums[i]
            if su-k in dic:
                count += dic[su- k]
            dic[su] = dic.get(su, 0) + 1
        return count