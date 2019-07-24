class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        result = [ [ 1 for _ in range(n)] for _ in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                result[i][j]= result[i-1][j]+result[i][j-1]
        return result[-1][-1]