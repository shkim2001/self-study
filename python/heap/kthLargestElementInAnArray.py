class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        for i in range(len(nums)):
            heapq.heappush(minHeap, -nums[i])
        
        for i in range(k - 1):
            heapq.heappop(minHeap)
        
        return -minHeap[0]