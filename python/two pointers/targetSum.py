class Solution:
    def search(self, arr, target_sum):

        start = 0
        end = len(arr) - 1

        while start < end:
            if arr[start] + arr[end] > target_sum:
                end -= 1
            elif arr[start] + arr[end] < target_sum:
                start += 1
            else:
                return [start, end]
            
        return [-1, -1]
