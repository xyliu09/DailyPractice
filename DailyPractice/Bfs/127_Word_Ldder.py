import collections

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        L = len(beginWord)
        wordDict = collections.defaultdict(list)
        for word in wordList:
            for i in range(L):
                wordDict[word[:i] + "*" + word[i + 1:]].append(word)
        count = 1
        queue = [(beginWord, count)]
        visited = {beginWord: True}
        while queue:
            word, count = queue.pop(0)

            for i in range(L):
                key = word[:i] + "*" + word[i + 1:]
                for intermediateword in wordDict[key]:
                    if intermediateword == endWord:
                        return count + 1
                    if intermediateword not in visited:
                        visited[intermediateword] = True
                        queue.append((intermediateword, count + 1))
                wordDict[key] = []
        return 0
