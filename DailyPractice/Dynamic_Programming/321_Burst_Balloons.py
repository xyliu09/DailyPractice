import functools


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]

        @functools.lru_cache(None)
        def dfs(left, right):
            # max coins you can get to burst all the balloon between left and right
            if left + 1 == right:
                #There is no extra baloon between left and right
                return 0
            # loop through all the possible last ballons
            return max(
                nums[left] * nums[i] * nums[right] + dfs(left, i) + dfs(i, right) for i in range(left + 1, right))

        return dfs(0, len(nums) - 1)
