class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        maxheap = [-stone for stone in stones]
        heapq.heapify(maxheap)
        while len(maxheap)>1:
            x=heapq.heappop(maxheap)
            y= heapq.heappop(maxheap)
            heapq.heappush(maxheap,(x-y))
        return -maxheap[0]



        # while(len(stones)>1):
        #     stones.sort()
        #     x=stones.pop()
        #     y=stones.pop()
        #     if x!=y:
        #         stones.append(x-y)
        # return stones[0] if stones else 0






        #     stones.sort()
        #     lst = stones.pop()
        #     stones[-1]= abs(stones[-1]-lst)
        #     # sec_lst = stones.pop()
        # ans = stones[0] if stones[0]>0 else  0
        # return ans
