class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if not n:
            return 1
        if n < 0:
            return self.myPow(1 / x, -n)
        if not n % 2:
            return self.myPow(x * x, n / 2)

        return x * self.myPow(x, n - 1)