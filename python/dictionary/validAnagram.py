class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        for char in s:
            if char not in dic:
                dic[char] = 1
            else: 
                dic[char] += 1
        
        for char in t:
            if char not in dic:
                return False
            elif dic[char] == 1:
                dic.pop(char)
            else:
                dic[char] -= 1
        
        return len(dic) == 0
