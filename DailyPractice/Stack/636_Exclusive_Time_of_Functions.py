class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:

        res = [0 for _ in range(n)]
        s = []
        i = 0
        while i < len(logs):
            log = logs[i].split(":")
            curId= int(log[0])
            nextTime = int(log[2])
            if log[1] =="start":
                if s:
                    res[s[-1]] += nextTime- curTime
                s.append(curId)
                curTime = nextTime
            else:
                res[s[-1]] += nextTime - curTime + 1
                s.pop()
                curTime = nextTime + 1
            i += 1
        return res