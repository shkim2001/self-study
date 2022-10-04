import collections
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        if len(nums) == k:
            return nums
        
        count = collections.Counter()
        minHeap, result = [], []
        
        for num in nums:
            count[num] += 1
        
        for num, freq in count.items():
            heappush(minHeap, [-freq, num])
        
        for i in range(k):
            result.append(heappop(minHeap)[1])
            
        return result