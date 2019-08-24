class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        maxProfitMiddle, buy, sell = self.helper(prices, 0, len(prices) - 1, 1)
        print(maxProfitMiddle, buy, sell)
        maxLossMiddle, _, _ = self.helper(prices, buy, sell, -1)
        maxProfitBefore, _, _ = self.helper(prices, 0, buy - 1, 1)
        maxProfitAfter, _, _ = self.helper(prices, sell, len(prices) - 1, 1)
        return maxProfitMiddle + max(maxLossMiddle, maxProfitBefore, maxProfitAfter)

    def helper(self, prices, i, j, isProfit):
        assert i >= 0 and i < len(prices), 'i dsa'
        if j <= i:
            return 0, 0, 0
        maxProfit = 0
        minSoFar, minSoFarIndex = prices[i], i
        buyPoint, sellPoint = i, i

        if isProfit == 1:
            for k in range(i, j + 1):
                print(k)
                if prices[k] - minSoFar > maxProfit:
                    maxProfit = prices[k] - minSoFar
                    sellPoint = k
                    buyPoint = minSoFarIndex
                if minSoFar > prices[k]:
                    minSoFar = prices[k]
                    minSoFarIndex = k

        else:
            for k in range(i, j + 1):
                if prices[k] - minSoFar < maxProfit:
                    maxProfit = prices[k] - minSoFar
                    sellPoint = k
                    buyPoint = minSoFarIndex
                if minSoFar < prices[k]:
                    minSoFar = prices[k]
                    minSoFarIndex = k

        return maxProfit * isProfit, buyPoint, sellPoint


