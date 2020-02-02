import functools


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]

        @functools.lru_cache(None)
        def dfs(left, right):
            if left + 1 == right:
                return 0
            return max(
                nums[left] * nums[i] * nums[right] + dfs(left, i) + dfs(i, right) for i in range(left + 1, right))

        return dfs(0, len(nums) - 1)
