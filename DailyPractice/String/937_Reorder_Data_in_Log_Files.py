class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def f(log):
            id_, res = log.split(' ', 1)
            return (0,res, id_) if res[0].isalpha() else (1,)
        return sorted(logs, key = f)