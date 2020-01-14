import collections


class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        length = len(A)
        counter = collections.Counter(A) + collections.Counter(B)
        minCost = length + 1
        for num, time in counter.items():
            if time >= length:
                minCost = min(minCost, self.cost(A, B, num))
        return -1 if minCost == length + 1 else minCost

    def cost(self, A, B, num):
        costA, costB = 0, 0
        for i in range(len(A)):
            if A[i] != num and B[i] != num:
                return -1
            if A[i] == B[i] == num:
                continue
            if A[i] != num:
                costA += 1
            if B[i] != num:
                costB += 1
        return min(costA, costB)

