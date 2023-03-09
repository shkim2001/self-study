class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        dic = collections.Counter()
        
        if s == "":
            return True
        
        for i in range(len(s)):
            dic[s[i]] += 1
        
        for j in range(len(t)):
            if t[j] in list(dic.keys()) and dic[t[j]] > 0:
                dic[t[j]] -= 1
            else:
                t = t.replace(t[j], " ", 1)
        
        if t.replace(" ", "") == s:
            return True
        else:
            return False
        
        