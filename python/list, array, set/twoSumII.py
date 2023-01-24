class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            
            tempSum = numbers[left] + numbers[right]
            if tempSum < target:
                left += 1
                
            elif tempSum > target:
                right -= 1
                
            else:
                return [left + 1, right + 1]
        return [-1, -1]