class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        for i in range(0, len(nums)):
            for j in range(max(0, i - k), i):
                if nums[i] == nums[j]:
                    return True
        return False

