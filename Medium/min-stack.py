class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val):
        if not self.minStack or val <= self.minStack[-1] :
            self.minStack.append(val)
        self.stack.append(val)
        
    def pop(self):
        if self.stack :
            if (self.stack[-1] == self.minStack[-1]) : 
                self.minStack.pop()
            return self.stack.pop()
        
    def top(self):
        if self.stack: 
            return self.stack[-1]
        
    def getMin(self):
        if self.minStack:
            return self.minStack[-1]
