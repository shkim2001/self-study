class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        pointer = 0
        temp = currentState
        lst = []
        
        
        while pointer < len(currentState) - 1:
            nextPointer = pointer + 1
            if currentState[pointer] == "+" and currentState[nextPointer] == "+":
                currentState = currentState[:pointer] + "--" + currentState[nextPointer+1:]
                lst.append(currentState)
            currentState = temp
            pointer += 1
            
        return lst
        
        