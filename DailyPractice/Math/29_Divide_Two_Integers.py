class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == -2**31 and divisor == -1:
            return 2**31-1
        sign = 1 if (dividend < 0) == ( divisor < 0) else -1
        res = 0
        divisor, dividend = abs(divisor), abs(dividend)
        while divisor <= dividend:
            temp = divisor
            m = 1
            while (temp<<1) <= dividend:
                temp <<= 1
                m <<= 1
            dividend -= temp
            res += m
        return sign * res