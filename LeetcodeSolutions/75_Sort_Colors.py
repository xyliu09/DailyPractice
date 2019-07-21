class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        red, white, blue = 0, 0, len(nums)-1
        while white<= blue:
            if nums[white] == 0:
                nums[red],nums[white] = nums[white],nums[red]
                red += 1
                white += 1
            elif nums[white] == 1:
                white += 1
            else:
                nums[blue],nums[white] = nums[white],nums[blue]
                blue -= 1
        return nums