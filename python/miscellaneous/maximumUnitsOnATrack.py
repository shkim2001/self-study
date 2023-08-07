class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes, key=lambda t: t[1], reverse=True)
        output = 0
        
        while truckSize > 0:
            if len(boxTypes) == 0:
                return output
            if truckSize < boxTypes[0][0]:
                output += boxTypes[0][1]
                truckSize -= 1
            else:
                output += (boxTypes[0][0] * boxTypes[0][1])
                truckSize -= boxTypes[0][0] 
                boxTypes = boxTypes[1:]
                
        return output