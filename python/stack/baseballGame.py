class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        
        for i in range(len(operations)):
            currOperation = operations[i]
            
            if len(stack) >= 2 and currOperation == "+":
                new = stack[-1] + stack[-2]
                stack.append(int(new))
            
            elif stack and currOperation == "C":
                stack.pop()
            
            elif stack and currOperation == "D":
                new = stack[-1] * 2
                stack.append(int(new))
                
            elif currOperation.lstrip("-").isdigit():
                stack.append(int(currOperation))
            
        return sum(stack)