class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        for p in 2, 3, 5:
            print(num%p)
            while num%p == 0 and num > 0:
                print (num)
                num /= p

        return num == 1
