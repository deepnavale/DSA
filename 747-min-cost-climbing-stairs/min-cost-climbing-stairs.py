class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        a, b = 0, 0  # cost to reach top from "beyond" last step
        for i in range(n-1, -1, -1):
            c = cost[i] + min(a, b)
            a, b = b, c
        return min(a, b)