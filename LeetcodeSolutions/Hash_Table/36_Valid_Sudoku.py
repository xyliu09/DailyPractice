import collections


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for r in board:
            if not self.isUnitValid(r):
                return False

        for c in zip(*board):
            if not self.isUnitValid(c):
                return False

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                square = [board[i + x][j + y] for x in range(0, 3) for y in range(0, 3)]
                if not self.isUnitValid(square):
                    return False
        return True

    def isUnitValid(self, unit):
        res = [x for x in unit if x != "."]
        return len(res) == len(set(res))