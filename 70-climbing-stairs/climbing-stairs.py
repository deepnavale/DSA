class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [-1]*46
        def solve(n):
            if n==0: return 1
            if n<0: return 0
            if dp[n]!=-1: return dp[n]

            else:
                onestep = solve(n-1)
                twostep = solve(n-2)
                dp[n] = onestep + twostep
            return dp[n]


        

        
             
        return solve(n)