class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        l, r = 0, 0
        ans = []
        for ch in s:
            l += (ch == '(')
            if l == 0:
                r += (ch == ')')
            else:
                l -= (ch == ')')
        self.dfs(s, 0, l, r, ans)
        return ans

    def isValid(self, s):
        count = 0
        for ch in s:
            if ch == '(':
                count += 1
            if ch == ')':
                count -= 1
            if count < 0:
                return False
        return count == 0

    def dfs(self, s, index, l, r, ans):
        if (l == 0 and r == 0):
            if self.isValid(s):
                ans.append(s)
                return
        for i in range(index, len(s)):
            if i != index and s[i] == s[i - 1]:
                continue
            if s[i] == '(' or s[i] == ')':
                curr = copy.deepcopy(s)
                curr = curr[:i] + curr[i + 1:]
                if r > 0:
                    # First need to remove all r ‘）’， then can start removing l '('
                    self.dfs(curr, i, l, r - 1, ans)
                elif l > 0:
                    self.dfs(curr, i, l - 1, r, ans)


