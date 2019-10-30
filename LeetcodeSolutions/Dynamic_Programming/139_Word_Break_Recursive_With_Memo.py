import collections


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
        if s in wordDict:
            self.memo[s] = True
            return True
        for i in range(0, len(s)):
            left, right = s[:i], s[i:]
            if self.wordBreak(left, wordDict) and right in wordDict:
                self.memo[s] = True
                return True
        self.memo[s] = False
        return False