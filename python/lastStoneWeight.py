class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones = sorted(stones)[::-1]
            if stones[0] != stones[1]:
                stones.append(abs(stones[0] - stones[1]))
            stones = stones[2:]
        
        if len(stones) == 0:
            return 0
        
        return stones[0]
            