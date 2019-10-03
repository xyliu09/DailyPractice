class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Recursive Binary Search

        return self.binarySearch(nums, 0, len(nums) - 1)

    def binarySearch(self, nums, l, r):
        if l == r:
            return l
        mid = (l + r) / 2
        if nums[mid] > nums[mid + 1]:
            return self.binarySearch(nums, l, mid)
        else:
            return self.binarySearch(nums, mid + 1, r)

        '''
        Iterative Binary Search:
        while left+1<right:
            mid = (left+right)/2    
            if nums[mid]>nums[mid+1]:
                right = mid
            else:
                left = mid
        if nums[left]>=nums[right]:
            return left
        else:
            return right
        Linear Scan:
        for i in range(len(nums[:-1])):
            if nums[i] >nums[i+1]:
                return i
        return len(nums)-1
        '''