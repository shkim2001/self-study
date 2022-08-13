class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        min_row = m
        min_col = n
        for op in ops:
            if op[0] < min_row:
                min_row = op[0]
            if op[1] < min_col:
                min_col = op[1]
        return min_row * min_col