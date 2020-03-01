class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        if not p:
            return not s
        if not s:
            return self.isMatch(s, p[1:]) if p[0]== "*" else not p
        firstmatch = s and p[0] in {s[0], "?", "*"}
        if p[0] == "*" and s:
            return self.isMatch(s[1:], p) or self.isMatch(s, p[1:])


        if p[0] != "*":
            return firstmatch and self.isMatch(s[1:], p[1:])

a= Solution()
print(a.isMatch("acdcb","a*c?b"))