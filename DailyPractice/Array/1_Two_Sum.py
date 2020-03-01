class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) <= 1: return []
        table = {}
        for index, item in enumerate(nums):
            if target - item in table:
                return [table[target-item],index]
            else:
                table[item] = index
        return []