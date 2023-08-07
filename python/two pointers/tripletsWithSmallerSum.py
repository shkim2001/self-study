class Solution:
    def searchTriplets(self, arr, target):
        arr.sort()
        count = 0
        for i in range(len(arr)):
            targetDiff = target - arr[i]
            left = i + 1
            right = len(arr) - 1
            while left < right:
                if arr[left] + arr[right] < targetDiff:
                    count += right - left
                    left += 1
                else:
                    right -= 1
            
        return count
