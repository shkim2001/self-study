class Solution:
    def findSubarrays(self, arr, target):
        result = []
        for i in range(len(arr)):
            currProduct = arr[i]
            currSubArray = [arr[i]]
            right = i
            while currProduct < target:
                result.append(list(currSubArray))
                if right < len(arr) - 1:
                    right += 1
                    currProduct = currProduct * arr[right]
                    currSubArray.append(arr[right])
                else:
                    break

        return result
