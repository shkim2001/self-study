class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        minHeap = []
        for i in range(len(stones)):
            heapq.heappush(minHeap, -stones[i])
        while len(minHeap) > 1:
            firstStone = heapq.heappop(minHeap)
            secondStone = heapq.heappop(minHeap)
            if firstStone < secondStone:
                heapq.heappush(minHeap, -(secondStone - firstStone))
            elif firstStone > secondStone:
                heapq.heappush(minHeap, -(firstStone - secondStone))
        
        if minHeap:
            return -heapq.heappop(minHeap)

        return 0

        # while len(stones) > 1:
        #     stones = sorted(stones)[::-1]
        #     if stones[0] != stones[1]:
        #         stones.append(abs(stones[0] - stones[1]))
        #     stones = stones[2:]
        
        # if len(stones) == 0:
        #     return 0
        
        # return stones[0]