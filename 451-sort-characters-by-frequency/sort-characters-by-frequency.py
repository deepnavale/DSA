class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        map = {}
        for ch in s:
            map[ch] = map.get(ch,0)+1
        sorted_map = sorted(map.items(),key=lambda x:x[1],reverse=True)
        res = ""
        for ch,freq in sorted_map:
            res += ch*freq
        return res

    