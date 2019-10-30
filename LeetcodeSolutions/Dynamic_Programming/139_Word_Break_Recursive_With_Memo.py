class Solution(object):
    def __init__(self):
        self.memo = []

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        return self.helper(s, 0, wordDict)

    def helper(self, s, index, wordDict):
        if index == len(s):
            return True
        if index in self.memo:
            return False

        for i in range(index + 1, len(s) + 1):
            if s[index:i] in wordDict:
                if self.helper(s, i, wordDict):
                    return True
                else:
                    self.memo.append(i)
        self.memo.append(index)
        return False