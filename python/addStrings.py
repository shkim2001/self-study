class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1Int = 0
        num2Int = 0
        num1 = num1[::-1]
        num2 = num2[::-1]
        for i in range(len(num1)):
            num1Int += 10**i * int(num1[i])
            
        for i in range(len(num2)):
            num2Int += 10**i * int(num2[i])
            
        return str(num1Int + num2Int)