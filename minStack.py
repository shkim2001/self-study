class MinStack(object):
    
    def __init__(self):
        self.stack = []
        self.min_stack = []        
        

    def push(self, x):
        
        self.stack.append(x)
        
        if not self.min_stack or x < self.min_stack[-1][0]:
            self.min_stack.append([x, 1])
            
        elif x == self.min_stack[-1][0]:
            self.min_stack[-1][1] += 1

    
    def pop(self):

        if self.min_stack[-1][0] == self.stack[-1]:
            self.min_stack[-1][1] -= 1
            
        if self.min_stack[-1][1] == 0:
            self.min_stack.pop()
            
        self.stack.pop()


    def top(self):
        return self.stack[-1]


    def getMin(self):
        return self.min_stack[-1][0]   