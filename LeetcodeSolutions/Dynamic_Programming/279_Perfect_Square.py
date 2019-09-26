import math
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [i for i in range(n+1)]
        for i in range(4, n+1):
            for x in range(1, int(math.sqrt(i))+1):
                temp = x*x
                if i- temp >=0:
                    dp[i] = min(dp[i], dp[i -temp]+1)
        return dp[n]