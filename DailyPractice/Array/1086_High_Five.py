class Solution:
    import collections
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        dic = collections.defaultdict(list)
        for id, s in items:
            dic[id].append(s)
        res = []
        for k, i in dic.items():
            allscore = sorted(i, reverse= True)
            res.append([k, int(sum(allscore[0:5])/5)])
        return res