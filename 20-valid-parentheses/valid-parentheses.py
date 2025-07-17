class Solution(object):
    def isClosed(self,c):
        return c=='}' or c==']' or c==')'
    
    def isOpp(self,curr,prev):
        return (curr==')' and prev=='(') or (curr==']' and prev=='[') or (curr=='}' and prev=='{')

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s:
            if self.isClosed(c):
                if len(stack) == 0:
                    return False
                elif self.isOpp(c,stack[-1]):
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return len(stack) == 0