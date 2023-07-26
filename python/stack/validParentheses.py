class Solution:
    def isValid(self, s: str) -> bool:
        bracketDic = {"{": "}", "(": ")", "[": "]"}
        bracketStack = []
        for bracket in s:
            if bracket in bracketDic:
                bracketStack.append(bracket)
            else:
                if len(bracketStack) == 0:
                    return False
                curr = bracketStack.pop()
                if bracketDic[curr] != bracket:
                    return False
        
        if len(bracketStack) != 0:
            return False

        return True