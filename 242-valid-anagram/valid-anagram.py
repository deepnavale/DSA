class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # for x in s:
        #     cntinc = 0
        #     for y in t:
        #         if x ==y:   
        #             t = t.replace(y,'',1)
        #             cntinc=1
        #             break
        #     if cntinc==0:
        #         return False
        # return True

        return sorted(s)==sorted(t)
        
                