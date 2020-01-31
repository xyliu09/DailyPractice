import collections
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        lookup = collections.defaultdict(list)
        for p in paths:
            path, value = p.split(' ')[0], p.split(' ')[1:]
            for v in value:
                lookup[v.split('.')[-1]].append(path + '/' + v.split('.')[0])
        res = []
        for k, v in lookup.items():
            res.append([n + '.' + k.split('(')[0] for n in v])
        return [x for x in res if len(x) > 1]
