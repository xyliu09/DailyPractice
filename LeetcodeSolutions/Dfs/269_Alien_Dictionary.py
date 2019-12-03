from collections import defaultdict


class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        graph = defaultdict(set)
        for i in range(len(words)):
            for j in range(len(words[i])):
                graph[words[i][j]] = set()

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    if w2[j] not in graph[w1[j]]:
                        print
                        w1[j], w2[j]
                        graph[w1[j]].add(w2[j])
                    break
        visited = {k: 0 for k in graph.keys()}

        self.res = []
        for v in graph:
            if not self.dfs(graph, v, visited): return ""
        return ''.join(self.res[::-1])

    def dfs(self, graph, v, visited):
        if visited[v] == 1:
            return False
        if visited[v] == -1:
            return True
        visited[v] = 1
        for neighbor in graph[v]:
            if not self.dfs(graph, neighbor, visited):
                return False
        visited[v] = -1
        self.res.append(v)
        return True