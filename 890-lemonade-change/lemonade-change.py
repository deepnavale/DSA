class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        five,ten=0,0
        for i in range(len(bills)):
            if bills[i]==5:
                five+=1
            elif bills[i]==10:
                if five>0:
                    five-=1
                    ten+=1
                else: return False
            elif ten>0 and five>0:
                ten-=1
                five-=1
            elif five>2:
                five-=3
            else: return False
        
        return True

        