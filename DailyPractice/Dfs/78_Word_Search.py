#dfs+backtracking, use list as the stack so it doesn't need to modify the matrix

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word, []):
                    return True
        return False

    def dfs(self, board, i, j, word, visited):
        if len(word) == 0:
            return True

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[0] != board[i][j] or (i, j) in visited:
            return False
        visited.append((i, j))
        res = self.dfs(board, i - 1, j, word[1:], visited) or self.dfs(board, i, j - 1, word[1:], visited) \
              or self.dfs(board, i + 1, j, word[1:], visited) or self.dfs(board, i, j + 1, word[1:], visited)
        if not res:
            a = visited.pop()
        return res



