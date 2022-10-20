class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        minimum = float(inf)
        res = []
        
        for i in range(len(arr) - 1):
            if abs(arr[i] - arr[i+1]) < minimum:
                minimum = abs(arr[i] - arr[i+1])
                
        for i in range(len(arr) - 1):
            if abs(arr[i] - arr[i+1]) == minimum:
                res.append([min(arr[i], arr[i+1]), max(arr[i], arr[i+1])])
                
        return res