import collections

class Solution:
    def lengthOfLongestSubstringKDistinct(self, str1: str, k: int) -> int:
      # TODO: Write your code here
        dic = collections.Counter()
        start = 0
        maxLen = 0
    
        for i in range(len(str1)):
            dic[str1[i]] += 1 
            while len(dic) > k:
                temp = str1[start]
                dic[temp] -= 1
                if dic[temp] == 0:
                    del dic[temp]
                start += 1
            maxLen = max(maxLen, i - start + 1)
                
        return maxLen