class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visited = []

        def backtrack(i, j, start, word):
            if start == len(word):
                return True
            if i < 0 or j < 0 or i > len(board) - 1 or j > len(board[0]) - 1 or (i, j) in visited:
                return False

            for x, y in direction:
                visited.append((i, j))
                if board[i][j] == word[start] and backtrack(i + x, j + y, start + 1, word):
                    return True
                visited.pop()
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i, j, 0, word):
                    return True
        return False
