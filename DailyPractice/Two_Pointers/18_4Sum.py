def findNSum(self, nums, target, N, result, results):
    if len(nums) < N or N < 2 or target < nums[0] * N or target > nums[-1] * N:
        return
    if N == 2:
        l, r = 0, len(nums) - 1
        while l < r:
            s = nums[r] + nums[l]
            if s == target:
                results.append(result + [nums[l], nums[r]])
                while l < r and nums[l] == nums[l + 1]: l += 1
                while l > r and nums[r] == nums[r - 1]: r -= 1
                l += 1
                r -= 1
            elif s < target:
                l += 1
            else:
                r -= 1
    else:
        for i in range(len(nums) - N + 1):
            if i == 0 or nums[i] != nums[i - 1]:
                self.findNSum(nums[i + 1:], target - nums[i], N - 1, result + [nums[i]], results)


def fourSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    res = []
    self.findNSum(sorted(nums), target, 4, [], res)
    return res