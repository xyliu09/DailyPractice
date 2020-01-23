class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def partition(nums, left, right):
            pivot = nums[right]
            i = left - 1
            for j in range(left, right):
                if nums[j] < pivot:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
            nums[i + 1], nums[right] = nums[right], nums[i + 1]
            return i + 1

        def quickSort(low, high):
            if low < high:
                pi = partition(nums, low, high)
                quickSort(low, pi - 1)
                quickSort(pi + 1, high)

        quickSort(0, len(nums) - 1)

        return nums

