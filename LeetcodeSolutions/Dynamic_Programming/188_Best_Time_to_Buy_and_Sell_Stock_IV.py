class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        maxprofit = 0
        if k > len(prices) // 2:
            for i in range(1, len(prices)):
                if prices[i] > prices[i - 1]:
                    maxprofit += prices[i] - prices[i - 1]
            return maxprofit

        hold = [float('-inf') for _ in range(k + 1)]
        release = [0 for _ in range(k + 1)]

        for p in prices:
            for i in range(1, k + 1):
                hold[i] = max(hold[i], release[i - 1] - p)
                release[i] = max(release[i], hold[i] + p)

        return release[-1] if k > 0 else 0