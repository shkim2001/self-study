class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        res = []
        temp = []
        for i in range(1, len(strs)):
            for j in range(len(strs[i])):
                if ord(strs[i-1][j]) > ord(strs[i][j]) and j not in temp:
                    temp.append(j)
                    res.append(strs[i])

        return len(res)