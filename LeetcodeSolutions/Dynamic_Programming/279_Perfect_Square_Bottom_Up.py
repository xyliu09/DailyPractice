class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [ i for i in range(n + 1) ]
        for i in range(4, n + 1):
            for j in range(1, int(i**0.5) + 1):
                if i - j*j >= 0:
                    dp[i] = min(dp[i], dp[i-j*j] + 1)
        return dp[n]