class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        p1, p2 = 0, 0
        res = []
        while p1 < len(A) and p2 < len(B):
            l = max(A[p1][0], B[p2][0])
            h = min(A[p1][1], B[p2][1])
            if l <= h:
                res.append([l, h])
            if A[p1][1] < B[p2][1]:
                p1 += 1
            else:
                p2 += 1
        return res
