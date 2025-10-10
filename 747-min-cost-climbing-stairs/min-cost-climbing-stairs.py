class Solution(object):


    def solve(self,i,n,cost,dp):
        if i>=n : return 0
        if dp[i]!=-1 : return dp[i]

        a=cost[i]+self.solve(i+1,n,cost,dp)
        b=cost[i]+self.solve(i+2,n,cost,dp)
        dp[i]=min(a,b)
        return dp[i]
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n=len(cost)
        dp=[-1]*1001
        return min(self.solve(0,n,cost,dp),self.solve(1,n,cost,dp))

   

        