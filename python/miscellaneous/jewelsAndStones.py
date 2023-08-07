class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewelsList = []
        count = 0
        
        for i in range(len(jewels)):
            jewelsList.append(jewels[i])
            
        for j in range(len(stones)):
            if stones[j] in jewelsList:
                count += 1
                
        return count