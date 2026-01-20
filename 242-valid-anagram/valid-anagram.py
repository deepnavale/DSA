class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cnt =0
        if len(s) != len(t):
            return False
        for x in s:
            cntinc = 0
            for y in t:
                if x ==y:   
                    t = t.replace(y,'',1)
                    cnt+=1
                    cntinc=1
                    break
            if cntinc==0:
                return False
        return True
        
                