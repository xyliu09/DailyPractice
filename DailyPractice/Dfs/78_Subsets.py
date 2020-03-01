class Solution(object):
    def __init__(self):
        self.res = []

    def subsets(self, nums, path=[]):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res.append(path)
        for i in range(len(nums)):
            self.subsets(nums[i + 1:], path + [nums[i]])
        return self.res

'''
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for n in nums:
            res+=[item +[n] for item in res]
        return res
'''