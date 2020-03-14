class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def isValid(segment):
            return int(segment) <= 255 if segment and segment[0] != '0' else len(segment) == 1

        def backTrack(s=s, dot=3):
            if dot == 0:
                seg = s
                if isValid(seg):
                    segs.append(seg)
                    output.append('.'.join(segs))
                    segs.pop()

            for i in range(0, min(4, n)):
                seg = s[:i + 1]
                if isValid(seg) and dot >= 1:
                    segs.append(seg)
                    backTrack(s[i + 1:], dot - 1)
                    segs.pop()

        n = len(s)
        output, segs = [], []
        backTrack()
        return output




