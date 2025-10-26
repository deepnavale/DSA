class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = dict()
        for x in nums:
            d[x] = d.get(x,0)+1
        sorted_d = sorted(d.items(),key=lambda v:v[1],reverse=True)
        lst=[]
        cnt=0
        for freq in sorted_d :
            if cnt==k: break
            lst.append(freq[0])
            cnt+=1
        return lst

    
        
    