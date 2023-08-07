class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {
                "2": ["a", "b", "c"], 
                "3": ["d", "e", "f"], 
                "4": ["g", "h", "i"], 
                "5": ["j", "k", "l"], 
                "6": ["m", "n", "o"], 
                "7": ["p","q","r","s"], 
                "8": ["t","u","v"], 
                "9": ["w","x","y","z"]
            }
        
        lst = []
        
        if len(digits) == 0:
            return []
        
        for num in range(len(digits)): 
            if digits[num] in dic.keys(): 
                lst.append(dic.get(digits[num]))
        
        while len(lst) > 1:
            l1 = lst.pop()
            l2 = lst.pop()
            ans = []
            for i in l1:
                for j in l2:
                    ans.append(j+i)
            lst.append(ans)
            
        return lst[0]