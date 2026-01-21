class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        i=0
        for x in nums:
            rem = target - x
            if rem in seen:
                
                return [seen[rem], i]
            seen[x]= i
            i+=1

        # for i,x in enumerate(nums):
        #     rem = target -x
        #     if rem in seen:
        #         return [seen[rem],i] 
        #     seen[x] = i