class Solution(object):
    def minIncrementForUnique(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if not A or len(A) <= 1:
            return 0
        A.sort()
        res, prev = 0, A[0]
        for i in range(1,len(A)):
            expect = prev+1
            res += 0 if A[i] > expect else expect - A[i]
            prev = max(A[i], expect)
        return res