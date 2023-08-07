class Solution:
    def findMaxSumSubArray(self,k, arr):
        maxSum = 0
        for i in range(len(arr) - k + 1):
            currSum = 0
            for j in range(i, i + k):
                currSum += arr[j]
            maxSum = max(maxSum, currSum)

        return maxSum
    
