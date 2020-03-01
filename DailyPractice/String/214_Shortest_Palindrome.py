class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        rev = s[::-1]
        for i in range(len(s)):
            if s[:n-i] == rev[i:]:
                return rev[:i] + s
        return ""