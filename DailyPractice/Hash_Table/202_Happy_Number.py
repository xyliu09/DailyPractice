'''
202. Happy Number
Easy

1603

357

Add to List

Share
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example:

Input: 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

'''

class Solution:
    def isHappy(self, n: int) -> bool:
        dic = set()
        while n != 1 and n not in dic:
            dic.add(n)
            total = 0
            while n:
                n, div= divmod(n, 10)
                total += div**2
            n = total
        return n == 1