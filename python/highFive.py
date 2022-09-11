class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        dic={}
        for i in range(len(items)):
            dic[items[i][0]]= list(dic.get(items[i][0],[])) + [items[i][1]]

        res=[]    
        for i in sorted(dic.keys()):
            dic[i].sort(reverse=True)
            res.append([i,sum(dic[i][0:5])//5])

        return res