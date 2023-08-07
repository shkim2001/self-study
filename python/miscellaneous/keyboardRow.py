class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        line1 = set("qwertyuiop")
        line2 = set("asdfghjkl")
        line3 = set("zxcvbnm")
        
        return [word for word in words if set(word.lower()).issubset(line1) or 
               set(word.lower()).issubset(line3) or
               set(word.lower()).issubset(line2)]