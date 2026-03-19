class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sdict = {}
        tdict = {}
        for char in s:
            sdict[char] = sdict.get(char,0) + 1
        for char in t:
            tdict[char] = tdict.get(char,0) +1
        
        for k,v in sdict.items():
            if k not in tdict:
                return False
            if tdict[k] != v:
                return False
        
        return True