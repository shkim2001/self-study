class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        
        prod = nums[0]
        
        for i in range(len(nums)):
            temp = 1
            for j in range(i, len(nums)):
                temp *= nums[j]
                prod = max(prod, temp)
            
        return prod