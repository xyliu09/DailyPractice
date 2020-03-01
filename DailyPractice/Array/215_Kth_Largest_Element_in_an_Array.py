class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        self.quickSelect(nums, 0, len(nums) - 1, k)
        return nums[k - 1]

    def quickSelect(self, nums, left, right, k):
        if left >= right:
            return
        pivot = self.partition(nums, left, right)
        if pivot > k - 1:
            self.quickSelect(nums, left, pivot - 1, k)
        elif pivot < k + 1:
            self.quickSelect(nums, pivot + 1, right, k)

    def partition(self, nums, left, right):
        i, j = left, left
        while j < right:
            if nums[j] > nums[right]:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1
        nums[right], nums[i] = nums[i], nums[right]
        return i 