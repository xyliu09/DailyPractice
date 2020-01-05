import functools
class Solution:
    def minInsertions(self, s: str) -> int:
        @functools.lru_cache(None)
        def dfs(h, t, outnum):
            if h > t:
                return outnum
            if h == t:
                return 0
            if h == t-1:
                return 0 if s[h] == s[t] else 1
            if s[h] == s[t]:
                return dfs(h + 1, t - 1, outnum)
            return min(dfs(h + 1, t, outnum ), dfs(h, t - 1, outnum )) + 1
        return dfs(0, len(s) - 1, 0)
