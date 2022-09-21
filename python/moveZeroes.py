class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        numberOfZero = nums.count(0)
        
        for _ in range(numberOfZero):
            nums.remove(0)
            nums.append(0)