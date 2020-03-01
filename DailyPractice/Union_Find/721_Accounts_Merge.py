import collections


class DSU:
    def __init__(self):
        self.p = [i for i in range(10001)]
        self.r = [i for i in range(10001)]

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return False
        if self.r[px] < self.r[py]:
            self.p[px] = py
        elif self.r[py] > self.r[px]:
            self.p[py] = px
        else:
            self.p[px] = py
            self.r[py] += 1
        return True


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        dsu = DSU()
        em_to_name = {}
        em_to_id = {}
        i = 0
        for acc in accounts:
            for email in acc[1:]:
                em_to_name[email] = acc[0]
                if email not in em_to_id:
                    em_to_id[email] = i
                    i += 1
                dsu.union(em_to_id[acc[1]], em_to_id[email])
        ans = collections.defaultdict(list)
        for email in em_to_name:
            ans[dsu.find(em_to_id[email])].append(email)
        return [[em_to_name[v[0]]] + sorted(v) for v in ans.values()]