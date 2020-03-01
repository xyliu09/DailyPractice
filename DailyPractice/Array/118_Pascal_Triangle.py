class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        for i in range(numRows):
            curr = [None for _ in range(i+1)]
            curr[0], curr[-1] = 1,1
            for j in range(1, i):
                curr[j] = res[-1][j-1] + res[-1][j]
            res.append(curr)
        return res