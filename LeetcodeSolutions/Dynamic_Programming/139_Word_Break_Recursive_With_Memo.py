class Solution(object):
    def __init__(self):
        self.memo = {}

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if s in self.memo:
            return self.memo[s]
        if not s or s in wordDict:
            self.memo[s] = True
            return True

        for i in range(len(s)):
            if s[:i + 1] in wordDict and self.wordBreak(s[i + 1:], wordDict):
                self.memo[s] = True
                return True
        self.memo[s] = False
        return False


