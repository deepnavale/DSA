class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if len(nums)==1:
            return 0
        List = nums.sort()
        maxstore= max(nums)
        maxs = max(nums)
        for i in range(len(nums)-k+1):
            maxstore = nums[i+k-1] -nums[i]
            maxs = min(maxs, maxstore)
        return maxs
        