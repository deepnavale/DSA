class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = [0]*2*len(nums)
        n = len(nums)
        ans[:n]= nums
        ans[n:2*n]= nums
        return ans
        