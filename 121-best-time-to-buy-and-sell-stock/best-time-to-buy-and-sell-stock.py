class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minprice = float('inf')
        maxprofit = 0

        for x in prices:
         profit = x-minprice
         minprice = min(minprice, x)

         maxprofit = max(maxprofit,profit)
 
        return maxprofit
    
        