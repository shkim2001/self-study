class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        textList = text.split(" ")
        temp = []
        
        for i in range(len(textList) - 2):
            if textList[i] == first and textList[i + 1] == second:
                temp.append(textList[i + 2])
        return temp