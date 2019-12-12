# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        isCelebrity = [True for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if isCelebrity[i] and i != j:
                    if knows(i, j) or not knows(j, i):
                        isCelebrity[i] = False
                        break
                    else:
                        isCelebrity[j] = False
            if isCelebrity[i]:
                return i
        return -1

'''
#Need to see the following approach
class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        for i in range(1, n):
            if knows(res, i):
                res = i
        for i in range(n):
            if i != res and (knows(res, i) or not knows(i, res)):
                return -1
        return res

'''





