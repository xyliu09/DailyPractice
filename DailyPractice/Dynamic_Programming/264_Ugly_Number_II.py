class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ugly = [1]
        i2, i3, i5 = 0, 0, 0
        while n > 1:
            num2, num3, num5 = 2 * ugly[i2], 3 * ugly[i3], 5 * ugly[i5]
            nummin = min(num2, num3, num5)
            if nummin == num2:
                i2 += 1
            if nummin == num3:
                i3 += 1
            if nummin == num5 :
                i5 += 1
            ugly.append(nummin)
            n -= 1
        return ugly[-1]