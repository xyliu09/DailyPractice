'''
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

Example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true

'''
class TrieNode():
    def __init__(self):
        self.children = {}
        self.isWord = False


class WordDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.isWord = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        node = self.root
        return self.dfs(node, word)

    def dfs(self, node, word):
        if not word:
            if node.isWord:
                return True
            return False

        if word[0] == ".":
            for n in node.children.values():
                if self.dfs(n, word[1:]):
                    return True
            return False
        else:
            node = node.children.get(word[0], None)
            return False if not node else self.dfs(node, word[1:])

            # Your WordDictionary object will be instantiated and called as such:
            # obj = WordDictionary()
            # obj.addWord(word)
            # param_2 = obj.search(word)