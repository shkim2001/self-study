class Solution:
    def findLength(self, str1, k):
        max_length = 0
        counterDict = {}
        startIndex = 0

        for i in range(len(str1)):
            if str1[i] not in counterDict:
                counterDict[str1[i]] = 0
            counterDict[str1[i]] += 1

            while len(counterDict) > k:
                counterDict[str1[startIndex]] -= 1
                if counterDict[str1[startIndex]] == 0:
                    del counterDict[str1[startIndex]]
                startIndex += 1

            max_length = max(i - startIndex + 1, max_length)
        return max_length
