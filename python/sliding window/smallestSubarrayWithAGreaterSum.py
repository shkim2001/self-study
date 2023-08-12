import math


class Solution:
    def findMinSubArray(self, s, arr):
        output = math.inf
        startIndex = 0
        currSum = 0
        for i in range(len(arr)):
            currSum += arr[i]
            while currSum >= s:
                output = min(output, i - startIndex + 1)
                currSum -= arr[startIndex]
                startIndex += 1
        if output == math.inf:
            return 0

        return output
