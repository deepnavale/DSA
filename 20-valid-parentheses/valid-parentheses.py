class Solution(object):
   
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []

        pairs ={')':'(',"]":'[',"}":"{"}

        for c in s:
            if c in pairs:
                if not stack: return False
                if stack[-1]==pairs[c]:
                    stack.pop()
                else: return False
            else: stack.append(c)
        return len(stack)==0
                
        # for c in s:
        #     if c in [']',')','}']:
        #         if len(stack)==0 : return False
        #         t=stack[-1]
        #         if t=='('and c==')' or  t=='{'and c=='}' or  t=='['and c==']' :
        #             stack.pop()
        #         else: return False
        #     else: stack.append(c)

       
        
        # return len(stack) == 0