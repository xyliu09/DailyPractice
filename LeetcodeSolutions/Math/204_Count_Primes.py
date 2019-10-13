'''
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0
        s = [1] * n
        s[0], s[1] = 0, 0
        for i in range(2, int(n**0.5)+1):
            if s[i] == 1:
                s[i*i: n: i] = [0]*len(s[i*i:n:i])
        return sum(s)
'''

import math
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        isPrime = [True for _ in range(n)]
        m = int(math.sqrt(n))
        for i in range(2, m + 1):
            if isPrime[i - 1]:
                for j in range(i + i, n, i):
                    isPrime[j - 1] = False
        count = 0
        for i in range(2, n):
            if isPrime[i - 1]:
                count += 1
        return count

    def isPrime(self, x):
        if x == 1:
            return False
        n = math.sqrt(x)
        for k in range(2, int(n)):
            if x % k == 0:
                return False
        return True
