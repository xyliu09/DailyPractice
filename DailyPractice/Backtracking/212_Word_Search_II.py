class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = ""


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        root = TrieNode()
        for word in words:
            self.buildTrie(word, root)

        self.ans = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in root.children:
                    self.backtrack(board, i, j, root.children[board[i][j]])
        return self.ans

    def backtrack(self, board, i, j, node):
        if not node:
            return False
        if node.word and node.word not in self.ans:
            self.ans.add(node.word)
        c, board[i][j] = board[i][j], '#'

        for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if i + x < 0 or j + y < 0 or i + x > len(board) - 1 or j + y > len(board[0]) - 1 or board[i + x][
                        j + y] not in node.children:
                continue
            self.backtrack(board, i + x, j + y, node.children[board[i + x][j + y]])
        board[i][j] = c

    def buildTrie(self, word, node):
        for c in word:
            if not c in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.word = word



