class MinStack(object):
    

    def __init__(self):
        self.stack = []
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        if self.stack :
            return self.stack[-1]
        else: return None
        

    def getMin(self):
        """
        :rtype: int
        """
        minVal=self.stack[0]
        for i in self.stack:
            minVal = min(minVal,i )

        return minVal

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()