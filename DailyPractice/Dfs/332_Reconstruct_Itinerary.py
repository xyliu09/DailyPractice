# Reverse Order Topological sort
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        for x, y in sorted(tickets)[::-1]:
            graph[x].append(y)
        ans = []

        def dfs(start):
            while graph[start]:
                dfs(graph[start].pop())
            ans.append(start)

        dfs('JFK')
        return ans[::-1]

