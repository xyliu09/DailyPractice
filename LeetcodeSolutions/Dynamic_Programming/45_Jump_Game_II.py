class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1: return 0
        l, r = 0, nums[0]
        time = 1
        while r < len(nums) - 1:
            time += 1
            nxt = max(i + nums[i] for i in range(l, r + 1))
            l, r = r, nxt
        return time
