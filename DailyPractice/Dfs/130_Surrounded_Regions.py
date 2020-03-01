class Solution(object):
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        for i in range(len(board)):
            if board[i][0] == "O":
                self.dfs(board, i, 0)
            if board[i][-1] == "O":
                self.dfs(board, i, len(board[0]) - 1)
        for j in range(len(board[0])):
            if board[0][j] == "O":
                self.dfs(board, 0, j)
            if board[-1][j] == "O":
                self.dfs(board, len(board) - 1, j)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "*":
                    board[i][j] = "O"

    def dfs(self, board, i, j):
        if i < 0 or i > len(board) - 1 or j < 0 or j > len(board[0]) - 1 or board[i][j] != "O":
            return
        board[i][j] = "*"
        for x, y in Solution.directions:
            self.dfs(board, i + x, j + y)