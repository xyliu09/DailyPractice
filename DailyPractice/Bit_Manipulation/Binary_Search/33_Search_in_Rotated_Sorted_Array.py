class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if (nums[mid] >= nums[left] and nums[left] <= target < nums[mid]) or target <= nums[mid] < nums[left] or \
                                    nums[mid] < nums[left] <= target:
                right = mid
            else:
                left = mid
        if nums and nums[left] == target:
            return left
        if nums and nums[right] == target:
            return right
        return -1

