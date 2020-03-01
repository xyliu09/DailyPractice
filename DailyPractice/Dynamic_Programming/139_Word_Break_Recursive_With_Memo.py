from functools import lru_cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @lru_cache
        def dfs(s):
            if not s or s in wordDict:
                return True
            for i in range(len(s)):
                if s[:i + 1] in wordDict and dfs(s[i + 1:]):
                    return True
            return False

        return dfs(s)