# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger], count=0) -> int:
        def findMaxDepth(nestedList):
            maxDepth = 1
            for x in nestedList:
                if x.getList():
                    maxDepth = max(findMaxDepth(x.getList()) + 1, maxDepth)
            return maxDepth

        def findWeightSum(nestedList, level, depth):
            ans = 0
            for x in nestedList:
                if x.isInteger():
                    ans += level * x.getInteger()
                else:
                    ans += findWeightSum(x.getList(), level - 1, depth + 1)
            return ans

        maxDepth = findMaxDepth(nestedList)
        return findWeightSum(nestedList, maxDepth, 1)