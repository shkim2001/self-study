
class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        column = ""
        
        #for columns A-Z
        if columnNumber <= 26:
            return upper(chr(columnNumber+96))
        
        #Z exception cases
        Z = False
        if columnNumber%26 == 0:
            Z = True
            columnNumber -= 1
        
        #used to see how many times 26 goes into columnNumber
        numTimes = 1
        tempNum = columnNumber
        
        #see how many times 26 goes into columnNum
        while (tempNum/26 > 26):
            numTimes += 1
            tempNum = tempNum/26
            
        #finds the cooresponding letter
        while numTimes >= 0:
            column += upper(chr((columnNumber/(26**numTimes))+96))
            columnNumber = columnNumber%(26**numTimes)
            numTimes -= 1  
        
        #Z excpetion case, drops the last letter of the column and
        #adds "Z"
        if Z == True:
            column = column[0:len(column)-1] + "Z"
        
        #returns the column
        return column