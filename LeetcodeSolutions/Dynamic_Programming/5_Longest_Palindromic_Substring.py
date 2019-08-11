class Solution(object):
    def __init__(self):
        self.maxlen = 0
        self.lo = 0

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        for i in range(len(s)):
            self.helper(s, i, i)
            self.helper(s, i, i + 1)
        return s[self.lo:self.lo + self.maxlen]

    def helper(self, s, j, k):
        while j >= 0 and k <= len(s) - 1 and s[j] == s[k]:
            j -= 1
            k += 1
        if self.maxlen < k - j - 1:
            self.lo = j + 1
            self.maxlen = k - j - 1