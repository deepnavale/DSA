class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        while(len(stones)>1):
            stones.sort()
            lst = stones.pop()
            stones[-1]= abs(stones[-1]-lst)
            # sec_lst = stones.pop()
        ans = stones[0] if stones[0]>0 else  0
        return ans
