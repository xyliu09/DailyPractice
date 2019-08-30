class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        tri = []
        for r in range(numRows):
            row = [None for _ in range(r+1)]
            row[0], row[-1] = 1, 1
            for j in range(1, len(row)-1):
                row[j] = tri[r-1][j-1]+tri[r-1][j]
            tri.append(row)
        return tri