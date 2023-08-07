class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        c = Counter(arr)
        s = set(c.values())
        return len(c) == len(s)