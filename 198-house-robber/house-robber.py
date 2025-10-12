class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        dp = [-1]*(n+1)
        dp[0]=0
        dp[1]=nums[0]
        for i in range(2,n+1):
            steal = dp[i-2] + nums[i-1]
            skip = dp[i-1]
            dp[i] = max(steal,skip)


        return dp[n]
