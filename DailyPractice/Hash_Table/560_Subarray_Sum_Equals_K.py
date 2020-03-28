'''
Share
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2

'''
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