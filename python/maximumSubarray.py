class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = [0 for i in range(len(nums))]
        n[0] = nums[0]
        for i in range(1, len(nums)):
            n[i] = max(n[i-1] + nums[i], nums[i])
        return max(n)