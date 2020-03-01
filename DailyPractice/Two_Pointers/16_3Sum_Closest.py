class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        nums.sort()
        dis = nums[0] + nums[1] + nums[-1] - target
        for i in range(0, len(nums) - 2):
            j, k = i + 1, len(nums) - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s == target:
                    return s
                if abs(s - target) < abs(dis):
                    dis = s - target
                k, j = k - (s - target > 0), j + (s - target <= 0)

        return dis + target