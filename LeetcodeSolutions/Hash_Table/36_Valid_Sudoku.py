class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        def isRowValid(board):
            for row in board:
                if not isUnitValid(row):
                    return False
            return True

        def isColValid(board):
            for col in zip(*board):
                if not isUnitValid(col):
                    return False
            return True

        def isSquareValid(board):
            for i in (0, 3, 6):
                for j in (0, 3, 6):
                    square = [board[i + x][j + y] for x in range(3) for y in range(3)]
                    if not isUnitValid(square):
                        return False
            return True

        def isUnitValid(unit):
            res = [x for x in unit if x != '.']
            return len(res) == len(set(res))

        return isRowValid(board) and isColValid(board) and isSquareValid(board)