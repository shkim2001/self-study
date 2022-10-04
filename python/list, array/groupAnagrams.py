import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic, tempDic = {}, {}
        
        for i in range(len(strs)):
            temp = strs[i]
            sortedList = "".join(sorted(temp))
            if sortedList not in tempDic:
                tempDic[sortedList] = [temp]
            else:
                tempDic[sortedList].append(temp)
        return list(tempDic.values())
            
        