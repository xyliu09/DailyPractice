class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(0, len(matrix)):
            for j in range(0,len(matrix[0])//2):
                matrix[i][j], matrix[i][len(matrix[0])-1-j] = matrix[i][len(matrix[0])-1-j], matrix[i][j]