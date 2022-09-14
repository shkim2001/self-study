class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        dic = {}
        for i in range(len(keyboard)):
            dic[keyboard[i]] = i
            
        res = abs(dic[word[0]] - dic[keyboard[0]])
        for j in range(len(word)-1):
            print(dic[word[j]] - dic[word[j+1]])
            temp = abs(dic[word[j]] - dic[word[j+1]])
            res += temp
        
        return res