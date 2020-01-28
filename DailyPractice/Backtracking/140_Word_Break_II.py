class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        memo = {}
        res = []

        def dfs(s):
            if s in memo:
                return memo[s]
            ans = []
            if s in wordDict:
                ans.append(s)
            for i in range(1, len(s)):
                if s[i:] not in wordDict:
                    continue
                ans += [w + ' ' + s[i:] for w in dfs(s[:i])]
            memo[s] = ans
            return memo[s]

        return dfs(s)




