class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        indegree = {}
        for x, y in prerequisites:
            graph[y].append(x)
            indegree[x] = indegree.get(x, 0) + 1
        queue = [i for i in range(numCourses) if i not in indegree]
        ans = []
        while queue:
            c = queue.pop(0)
            ans.append(c)
            for neighbor in graph[c]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        return ans if len(ans) == numCourses else []
