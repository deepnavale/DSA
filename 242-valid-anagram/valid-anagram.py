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

        # a = list(s)
        # b = list(t)
        # a.sort()
        # b.sort()
        # return a==b

        sfreq = {}
        tfreq = {}
        for x in s:
            sfreq[x] = sfreq.get(x,0) + 1
        for x in t:
            tfreq[x] = tfreq.get(x,0) + 1
        
        for x in list(sfreq):
            if x not in tfreq:
                return False
            else:
                sfreq[x] -= tfreq[x]
                if sfreq[x]==0:
                    del sfreq[x]
        return not sfreq
        
        # for x in sfreq:
        #     if x not in tfreq:
        #         return False
        #     elif sfreq[x]!=tfreq[x]:
        #         return False
        # return True

            
        # for key, val in sfreq.items():
            # if key in tfreq:
            #     if sfreq[key]!=tfreq[key]:
            #         return False
            # else:
            #     return False

            # if sfreq[key] != tfreq.get(key,0):
            #     return False
        # return True
                