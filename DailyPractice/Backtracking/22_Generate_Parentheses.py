class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.backtrack(res, "", 0, 0, n)
        return res

    def backtrack(self, res, st, left, right, n):
        if len(st) == 2 * n:
            res.append(st)
            return
        if left < n:
            self.backtrack(res, st + '(', left + 1, right, n)
        if right < left:
            self.backtrack(res, st + ')', left, right + 1, n)