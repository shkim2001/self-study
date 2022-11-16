class Solution:
    def calPoints(self, operations: List[str]) -> int:

        stack = []
        for op in ops:
            if op == '+':
                stack.append(stack[-1] + stack[-2])
            elif op == 'C':
                stack.pop()
            elif op == 'D':
                stack.append(2 * stack[-1])
            else:
                stack.append(int(op))

        return sum(stack)
        
        # stack = []
        
        # for i in range(len(operations)):
        #     currOperation = operations[i]
            
        #     if len(stack) >= 2 and currOperation == "+":
        #         new = stack[-1] + stack[-2]
        #         stack.append(int(new))
            
        #     elif stack and currOperation == "C":
        #         stack.pop()
            
        #     elif stack and currOperation == "D":
        #         new = stack[-1] * 2
        #         stack.append(int(new))
                
        #     elif currOperation.lstrip("-").isdigit():
        #         stack.append(int(currOperation))
            
        # return sum(stack)