class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1: return nums
        for i in range(len(nums) - 2, -1, -1):
            j = i
            if nums[i] < nums[i + 1]:
                j = self.findpivot(nums, i + 1)
                nums[i], nums[j] = nums[j], nums[i]
                break
        if i != j:
            nums[i + 1:] = nums[i + 1:][::-1]
        else:
            nums = nums.reverse()
        return nums

    def findpivot(self, nums, i):
        l = i
        r = len(nums) - 1
        while l + 1 < r:
            m = (l + r) // 2
            if nums[m] > nums[i - 1]:
                l = m
            else:
                r = m
        if nums[r] > nums[i - 1]:
            return r
        return l


