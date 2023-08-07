class Solution:
    def judgeCircle(self, moves: str) -> bool:
        dic = collections.Counter()
        for i in range(len(moves)):
            dic[moves[i]] += 1
        
        if dic["U"] == dic["D"] and dic["L"] == dic["R"]:
            return True
        
        return False