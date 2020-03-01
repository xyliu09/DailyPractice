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
                self.bfs(board, i, 0)
            if board[i][-1] == "O":
                self.bfs(board, i, len(board[0]) - 1)
        for j in range(len(board[0])):
            if board[0][j] == "O":
                self.bfs(board, 0, j)
            if board[-1][j] == "O":
                self.bfs(board, len(board) - 1, j)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "*":
                    board[i][j] = "O"

    def bfs(self, board, i, j):
        stack = [(i, j)]
        while stack:
            p, q = stack.pop()
            board[p][q] = "*"
            for x, y in Solution.directions:
                if p + x < 0 or q + y < 0 or p + x > len(board) - 1 or q + y > len(board[0]) - 1 or board[p + x][
                            q + y] != "O":
                    continue
                stack.append((p + x, q + y))

