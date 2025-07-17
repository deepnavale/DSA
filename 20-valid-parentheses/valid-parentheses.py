class Solution(object):
   
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s:
            if c in [']',')','}']:
                if len(stack)==0 : return False
                t=stack[-1]
                if t=='('and c==')' or  t=='{'and c=='}' or  t=='['and c==']' :
                    stack.pop()
                else: return False
            else: stack.append(c)

       
        
        return len(stack) == 0