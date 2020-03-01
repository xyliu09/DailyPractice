import collections


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = collections.defaultdict(list)
        for x, y in connections:
            graph[x].append(y)
            graph[y].append(x)
        low = [0 for i in range(n)]

        def dfs(curr, parent, level):
            low[curr], res = level, []
            for neighbor in graph[curr]:
                if neighbor == parent:
                    continue
                if not low[neighbor]:
                    res += dfs(neighbor, curr, level + 1)
                low[curr] = min(low[curr], low[neighbor])
                if low[neighbor] == level + 1:
                    res.append([neighbor, curr])
            return res

        return dfs(0, -1, 1)

