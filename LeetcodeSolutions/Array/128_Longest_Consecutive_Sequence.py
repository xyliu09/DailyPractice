class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest_streak = 0
        nums_set = set(nums)
        for num in nums:
            if num - 1 not in nums_set:
                current_nums = num
                current_streak = 1
                while current_nums+1 in nums_set:
                    current_nums += 1
                    current_streak += 1
                longest_streak = max(longest_streak, current_streak)
        return longest_streak