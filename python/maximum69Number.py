class Solution:
    def maximum69Number (self, num: int) -> int:
        numStr = str(num)
        newNum = numStr.replace("6", "9", 1)
        return newNum
