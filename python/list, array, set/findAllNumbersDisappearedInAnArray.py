import collections

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        count = collections.Counter()
        res = []
        minimum = 1
        
        for i in range(len(nums)):
            count[nums[i]] += 1
        
        while minimum <= len(nums):
            if minimum not in count:
                res.append(minimum)
            minimum += 1
            
    
        return res