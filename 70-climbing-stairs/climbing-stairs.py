class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n==1 : return 1

        a=1
        b=1
        c=a+b

        for i in range(2,n+1):
            c = a+b
            a=b
            b=c
        return c

       
