class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for i in range(len(nums)):
            if count == 0:
                candidate = nums[i]
            count += 1 if nums[i] == candidate else -1
        return candidate