class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        def searchLeft(nums, target):
            start, end = 0, len(nums) - 1
            while start + 1 < end:
                mid = (start + end) // 2
                if nums[mid] < target:
                    start = mid
                else:
                    end = mid
            if nums[start] == target:
                return start
            elif nums[end] == target:
                return end
            else:
                return -1

        def searchRight(nums, target):
            start, end = 0, len(nums) - 1
            while start + 1 < end:
                mid = (start + end) // 2
                if nums[mid] > target:
                    end = mid
                else:
                    start = mid
            if nums[end] == target:
                return end
            elif nums[start] == target:
                return start
            else:
                return -1

        if not nums: return [-1, -1]
        left, right = searchLeft(nums, target), searchRight(nums, target)
        return [left, right] if left <= right else [-1, -1]