class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [] # list of results
        
        for i in range(len(nums)): #first element of the sum
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            l = i + 1 # pointer for nums[j]
            r = len(nums) - 1 # pointer for nums[k]
            
            while l < r:
                threeSum = nums[i] + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        
#         res = [] #list of results
        
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 for k in range(j + 1, len(nums)):
#                     if nums[i] + nums[j] + nums[k] == 0 and sorted([nums[i], nums[j], nums[k]]) not in res:
#                         res.append(sorted([nums[i], nums[j], nums[k]]))
                        
        return res