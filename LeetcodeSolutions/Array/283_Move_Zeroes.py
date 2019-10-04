class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.

        Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

        """
        nz = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[nz] = nums[nz], nums[i]
                nz += 1