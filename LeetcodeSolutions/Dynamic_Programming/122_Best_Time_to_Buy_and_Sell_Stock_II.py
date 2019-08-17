class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxProfit = 0
        for p in prices:
            try:
                maxProfit = max(maxProfit, p - minSoFar)
                minSoFar = min(minSoFar, p)
            except:
                minSoFar = p
        return maxProfit