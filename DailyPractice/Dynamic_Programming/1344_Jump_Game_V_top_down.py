class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dfs(i):
            res = 1
            for j in range(i + 1, min(i + d + 1, len(arr))):
                if arr[j] >= arr[i]: break
                res = max(res, 1 + dfs(j))

            for j in range(i - 1, max(i - 1 - d, -1), -1):
                if arr[j] >= arr[i]: break
                res = max(res, 1 + dfs(j))

            return res

        res = 1
        for i in range(len(arr)):
            res = max(res, dfs(i))
        return res
