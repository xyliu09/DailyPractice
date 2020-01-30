class Solution:
    def beforeAndAfterPuzzles(self, phrases: List[str]) -> List[str]:
        words = []
        for p in phrases:
            words.append(p.split())
        res = set()
        for i in range(len(words)):
            for w2 in words[:i]+words[i+1:]:
                if words[i][-1] == w2[0]:
                    r = ' '.join(words[i][:-1] + w2)
                    if r not in res:
                        res.add(r)
        return sorted(list(res))