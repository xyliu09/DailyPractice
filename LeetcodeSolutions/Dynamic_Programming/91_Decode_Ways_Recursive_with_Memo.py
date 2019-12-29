class Solution(object):
    def __init__(self):
        self.memo = {}

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        return self.dfs(s, 0, len(s) - 1)

    def dfs(self, s, l, r):
        if l in self.memo: return self.memo[l]
        if l <= r and s[l] == '0': return 0
        if l >= r: return 1
        w = self.dfs(s, l + 1, r)
        prefix = int(s[l]) * 10 + int(s[l + 1])
        if prefix <= 26:
            w += self.dfs(s, l + 2, r)
        self.memo[l] = w
        return w
