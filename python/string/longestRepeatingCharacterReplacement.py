class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dic = collections.Counter()
        res = 0
        left = 0
        
        for i in range(len(s)):
            dic[s[i]] += 1
            while (i - left + 1) - max(dic.values()) > k:
                dic[s[left]] -= 1
                left += 1
            res = max(res, i - left + 1)
        
        return res