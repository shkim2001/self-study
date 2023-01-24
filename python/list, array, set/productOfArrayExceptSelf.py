class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        temp = 1
        n = len(nums)
        for i in range(n):
            if i > 0:
                temp *= nums[i-1]
            output.append(temp)
        
        temp = 1
        nums.reverse()
        for i in range(n):
            if i > 0:
                temp *= nums[i-1]
            output[n-i-1] *= temp
        
        return output
                       