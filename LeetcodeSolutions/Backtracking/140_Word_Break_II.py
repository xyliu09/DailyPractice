class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        res = []
        self.dfs(s, wordDict, "", res)
        return res

    def dfs(self, s, dic, path, res):
        if not s:
            res.append(path[:-1])
            return
        if self.check(s, dic):
            for i in range(1, len(s) + 1):
                if s[:i] in dic:
                    self.dfs(s[i:], dic, path + s[:i] + " ", res)

    def check(self, s, dic):
        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True
        for i in range(1, len(s) + 1):
            for j in xrange(i):
                if dp[j] and s[j:i] in dic:
                    dp[i] = True
        return dp[-1]
