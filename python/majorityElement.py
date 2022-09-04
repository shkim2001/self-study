from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
#         majority_count = len(nums)//2
#         for num in nums:
#             count = sum(1 for elem in nums if elem == num)
#             if count > majority_count:
#                 return num
            
#         count = Counter()
#         n = len(nums)
#         for i in range(n):
#             count[nums[i]] += 1
        
#             if count[nums[i]] > n // 2:
#                 return nums[i]

#         counts = Counter(nums)
#         return max(counts.keys(), key = counts.get)
        
        nums.sort()
        return nums[len(nums)//2]
#         count = 0
#         candidate = None

#         for num in nums:
#             if count == 0:
#                 candidate = num
#             count += (1 if num == candidate else -1)

#         return candidate