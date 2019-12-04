from collections import deque, defaultdict


class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        graph = defaultdict(set)
        indegree = {}
        for i in range(len(words)):
            for j in range(len(words[i])):
                graph[words[i][j]] = set()
                indegree[words[i][j]] = 0

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    if w2[j] not in graph[w1[j]]:
                        graph[w1[j]].add(w2[j])
                        indegree[w2[j]] = indegree.get(w2[j]) + 1
                    break
        queue = []
        for c in indegree:
            if indegree[c] == 0:
                queue.append(c)
        res = []
        while queue:
            c = queue.pop(0)
            res.append(c)
            for neighbor in graph[c]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        if len(res) != len(indegree): return ""
        return ''.join(res[::])

