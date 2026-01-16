class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxprofit = 0
        minprice = prices[0]
        for x in prices:
            profit = x- minprice
            maxprofit = max(maxprofit, profit)
            minprice = min(minprice,x)

        return maxprofit
        